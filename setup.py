#!/usr/bin/env python

import imp
import os
import re

from setuptools import setup, find_packages


MODULE_NAME = 'ocs_sdk'


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
    name='ocs-sdk',
    version=get_version(),
    description='OCS APIs client',
    long_description=get_long_description(),

    author='OCS',
    author_email='contact@ocs.online.net',
    url='http://online.net',

    install_requires=[
        'slumber >=0.6.0',
    ],

    packages=find_packages(),

    tests_require=[
        'httpretty >=0.8.0',
    ],
    test_suite=MODULE_NAME + '.tests',

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: Other/Proprietary License',
        'Operating System :: POSIX',
        'Operating System :: MacOS',
        'Operating System :: Unix',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Internet',
        'Topic :: System :: Distributed Computing',
    ],

    entry_points={
        'console_scripts': [
        ]
    }
)
