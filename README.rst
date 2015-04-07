Scaleway SDK
============

This package provides tools to query the REST APIs of `Scaleway`_.

.. image:: https://img.shields.io/pypi/v/scaleway-sdk.svg?style=flat
    :target: https://pypi.python.org/pypi/scaleway-sdk
    :alt: Last release
.. image:: https://img.shields.io/travis/scaleway/python-scaleway/develop.svg?style=flat
    :target: https://travis-ci.org/scaleway/python-scaleway
    :alt: Unit-tests status
.. image:: https://img.shields.io/coveralls/scaleway/python-scaleway/develop.svg?style=flat
    :target: https://coveralls.io/r/scaleway/python-scaleway?branch=develop
    :alt: Coverage Status
.. image:: https://img.shields.io/requires/github/scaleway/python-scaleway/master.svg?style=flat
    :target: https://requires.io/github/scaleway/python-scaleway/requirements/?branch=master
    :alt: Requirements freshness
.. image:: https://img.shields.io/pypi/l/scaleway-sdk.svg?style=flat
    :target: http://opensource.org/licenses/BSD-2-Clause
    :alt: Software license
.. image:: https://img.shields.io/pypi/dm/scaleway-sdk.svg?style=flat
    :target: https://pypi.python.org/pypi/scaleway-sdk#downloads
    :alt: Popularity


Installation
------------

The package is available on pip. To install it in a virtualenv:

.. code-block:: bash

    virtualenv my_virtualenv
    source my_virtualenv/bin/activate
    pip install scaleway-sdk


General principle
-----------------

If you're looking to send a ``GET`` HTTP request against our APIs, like:

.. code-block:: http

    GET <api_url>/foo/bar

you only need to call the following pythonic code:

.. code-block:: python

    >>> from scaleway.apis import DummyAPI
    >>> DummyAPI().query().foo.bar.get()

The magic here lies in ``scaleway.apis.*API`` instances, which all have a
``query`` method returning a ``slumber.API`` object. The latter handling all
the excruciating details of the requests.


Documentation
-------------

Even if this SDK is designed to be developer-friendly and aim for self-service
discovery, it is still recommended to read the official `API documentation`_.

And because most of the provided helpers takes the form of pre-configured
Slumber_ objects, a good read of Slumber_ documention is encouraged as well.


Examples
--------

- List your organizations:

.. code-block:: python

    >>> from scaleway.apis import AccountAPI
    >>> api = AccountAPI(auth_token='')  # Set your token here!
    >>> print api.query().organizations.get()
    {u'organizations': [...]}


- List your servers:

.. code-block:: python

    >>> from scaleway.apis import ComputeAPI
    >>> api = ComputeAPI(auth_token='')  # Set your token here!
    >>> print api.query().servers.get()
    {u'servers': [...]}


- Get details of a server:

.. code-block:: python

    >>> from scaleway.apis import ComputeAPI
    >>> api = ComputeAPI(auth_token='')  # Set your token here!
    >>> server_id = ''  # Set a server ID here!
    >>> print api.query().servers(server_id).get()
    {u'server': {...}}


- Check if your token has the permission ``servers:read`` for the service
  ``compute`` for the organization ``9a096d36-6bf9-470f-91df-2398aa7361f7``:

.. code-block:: python

    >>> from scaleway.apis import AccountAPI
    >>> api = AccountAPI(auth_token='')  # Set your token here!
    >>> print api.has_perm(service='compute', name='servers:read',
    ...     resource='9a096d36-6bf9-470f-91df-2398aa7361f7')
    False


Development
-----------

Assuming you are in a `virtualenv`_:

.. code-block:: bash

    pip install -e .
    python -c 'from scaleway.apis import AccountAPI'
    # it works!


Test
----

To submit a patch, you'll need to test your code. To run tests:

.. code-block:: bash

    pip install nose coverage pep8 pylint
    python setup.py nosetests --with-coverage
    # (...)
    pep8 scaleway
    # (...)
    pylint scaleway
    # (...)

* coverage score should never be lower than before your patch.
* PEP8 should never return an error.
* pylint score should never be lower than before your patch.


Alternative libraries / clients
-------------------------------

- Ruby

  - API client: https://github.com/bchatelard/onlinelabs-ruby

- Golang

  - Go library + CLI: https://github.com/lalyos/onlabs (@lalyos)
  - Vagrant packer + API client: https://github.com/meatballhat/packer-builder-onlinelabs/ (@meatballhat)
  - Go CLI: https://github.com/nlamirault/go-scaleway (@nlamirault)

- Node.js/javascript

  - Docker-like CLI: https://github.com/moul/scaleway-cli (@moul)
  - Node.js + browser client: https://github.com/moul/node-scaleway (@moul)
  - Cloudformation plugin, with API client: https://github.com/resin-io/onlinelabs-cloudformation (@resin.io)

- Python

  - Juju plugin + with API client: https://github.com/online-labs/juju-onlinelabs
  - API client: https://github.com/adebarbara/olpy (@adebarbara)



License
-------

This software is licensed under a `BSD 2-Clause License`_.


.. _Scaleway: https://www.scaleway.com/
.. _Slumber: http://slumber.readthedocs.org/
.. _API documentation: https://www.scaleway.com/docs/
.. _virtualenv: http://virtualenv.readthedocs.org/en/latest/
.. _BSD 2-Clause License: https://github.com/scaleway/python-scaleway/blob/develop/LICENSE.rst
