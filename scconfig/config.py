"""Configurations

Copyright (c) 2021 Scott Lau
"""

import logging
import os

from config42 import ConfigManager


class Config:

    @staticmethod
    def _get_config_file_path(project_name, environment):
        config_directory = '.{}'.format(project_name)
        return os.path.join('/var/opt/sc', '{}/{}.yml'.format(config_directory, environment))

    @staticmethod
    def create(*, project_name, environment=None, defaults={}):
        prefix = project_name.upper()
        prefix = prefix.replace("-", "_")
        # load defaults from defaults.py file
        config = ConfigManager(defaults=defaults)
        # load defaults from home directory
        config_file = Config._get_config_file_path(project_name, "default")
        if os.path.exists(config_file):
            logging.getLogger(__name__).info("loading default configurations from %s", config_file)
            config.set_many(ConfigManager(path=config_file).as_dict())
        # load environment configurations from environment variables
        env_config = ConfigManager(prefix=prefix)
        config.set_many(env_config.as_dict())

        key_env = "environment"
        if environment is None:
            environment = env_config.get(key_env)
            if environment is None:
                # use production configuration if not specified environment
                environment = "production"
                logging.getLogger(__name__).info("did not specify environment, using %s", environment)
        else:
            logging.getLogger(__name__).info("using environment: %s", environment)
        config.set(key_env, environment)
        # load environment configurations from file
        env_config_file = Config._get_config_file_path(project_name, environment)
        if os.path.exists(env_config_file):
            logging.getLogger(__name__).info("loading environmental configurations from %s", env_config_file)
            config.set_many(ConfigManager(path=env_config_file).as_dict())
        return config
