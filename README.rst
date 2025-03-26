.. image:: https://badge.fury.io/py/sc-config.svg
    :target: https://badge.fury.io/py/sc-config
.. image:: https://img.shields.io/pypi/pyversions/sc-config
    :alt: PyPI - Python Version


A simple Python configuration file operator
===========================================

This project provides a common way to read configurations.


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

* Pyyaml >= 5.1
* Jinja2 >= 2.0
* Cerberus >= 1.3.1
* MarkupSafe>=3.0.2

License
-------------

The script is released under the `MIT License <https://opensource.org/licenses/MIT>`_.
The MIT License is registered with and approved by the `Open Source Initiative <https://opensource.org/>`_.