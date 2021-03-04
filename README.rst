.. image:: https://badge.fury.io/py/sc-config.svg
    :target: https://badge.fury.io/py/sc-config
.. image:: https://img.shields.io/pypi/pyversions/sc-config
    :alt: PyPI - Python Version


A simple Python configuration file operator
===========================================

This project provides a common way to read configurations using `config42 <https://pypi.org/project/config42/>`_.


Installation
------------

It is possible to install the tool with `pip`::

    pip install sc-config

Configuration
-------------

First, make sure /var/opt/sc directory exists, if not create this directory and make sure current user has the right
to create files in this directory.

You can copy `default.yml <https://github.com/Scott-Lau/sc-config/blob/master/scconfig/tests/sample_config/default.yml>`_
to /var/opt/sc/.<project-name>/production.yml to initialize the production configuration.

The default configuration file looks like this::

    dev:
      # whether this program is running is development mode
      dev_mode: False

Dependencies
-------------

* `config42 <https://pypi.org/project/config42/>`_ >= 0.4.4

License
-------------

The script is released under the `MIT License <https://opensource.org/licenses/MIT>`_.
The MIT License is registered with and approved by the `Open Source Initiative <https://opensource.org/>`_.