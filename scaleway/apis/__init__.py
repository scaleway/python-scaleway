# -*- coding: utf-8 -*-
#
# Copyright (c) 2013-2016 Online SAS and Contributors. All Rights Reserved.
#                         Julien Castets <jcastets@scaleway.com>
#                         Kevin Deldycke <kdeldycke@scaleway.com>
#
# Licensed under the BSD 2-Clause License (the "License"); you may not use this
# file except in compliance with the License. You may obtain a copy of the
# License at https://opensource.org/licenses/BSD-2-Clause

from __future__ import print_function

import logging
import platform
import sys
import time

import requests
import slumber

from .. import __version__


logger = logging.getLogger(__name__)


class _CustomHTTPAdapter(requests.adapters.HTTPAdapter):
    """ In order to support SNI in Python 2.x, the packages pyOpenSSL, pyasn1
    and ndg-httpsclient need to be installed. pyOpenSSL needs the system
    packages gcc, python-dev, libffi-dev and libssl-dev to be installed.

    Because Python packaging sucks, you will succeed to install pyOpenSSL even
    if the system requirements aren't installed ; but SNI requests will fail.

    _CustomHTTPAdapter is a simple wrapper around a requests HTTPAdapter that
    logs an explicit message if a SSLError occurs, as there are good chances
    the problem comes from a bad installation.
    """
    def send(self, *args, **kwargs):  # pragma: no cover
        try:
            return super(_CustomHTTPAdapter, self).send(*args, **kwargs)
        except requests.exceptions.SSLError:
            print("SSL error is raised by python-requests. This is probably "
                  "because the required modules to handle SNI aren't "
                  "installed correctly. You should probably uninstall them "
                  "(pip uninstall pyopenssl pyasn1 ndg-httpsclient), install "
                  "the system dependencies required for their installation "
                  "(on Ubuntu, apt-get install python-dev libffi-dev "
                  "libssl-dev) and resintall them (pip install pyopenssl "
                  "pyasn1 ndg-httpsclient).", file=sys.stderr)
            raise


class SlumberResource(slumber.Resource):

    # Maximum number of times we try to make a request against an API in
    # maintenance before aborting.
    MAX_RETRIES = 3

    def retry_in(self, retry):
        """ If the API returns a maintenance HTTP status code, sleep a while
        before retrying.
        """
        return min(2 ** retry, 30)

    def _request(self, *args, **kwargs):
        """ Makes a request to the Scaleway API, and wait patiently if there is
        an ongoing maintenance.
        """
        retry = 0

        while True:
            try:
                return super(SlumberResource, self)._request(*args, **kwargs)
            except slumber.exceptions.HttpServerError as exc:
                # Not a maintenance exception
                if exc.response.status_code not in (502, 503, 504):
                    raise

                retry += 1
                retry_in = self.retry_in(retry)

                if retry >= self.MAX_RETRIES:
                    logger.error(
                        'API endpoint still in maintenance after %s attempts. '
                        'Stop trying.' % (self.MAX_RETRIES,)
                    )
                    raise

                logger.info(
                    'API endpoint is currently in maintenance. Try again in '
                    '%s seconds... (retry %s on %s)' % (
                        retry_in, retry, self.MAX_RETRIES
                    )
                )
                time.sleep(retry_in)

    def _process_response(self, resp):
        if self._store.get('serialize', True) is False:
            return resp
        return super(SlumberResource, self)._process_response(resp)


class SlumberAPI(slumber.API):

    resource_class = SlumberResource


class API(object):

    base_url = None
    user_agent = 'scw-sdk/%s Python/%s %s' % (
        __version__, ' '.join(sys.version.split()), platform.platform()
    )

    def __init__(self, auth_token=None, base_url=None, verify_ssl=True,
                 user_agent=None, auth_jwt=None):

        self.auth_token = auth_token
        self.auth_jwt = auth_jwt
        if user_agent is not None:
            self.user_agent = user_agent

        if base_url:
            self.base_url = base_url

        self.verify_ssl = verify_ssl

    def make_requests_session(self):
        """ Attaches headers needed to query Scaleway APIs.
        """
        session = requests.Session()

        session.headers.update({'User-Agent': self.user_agent})

        if self.auth_token:
            # HTTP headers must always be ISO-8859-1 encoded
            session.headers.update({
                'X-Auth-Token': self.auth_token.encode('latin1')
            })
        if self.auth_jwt:
            session.headers.update({
                'X-Session-Token': self.auth_jwt.encode('latin1')
            })
        if not self.verify_ssl:
            session.verify = False

        session.mount('https://', _CustomHTTPAdapter())

        return session

    def get_api_url(self):
        return self.base_url

    def query(self, serialize=True, **kwargs):
        """ Gets a configured slumber.API object.
        """
        api = SlumberAPI(
            self.get_api_url(),
            session=self.make_requests_session(),
            **kwargs
        )
        api._store['serialize'] = serialize
        return api


from .api_account import AccountAPI  # noqa  # isort:skip
from .api_compute import ComputeAPI  # noqa  # isort:skip
from .api_metadata import MetadataAPI  # noqa  # isort:skip
from .api_billing import BillingAPI  # noqa  # isort:skip
