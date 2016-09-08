#!/usr/bin/env python
# coding=utf-8
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


config = {
    'description': 'My Project',
    'author': 'Jia',
    'url': 'github.com/coolmaples',
    'download_url': 'github.com/coolmaples',
    'author_email': 'jazpenn@163.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['myproject'],
    'scripts': [],
    'name': 'projectname'
}


setup(**config)
