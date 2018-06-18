Scaleway SDK
============

Python SDK to query `Scaleway <https://scaleway.com>`_'s `APIs
<https://developer.scaleway.com>`_.

Stable release: |release| |versions| |license| |dependencies|

Development: |build| |coverage| |quality|

.. |release| image:: https://img.shields.io/pypi/v/scaleway-sdk.svg
    :target: https://pypi.python.org/pypi/scaleway-sdk
    :alt: Last release
.. |versions| image:: https://img.shields.io/pypi/pyversions/scaleway-sdk.svg
    :target: https://pypi.python.org/pypi/scaleway-sdk
    :alt: Python versions
.. |license| image:: https://img.shields.io/pypi/l/scaleway-sdk.svg
    :target: https://opensource.org/licenses/BSD-2-Clause
    :alt: Software license
.. |dependencies| image:: https://requires.io/github/scaleway/python-scaleway/requirements.svg?branch=master
    :target: https://requires.io/github/scaleway/python-scaleway/requirements/?branch=master
    :alt: Requirements freshness
.. |build| image:: https://travis-ci.org/scaleway/python-scaleway.svg?branch=develop
    :target: https://travis-ci.org/scaleway/python-scaleway
    :alt: Unit-tests status
.. |coverage| image:: https://codecov.io/gh/scaleway/python-scaleway/branch/develop/graph/badge.svg
    :target: https://codecov.io/github/scaleway/python-scaleway?branch=develop
    :alt: Coverage Status
.. |quality| image:: https://scrutinizer-ci.com/g/scaleway/python-scaleway/badges/quality-score.png?b=develop
    :target: https://scrutinizer-ci.com/g/scaleway/python-scaleway/?branch=develop
    :alt: Code Quality


Installation
------------

The package is available on ``pip``. To install it in a virtualenv:

.. code-block:: bash

    $ virtualenv my_virtualenv
    $ source my_virtualenv/bin/activate
    $ pip install scaleway-sdk


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
discovery, it is still recommended to read the official `API documentation
<https://scaleway.com/docs/>`_.

And because most of the provided helpers takes the form of pre-configured
``Slumber`` objects, a good read of `Slumber <https://slumber.readthedocs.org>`_
documention is encouraged as well.

The list of available resources per API can be found [on the Scaleway API repository](https://github.com/scaleway/api.scaleway.com/blob/master/README.md#apis)


Examples
--------

- List your organizations:

.. code-block:: python

    >>> from scaleway.apis import AccountAPI
    >>> api = AccountAPI(auth_token='')  # Set your token here!
    >>> print api.query().organizations.get()
    {u'organizations': [...]}


- List your organizations, but get a `flask.Response` object instead of a
  `dict`:

.. code-block:: python

    >>> from scaleway.apis import AccountAPI
    >>> api = AccountAPI(auth_token='')  # Set your token here!
    >>> resp = api.query(serialize=False).organizations.get()
    >>> print type(resp)
    <Response [200]>
    >>> print resp.headers
    {...}  # Response HTTP headers.
    >>> print resp.links
    {...}  # Parsed "Link" HTTP header, for pagination.
    >>> print resp.json()
    {u'organizations': [...]}


- List your servers:

.. code-block:: python

    >>> from scaleway.apis import ComputeAPI
    >>> api = ComputeAPI(auth_token='')  # Set your token here!
    >>> print api.query().servers.get()
    {u'servers': [...]}
    # Or choose your region, as in apis/api_compute.py
    >>> api = ComputeAPI(region='ams1', auth_token='')  # Set your token here!
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

Assuming you are in a `virtualenv <https://virtualenv.readthedocs.org>`_:

.. code-block:: bash

    $ pip install -e .
    $ python -c 'from scaleway.apis import AccountAPI'
      # it works!


Test
----

To submit a patch, you'll need to test your code against python2.7 and
python3.4. To run tests:

.. code-block:: bash

    $ pip install nose coverage pycodestyle pylint
    $ python setup.py nosetests --with-coverage
      (...)
    $ pycodestyle scaleway
      (...)
    $ pylint scaleway
      (...)

* Coverage score should never be lower than before your patch.
* PEP8 should never return an error.
* Pylint score should never be lower than before your patch.

Alternatively, to run `nosetests` on both Python2.7 and Python3.4, you can run
`tox`.


Alternative libraries / clients
-------------------------------

We maintain a list of the current library/client implementations on the
`api.scaleway.com repository
<https://github.com/scaleway/api.scaleway.com/blob/master/README.md#clients--libraries>`_.

License
-------

This software is licensed under a `BSD 2-Clause License
<https://github.com/scaleway/python-scaleway/blob/develop/LICENSE>`_.
