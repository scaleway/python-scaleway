ChangeLog
=========

`1.9.0 (2019-07-03) <https://github.com/scaleway/python-scaleway/compare/v1.8.1...v1.9.0>`_
--------------------------------------------------------------------------------------------

* Add support for unlimited quotas

`1.8.1 (2019-06-18) <https://github.com/scaleway/python-scaleway/compare/v1.8.0...v1.8.1>`_
--------------------------------------------------------------------------------------------

* Call api-account with query params in ``get_resources`` function

`1.8.0 (2019-01-28) <https://github.com/scaleway/python-scaleway/compare/v1.7.0...v1.8.0>`_
--------------------------------------------------------------------------------------------

* Target tests on Python 3.7 and 3.8-dev.
* Remove Python 3.3 support.
* In AccountAPI.get_quotas(), request more than the default 50 lines, quick fix of CP-1660


`1.7.0 (2018-12-14) <https://github.com/scaleway/python-scaleway/compare/v1.6.0...v1.7.0>`_
--------------------------------------------------------------------------------------------

* Add jwt support in api-account


`1.6.0 (2018-06-20) <https://github.com/scaleway/python-scaleway/compare/v1.5.0...v1.6.0>`_
--------------------------------------------------------------------------------------------

* Add ``scaleway.apis.BillingAPI``.
* Add MAINTAINERS.md file.


`1.5.0 (2016-12-19) <https://github.com/scaleway/python-scaleway/compare/v1.4.1...v1.5.0>`_
-------------------------------------------------------------------------------------------

* Add default ``isort`` config.
* Activate tests on Python 3.3, 3.5, 3.6-dev, 3.7-dev, PyPy2 and PyPy3.
* Remove popularity badge: PyPI download counters are broken and no longer
  displayed.
* Move ``coverage`` config to ``setup.cfg``.
* Add ``test`` and ``develop`` dependencies.
* Only show latest changes in the long description of the package instead of
  the full changelog.
* Add default PyLint config.
* Add default ``pycodestyle`` config.
* Enforce ``pycodestyle`` checks in Travis CI jobs.
* Test production of packages in Travis CI jobs.
* Always check for package metadata in Travis CI jobs.
* Make wheels generated under Python 2 environnment available for Python 3 too.
* Add link to full changelog in package's long description.


`1.4.1 (2016-10-31) <https://github.com/scaleway/python-scaleway/compare/v1.4.0...v1.4.1>`_
-------------------------------------------------------------------------------------------

* Fix ``ComputeAPI`` when ``base_url`` is providen explicitely.


`1.4.0 (2016-10-28) <https://github.com/scaleway/python-scaleway/compare/v1.3.0...v1.4.0>`_
-------------------------------------------------------------------------------------------

* Accept ``region`` argument in the constructor of ``ComputeAPI``.


`1.3.0 (2016-08-30) <https://github.com/scaleway/python-scaleway/compare/v1.2.0...v1.3.0>`_
-------------------------------------------------------------------------------------------

* ``query()`` accepts the argument ``serialize``. If ``False`` (default is
  ``True``), a ``flask.Response`` object is returned instead of a ``dict``. It
  can be used to get response HTTP headers.


`1.2.0 (2016-08-16) <https://github.com/scaleway/python-scaleway/compare/v1.1.4...v1.2.0>`_
-------------------------------------------------------------------------------------------

* Forward ``api.query()`` ``kwargs`` to the ``slumber.API`` object. It is now
  possible to override the ``append_slash`` behaviour with
  ``api.query(append_slash=False)``.


`1.1.4 (2016-05-31) <https://github.com/scaleway/python-scaleway/compare/v1.1.3...v1.1.4>`_
-------------------------------------------------------------------------------------------

* Really, do not flood the APIs in case of maintenance. Reduce number of
  retries from 10 to 3.


`1.1.3 (2016-03-29) <https://github.com/scaleway/python-scaleway/compare/v1.1.2...v1.1.3>`_
-------------------------------------------------------------------------------------------

* Do not flood the APIs in case of maintenance.


`1.1.2 (2015-11-23) <https://github.com/scaleway/python-scaleway/compare/v1.1.1...v1.1.2>`_
-------------------------------------------------------------------------------------------

* Add bumpversion config.
* Fix readme rendering.


`1.1.1 (2015-11-23) <https://github.com/scaleway/python-scaleway/compare/v1.1.0...v1.1.1>`_
-------------------------------------------------------------------------------------------

* Switch from ``coveralls.io`` to ``codecov.io``.


`1.1.0 (2015-10-13) <https://github.com/scaleway/python-scaleway/compare/v1.0.2...v1.1.0>`_
-------------------------------------------------------------------------------------------

* Add Python3 support (#4).
* Add an explicit error message when SNI fails (#8).
* In an API endpoint is in maintenance (ie. it returns ``HTTP/503``), keep
  trying to make requests for 180 seconds.


`1.0.2 (2015-04-07) <https://github.com/scaleway/python-scaleway/compare/v1.0.0...v1.0.2>`_
-------------------------------------------------------------------------------------------

* Fix Pypi mess.


`1.0.0 (2015-04-07) <https://github.com/scaleway/python-scaleway/compare/v0.4.2...v1.0.0>`_
-------------------------------------------------------------------------------------------

* Rename OCS to Scaleway. ``import ocs`` becomes ``import scaleway``.


`0.4.2 (2015-04-02) <https://github.com/scaleway/python-scaleway/compare/v0.4.1...v0.4.2>`_
-------------------------------------------------------------------------------------------

* Install packages to have TLS SNI support.


`0.4.1 (2015-04-02) <https://github.com/scaleway/python-scaleway/compare/v0.4.0...v0.4.1>`_
-------------------------------------------------------------------------------------------

* Update APIs URLs from ``cloud.online.net`` to ``scaleway.com``.


`0.4.0 (2015-03-11) <https://github.com/scaleway/python-scaleway/compare/v0.3.2...v0.4.0>`_
-------------------------------------------------------------------------------------------

* Add param ``include_locked`` to ``AccountAPI.get_resources()``. Useful if you
  need to list all the permissions of a token, even if the owner's organization
  is locked.
* ``AccountAPI.has_perm()`` also accepts the param ``include_locked``.


`0.3.2 (2015-01-08) <https://github.com/scaleway/python-scaleway/compare/v0.3.1...v0.3.2>`_
-------------------------------------------------------------------------------------------

* Raise ``BadToken`` if account API returns ``HTTP/400``.


`0.3.1 (2014-12-19) <https://github.com/scaleway/python-scaleway/compare/v0.3.0...v0.3.1>`_
-------------------------------------------------------------------------------------------

* ``ocs_sdk.apis.API`` accepts the constructor param ``user_agent``. Defaults
  to ``ocs-sdk Pythons/version Platform``.
* Check code coverage thanks to coveralls.


`0.3.0 (2014-11-12) <https://github.com/scaleway/python-scaleway/compare/v0.2.1...v0.3.0>`_
-------------------------------------------------------------------------------------------

* Add missing license files. Closes #1.
* Create class ``MetadataAPI`` to get metadata of a running server.


`0.2.1 (2014-10-14) <https://github.com/scaleway/python-scaleway/compare/v0.2.0...v0.2.1>`_
-------------------------------------------------------------------------------------------

* Add documentation.
* Set production URLs as defaults in ``AccountAPI`` and ``ComputeAPI``.


`0.2.0 (2014-04-16) <https://github.com/scaleway/python-scaleway/compare/v0.1.3...v0.2.0>`_
-------------------------------------------------------------------------------------------

* Added quota methods (``has_quota``, ``get_quotas``) & their tests.
  Refs: AM-1, AM-11.


`0.1.3 (2014-03-07) <https://github.com/scaleway/python-scaleway/compare/v0.1.2...v0.1.3>`_
-------------------------------------------------------------------------------------------

* Minor changes in ``AccountAPI.perm_matches`` (67f967d26d3).
* ``base_url`` can be given to the constructor of ``API()``.
* ``verify_ssl`` can be given to the constructor of ``API()``.


`0.1.2 (2014-02-28) <https://github.com/scaleway/python-scaleway/compare/v0.1.1...v0.1.2>`_
-------------------------------------------------------------------------------------------

* Raise ``InvalidToken`` when ``get_resources`` is called with and invalid
  token.


`0.1.1 (2014-02-28) <https://github.com/scaleway/python-scaleway/compare/v0.1.0...v0.1.1>`_
-------------------------------------------------------------------------------------------

* Add missing files in source tarball.


`0.1.0 (2014-02-28) <https://github.com/scaleway/python-scaleway/compare/98f429...v0.1.0>`_
-------------------------------------------------------------------------------------------

* Initial release.


`0.0.0 (2013-06-24) <https://github.com/scaleway/python-scaleway/commit/98f429>`_
---------------------------------------------------------------------------------

* First commit.
