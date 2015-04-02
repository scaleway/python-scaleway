# -*- coding: utf-8 -*-
#
# Copyright (c) 2013-2014 Online SAS and Contributors. All Rights Reserved.
#                         Julien Castets <jcastets@scaleway.com>
#                         Kevin Deldycke <kdeldycke@scaleway.com>
#
# Licensed under the BSD 2-Clause License (the "License"); you may not use this
# file except in compliance with the License. You may obtain a copy of the
# License at http://opensource.org/licenses/BSD-2-Clause

import platform
import sys

import requests
import slumber

from .. import __version__


class API(object):

    base_url = None
    user_agent = 'scw-sdk/%s Python/%s %s' % (
        __version__, ' '.join(sys.version.split()), platform.platform()
    )

    def __init__(self, auth_token=None, base_url=None, verify_ssl=True,
                 user_agent=None):

        self.auth_token = auth_token

        if user_agent is not None:
            self.user_agent = user_agent

        if base_url:
            self.base_url = base_url

        self.verify_ssl = verify_ssl

    def make_requests_session(self):
        """ Attaches headers needed to query OCS APIs.
        """
        session = requests.Session()

        session.headers.update({'User-Agent': self.user_agent})

        if self.auth_token:
            # HTTP headers must always be ISO-8859-1 encoded
            session.headers.update({
                'X-Auth-Token': self.auth_token.encode('latin1')
            })

        if not self.verify_ssl:
            session.verify = False

        return session

    def get_api_url(self):
        return self.base_url

    def query(self):
        """ Gets a configured slumber.API object.
        """
        return slumber.API(
            self.get_api_url(),
            session=self.make_requests_session()
        )


from .api_account import AccountAPI
from .api_compute import ComputeAPI
from .api_metadata import MetadataAPI
