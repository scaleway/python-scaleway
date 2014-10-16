ocs-sdk
=======

This package provides tools to query the REST APIs of
`Online.net's cloud services`_.


Installation
------------

The package is available on pip. To install it in a virtualenv::

        virtualenv my_virtualenv
        source my_virtualenv/bin/activate
        pip install ocs-sdk


General principle
-----------------

If you're looking to send a ``GET`` HTTP request against our APIs, like::

        GET <api_url>/xxx/yyy/zzz

you only need to call the following pythonic code::

        >>> from ocs_sdk.apis import XxxAPI
        >>> XxxAPI().query().xxx.yyy.zzz.get()

The magic here lies in ``ocs_sdk.apis.*API`` instances, which all have a
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

- List your organizations::

        >>> from ocs_sdk.apis import AccountAPI
        >>>
        >>> api = AccountAPI(auth_token='') # set your token here!
        >>>
        >>> print api.query().organizations.get()
        {u'organizations': [...]}


- List your servers::

        >>> from ocs_sdk.apis import ComputeAPI
        >>>
        >>> api = ComputeAPI(auth_token='') # set your token here!
        >>>
        >>> print api.query().servers.get()
        {u'servers': [...]}


- Get details of a server::

        >>> from ocs_sdk.apis import ComputeAPI
        >>>
        >>> api = ComputeAPI(auth_token='') # set your token here!
        >>> server_id = '' # set a server id here!
        >>>
        >>> print api.query().servers(server_id).get()
        {u'server': {...}}


Using helpers:

- Check if your token has the permission ``servers:read`` for the service
  ``compute`` for the organization ``9a096d36-6bf9-470f-91df-2398aa7361f7``::

        >>> from ocs_sdk.apis import AccountAPI
        >>>
        >>> api = AccountAPI(auth_token='') # set your token here!
        >>>
        >>> print api.has_perm(service='compute', name='servers:read',
        ...     resource='9a096d36-6bf9-470f-91df-2398aa7361f7')
        False


Development
-----------

Assuming you are in a `virtualenv`_::

        $> pip install -e .
        $> python -c 'from ocs_sdk.apis import AccountAPI'
        $> # it worked!


Test
----

To submit a patch, you'll need to test your code. To run tests::

        $> pip install nose coverage pep8 pylint
        $> python setup.py nosetests --with-coverage
        ...
        $> pep8 ocs_sdk
        ...
        $> pylint ocs_sdk
        ...

* coverage score should never be lower than before your patch.
* PEP8 should never return an error.
* pylint score should never be lower than before your patch.


License
-------

This software is licensed under a `BSD 2-Clause License`_.


.. _Online.net's cloud services: https://cloud.online.net
.. _Slumber: http://slumber.readthedocs.org/
.. _API documentation: https://doc.cloud.online.net/api/
.. _virtualenv: http://virtualenv.readthedocs.org/en/latest/
.. _BSD 2-Clause License: ./LICENSE.rst
