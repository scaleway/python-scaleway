#!/usr/bin/env python

import imp
import os

from setuptools import setup, find_packages


MODULE_NAME = 'ocs_sdk'
MODULE = imp.load_module(MODULE_NAME, *imp.find_module(MODULE_NAME))


def get_long_description():
    readme = os.path.join(os.path.dirname(__file__), 'README.rst')
    return open(readme).read()


setup(
    name='ocs-sdk',
    version=MODULE.__version__,
    description='OCS APIs client',
    long_description=get_long_description(),

    author='OCS',
    author_email='contact@ocs.online.net',
    url='http://online.net',

    install_requires=[
        'slumber >=0.6.0',
    ],

    packages=find_packages(),

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
