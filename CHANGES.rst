ChangeLog
=========

1.4.0 (2016-10-28)
------------------

* Accept "region" argument in the constructor of ComputeAPI.

1.3.0 (2016-08-30)
------------------

* query() accepts the argument serialize. If False (default is True), a
  flask.Response object is returned instead of a dict. It can be used to get
  response HTTP headers.

1.2.0 (2016-08-16)
------------------

* Forward api.query() kwargs to the slumber.API object. It is now possible to
  override the append_slash behaviour with `api.query(append_slash=False)`.

1.1.4 (2016-05-31)
------------------

* Really, do not flood the APIs in case of maintenance. Reduce number of
  retries from 10 to 3.

1.1.3 (2016-03-29)
------------------

* Do not flood the APIs in case of maintenance.

1.1.2 (2015-11-23)
------------------

* Add bumpversion config.
* Fix readme rendering.

1.1.1 (2015-11-23)
------------------

* Switch from coveralls.io to codecov.io.

1.1.0 (2015-10-13)
------------------

* Add Python3 support (#4).
* Add an explicit error message when SNI fails (#8).
* In an API endpoint is in maintenance (ie. it returns HTTP/503), keep trying
  to make requests for 180 seconds.

1.0.2 (2015-04-07)
------------------

* Fix Pypi mess.

1.0.0 (2015-04-07)
------------------

* Rename OCS to Scaleway. ``import ocs`` becomes ``import scaleway``.

0.4.2 (2015-04-02)
------------------

* Install packages to have TLS SNI support.

0.4.1 (2015-04-02)
------------------

* Update APIs URLs from ``cloud.online.net`` to ``scaleway.com``.

0.4.0 (2015-03-11)
------------------

* Add param ``include_locked`` to ``AccountAPI.get_resources()``. Useful if you
  need to list all the permissions of a token, even if the owner's organization
  is locked.
* ``AccountAPI.has_perm()`` also accepts the param ``include_locked``.

0.3.2 (2015-01-08)
------------------

* Raise ``BadToken`` if account API returns ``HTTP/400``.

0.3.1 (2014-12-19)
------------------

* ``ocs_sdk.apis.API`` accepts the constructor param ``user_agent``. Defaults
  to ``ocs-sdk Pythons/version Platform``.
* Check code coverage thanks to coveralls.

0.3.0 (2014-11-12)
------------------

* Add missing license files. Closes #1.
* Create class ``MetadataAPI`` to get metadata of a running server.

0.2.1 (2014-10-14)
------------------

* Add documentation.
* Set production URLs as defaults in ``AccountAPI`` and ``ComputeAPI``.

0.2.0 (2014-04-16)
------------------

* Added quota methods (``has_quota``, ``get_quotas``) & their tests.
  Refs: AM-1, AM-11.

0.1.3 (2014-03-07)
------------------

* Minor changes in ``AccountAPI.perm_matches`` (67f967d26d3).
* ``base_url`` can be given to the constructor of ``API()``.
* ``verify_ssl`` can be given to the constructor of ``API()``.

0.1.2 (2014-02-28)
------------------

* Raise ``InvalidToken`` when ``get_resources`` is called with and invalid
  token.

0.1.1 (2014-02-28)
------------------

* Add missing files in source tarball.

0.1.0 (2014-02-28)
------------------

* Initial release.

0.0.0 (2013-06-24)
------------------

* First commit.
