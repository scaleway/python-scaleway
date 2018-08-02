# -*- coding: utf-8 -*-
#
# Copyright (c) 2013-2018 Online SAS and Contributors. All Rights Reserved.
#                         Antoine Barbare <abarbare@scaleway.com>
#
# Licensed under the BSD 2-Clause License (the "License"); you may not use this
# file except in compliance with the License. You may obtain a copy of the
# License at https://opensource.org/licenses/BSD-2-Clause

from . import API
import requests
import random
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.poolmanager import PoolManager

class SourcePortAdapter(HTTPAdapter):
    """" Transport adapter that allows us to set a custom source port.
    """

    def __init__(self, port, *args, **kwargs):
        self._source_port = port
        super(SourcePortAdapter, self).__init__(*args, **kwargs)

    def init_poolmanager(self, connections, maxsize, block=False):
        self.poolmanager = PoolManager(
            num_pools=connections,
            maxsize=maxsize,
            block=block,
            source_address=("", self._source_port),
        )

class UserDataAPI(API):
    """ The user_data API is used to get user custom variable on a running instance.

    To authenticate the client, the API uses its IP address. The header
    X-Auth-Token is not needed.
    """

    base_url = 'http://169.254.42.42/'

    def __init__(self, **kwargs):

        assert 'auth_token' not in kwargs, \
            'auth_token is not required to query the metadata API'

        super(UserDataAPI, self).__init__(auth_token=None, **kwargs)

    def get_userdata(self, as_shell=False):
        """ Returns server userdata.

        If `as_shell` is True, return a string easily parsable by a shell. If
        False, return a dictionary.
        """
        with requests.Session() as s:
            s.mount('http://', SourcePortAdapter(random.randrange(1, 1024)))

            if as_shell:
                return s.get('%s/user_data' % self.base_url).text
            return s.get('%s/user_data?format=json' % self.base_url).text
