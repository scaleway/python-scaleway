#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2013-2014 Online SAS and Contributors. All Rights Reserved.
#                         Julien Castets <jcastets@scaleway.com>
#                         Kevin Deldycke <kdeldycke@scaleway.com>
#
# Licensed under the BSD 2-Clause License (the "License"); you may not use this
# file except in compliance with the License. You may obtain a copy of the
# License at http://opensource.org/licenses/BSD-2-Clause

import os
import re

from setuptools import setup, find_packages


MODULE_NAME = 'scaleway'


def get_version():

    with open(os.path.join(
        os.path.dirname(__file__), MODULE_NAME, '__init__.py')
    ) as init:

        for line in init.readlines():
            res = re.match(r'__version__ *= *[\'"]([0-9\.]*)[\'"]$', line)
            if res:
                return res.group(1)


def get_long_description():
    readme = os.path.join(os.path.dirname(__file__), 'README.rst')
    changes = os.path.join(os.path.dirname(__file__), 'CHANGES.rst')
    return open(readme).read() + '\n' + open(changes).read()


setup(
    name='scaleway-sdk',
    version=get_version(),
    description="Tools to query the REST APIs of Scaleway",
    long_description=get_long_description(),

    author='Scaleway',
    author_email='opensource@scaleway.com',
    url='https://github.com/scaleway/python-scaleway',
    license='BSD',

    install_requires=[
        'slumber >= 0.6.0',

        'pyOpenSSL',
        'ndg-httpsclient',
        'pyasn1',
    ],

    packages=find_packages(),

    tests_require=[
        'httpretty >= 0.8.0',
    ],
    test_suite=MODULE_NAME + '.tests',

    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Internet',
        'Topic :: System :: Distributed Computing',
    ],

    entry_points={
        'console_scripts': [
        ]
    }
)
