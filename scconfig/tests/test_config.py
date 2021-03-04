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

import os
import shutil
import unittest

from scconfig.config import Config
from .sample_config.default import DEFAULT_CONFIG


class ConfigTestCase(unittest.TestCase):

    def test_create_config(self):
        config = Config.create(project_name="sc-config")
        self.assertIsNotNone(config)
        environment = config.get("environment")

        self.assertEqual(environment, 'production')

    def test_create_config_with_defaults(self):
        config = Config.create(project_name="sc-config", defaults=DEFAULT_CONFIG)
        self.assertIsNotNone(config)
        environment = config.get("environment")

        self.assertEqual(environment, 'production')
        self.assertEqual(config.get("dev.dev_mode"), True)

    def test_create_config_from_project_file(self):
        project_name = "sc-config"
        config_directory = '.{}'.format(project_name)
        directory = os.path.join(os.path.expanduser('~'), config_directory)
        if not os.path.exists(directory):
            os.makedirs(directory)

        with open("tests/sample_config/development.yml", "r") as reader:
            dev_file_content = reader.readlines()
        filename = Config._get_config_file_path(project_name, "development")
        with open(filename, "w+") as writer:
            writer.writelines(dev_file_content)

        config = Config.create(project_name=project_name, environment="development")
        self.assertIsNotNone(config)
        environment = config.get("environment")

        self.assertEqual(environment, 'development')
        self.assertEqual(config.get("dev.dev_mode"), True)

        try:
            shutil.rmtree(directory)
        except OSError as e:
            print("failed to delete directory: %s : %s" % (directory, e.strerror))


if __name__ == '__main__':
    unittest.main()
