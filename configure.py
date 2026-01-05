#!/usr/bin/env python3

import os
import sys


LOCAL_ENV = {
    'ION_API_CACHE_ENABLED': '0',
    'ION_API_CACHE_REDIS_ENDPOINT': 'cache_redis',
    'ION_API_CACHE_REDIS_PORT': '6379',
    'ION_API_CACHE_REDIS_TIMEOUT': '1',
    'ION_API_LOGS_JSONIFY': '0',
    'ION_API_LOGS_LEVEL': 'ERROR',
    'ION_API_GET_METHODS_ENABLED': '1',
    'ION_API_HTTP_PORT': '80',
    'ION_API_JSON_RPC_ENABLED': '1',
    'ION_API_ROOT_PATH': '/',
    'ION_API_WEBSERVERS_WORKERS': '1',
    'ION_API_TONLIB_LITESERVER_CONFIG': 'private/mainnet.json',
    'ION_API_TONLIB_KEYSTORE': '/tmp/ion_keystore/',
    'ION_API_TONLIB_PARALLEL_REQUESTS_PER_LITESERVER': '50',
    'ION_API_TONLIB_CDLL_PATH': '',
    'ION_API_TONLIB_REQUEST_TIMEOUT': '10',
    'ION_API_GUNICORN_FLAGS': ''
}


def strtobool(val):
    if val.lower() in ['y', 'yes', 't', 'true', 'on', '1']:
        return True
    if val.lower() in ['n', 'no', 'f', 'false', 'off', '0']:
        return False
    raise ValueError(f"Invalid bool value {val}")

def main():
    default_env = LOCAL_ENV

    for var in default_env.keys():
        if os.getenv(var) != None:
            default_env[var] = os.getenv(var)

    compose_file = 'docker-compose.yaml'

    cache_enabled = strtobool(default_env['ION_API_CACHE_ENABLED'])
    if cache_enabled:
        compose_file += ':docker-compose.cache.yaml'
    default_env['COMPOSE_FILE'] = compose_file

    env_content = ''
    for k, v in default_env.items():
        env_content += f'{k}={v}\n'

    with open(os.path.join(sys.path[0], ".env"), "w") as f:
        f.write(env_content)

    print(".env file created.")

if __name__ == '__main__':
    main()
