ocs-sdk
=======

ocs-sdk provides configured Slumber_ objects to make HTTP requests easily
against the REST APIs of the `Online.net Cloud service`_. It also provides
helpers to render APIs results under a more usable form.

First of all, it is recommended to read the `API documentation`_. You probably
need to give a look to the Slumber_ documentation, too.


Examples
--------

Instances of `ocs_sdk.apis.API` define a `query` method that returns a
`slumber.API` object. `API.query().xxx.yyy.zzz.get()` generates a *GET
API_URL/xxx/yyy/zzz*.


Examples, using `Slumber`_:

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

- Check if your token has the permission "servers:read" for the service
  "compute" for the organization "9a096d36-6bf9-470f-91df-2398aa7361f7"::

        >>> from ocs_sdk.apis import AccountAPI
        >>>
        >>> api = AccountAPI(auth_token='') # set your token here!
        >>>
        >>> print api.has_perm(service='compute', name='servers:read',
        ...  resource='9a096d36-6bf9-470f-91df-2398aa7361f7')
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


.. _Online.net Cloud service: https://cloud.online.net
.. _Slumber: http://slumber.readthedocs.org/
.. _API documentation: https://doc.cloud.online.net/api/
.. _virtualenv: http://virtualenv.readthedocs.org/en/latest/
