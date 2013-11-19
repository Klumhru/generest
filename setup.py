#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Mimir runtime application
=======

This is the Mimir main application runtime. Call mimir <action> [options] to
run the various application components
"""
from __future__ import unicode_literals, print_function, absolute_import

from setuptools import setup, find_packages

requires = [
    'jinja2',
    'django',
]

setup(
    name='generest',
    version='0.1.1',
    packages=find_packages(),
    author="Högni Gylfason",
    author_email="hognig@vis.is",
    install_requires=requires,
    description=__doc__,
    include_package_data=True,
    classifiers=[
        "Development Status :: 5 - Alpha",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
    ],
    zip_safe=True,
)
