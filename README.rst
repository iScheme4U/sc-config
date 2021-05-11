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

Configuration files reading in this order, the first is the top most priority:
1. production.xml in current directory,
2. production.xml in <project_name> directory under User directory,
3. production.xml in <project_name> directory under /var/opt/sc/ directory,
4. default.xml in <project_name> directory under /var/opt/sc/ directory.

Dependencies
-------------

* `config42 <https://pypi.org/project/config42/>`_ >= 0.4.4

License
-------------

The script is released under the `MIT License <https://opensource.org/licenses/MIT>`_.
The MIT License is registered with and approved by the `Open Source Initiative <https://opensource.org/>`_.