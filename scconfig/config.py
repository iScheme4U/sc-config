"""Configurations

Copyright (c) 2021 Scott Lau
"""

#  The MIT License (MIT)
#
#  Copyright (c) 2021. Scott Lau
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE.

import logging
import os

from config42 import ConfigManager


class Config:

    @staticmethod
    def _get_cur_dir_config_file_path(environment):
        """Top priority configuration file

        :param environment:
        :return:
        """
        filename = '{}.yml'.format(environment)
        return os.path.join(os.getcwd(), filename)

    @staticmethod
    def _get_user_dir_config_file_path(project_name, environment):
        """Second priority configuration file

        :param environment:
        :return:
        """
        config_directory = '{}'.format(project_name)
        filename = '{}/{}.yml'.format(config_directory, environment)
        return os.path.join(os.path.expanduser('~'), filename)

    @staticmethod
    def _get_config_file_path(project_name, environment):
        """Third priority configuration file

        :param environment:
        :return:
        """
        config_directory = '{}'.format(project_name)
        filename = '{}/{}.yml'.format(config_directory, environment)
        return os.path.join('/var/opt/sc', filename)

    @staticmethod
    def create(*, project_name, encoding='utf-8', environment=None, defaults=None):
        if defaults is None:
            defaults = {}
        # fix prefix to be SC
        prefix = "SC"
        # load defaults from defaults.py file
        config = ConfigManager(defaults=defaults, encoding=encoding)
        # load defaults from home directory
        config_file = Config._get_config_file_path(project_name, "default")
        if os.path.exists(config_file):
            logging.getLogger(__name__).info("loading default configurations from %s", config_file)
            config.set_many(ConfigManager(path=config_file, encoding=encoding).as_dict())
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

        # load environment configurations from /var/opt/sc directory
        env_config_file = Config._get_config_file_path(project_name, environment)
        if os.path.exists(env_config_file):
            logging.getLogger(__name__).info("loading environmental configurations from %s", env_config_file)
            config.set_many(ConfigManager(path=env_config_file, encoding=encoding).as_dict())

        # load environment configurations from user directory
        user_config_file = Config._get_user_dir_config_file_path(project_name, environment)
        if os.path.exists(user_config_file):
            logging.getLogger(__name__).info("loading user directory configurations from %s", user_config_file)
            config.set_many(ConfigManager(path=user_config_file, encoding=encoding).as_dict())

        # load environment configurations from current directory
        current_dir_config_file = Config._get_cur_dir_config_file_path(environment)
        if os.path.exists(current_dir_config_file):
            logging.getLogger(__name__).info("loading current directory configurations from %s", current_dir_config_file)
            config.set_many(ConfigManager(path=current_dir_config_file, encoding=encoding).as_dict())
        return config
