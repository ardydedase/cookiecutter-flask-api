import os

from app.config import development, docker, production, test

# Solves the loading of config values issue
config_env_map = {
    'development': development,
    'test': test,
    'docker': docker,
    'production': production,
}

def get_env_config(env):
    return config_env_map.get(env, development)