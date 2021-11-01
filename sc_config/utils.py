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

from sc_utilities import Singleton

from sc_config.config import Config


class ConfigUtils(metaclass=Singleton):
    """
    配置文件相关工具类
    """

    _config: dict = {}

    def __init__(self):
        pass

    @classmethod
    def clear(cls, project_name):
        """
        清除指定工程的配置信息
        :return:
        """
        if (project_name in cls._config.keys()):
            cls._config[project_name] = {}

    @classmethod
    def clear_all(cls):
        """
        清除所有配置信息
        :return:
        """
        cls._config.clear()

    @classmethod
    def load_configurations(cls, project_name):
        """
        加载配置文件
        :return:
        """
        try:
            # load configurations
            cls._config[project_name] = {}
            config = Config.create(project_name=project_name)
            cls._config[project_name] = config
        except Exception as error:
            cls._config[project_name] = {}
            logging.getLogger(__name__).exception(f"failed to read {project_name} configuration", exc_info=error)

    @classmethod
    def get_config(cls, project_name):
        """
        获取配置信息
        :return: 配置信息字典
        """
        if len(cls._config) == 0 or project_name not in cls._config.keys():
            cls.load_configurations(project_name)
        return cls._config[project_name]
