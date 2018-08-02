# -*- coding: utf-8 -*-
#
# Copyright (c) 2013-2016 Online SAS and Contributors. All Rights Reserved.
#                         Julien Castets <jcastets@scaleway.com>
#
# Licensed under the BSD 2-Clause License (the "License"); you may not use this
# file except in compliance with the License. You may obtain a copy of the
# License at https://opensource.org/licenses/BSD-2-Clause

import json
import random

import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.poolmanager import PoolManager

from . import API


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


class MetadataAPI(API):
    """ The metadata API is used to get info about a running instance.

    To authenticate the client, the API uses its IP address. The header
    X-Auth-Token is not needed.
    """

    base_url = 'http://169.254.42.42/'

    def __init__(self, **kwargs):

        assert 'auth_token' not in kwargs, \
            'auth_token is not required to query the metadata API'

        super(MetadataAPI, self).__init__(auth_token=None, **kwargs)

    def get_metadata(self, as_shell=False):
        """ Returns server metadata.

        If `as_shell` is True, return a string easily parsable by a shell. If
        False, return a dictionary.
        """
        if as_shell:
            return self.query().conf.get()
        return self.query().conf.get(format='json')

    def get_userdata(self, key=None, as_shell=False):
        """ Returns server userdata.

        If a key is specified, the value of the specified key is returned
        If no key is specified, return a dictionary

        If `as_shell` is True, return a string easily parsable by a shell. If
        False, return a dictionary.
        """
        with requests.Session() as s:
            s.mount('http://', SourcePortAdapter(random.randrange(1, 1024)))

            if key:
                return self._get_userdata(key)

            user_keys = s.get(
                '%s/user_data?format=json' %
                self.base_url).json().get('user_data')
            if as_shell:
                return self._get_shell_userdata(user_keys)
            return self._get_json_userdata(user_keys)

    def _get_userdata(self, key):
        with requests.Session() as s:
            s.mount('http://', SourcePortAdapter(random.randrange(1, 1024)))
            return s.get('%s/user_data/%s' % (self.base_url, key)).text

    def _get_json_userdata(self, user_keys):
        result = {}
        for key in user_keys:
            result[key] = self._get_userdata(key)

        return json.dumps(result)

    def _get_shell_userdata(self, user_keys):
        result = []
        for key in user_keys:
            result.append("%s=%s" % (str(key), self._get_userdata(key)))

        return "\n".join(result)
