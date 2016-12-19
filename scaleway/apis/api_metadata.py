# -*- coding: utf-8 -*-
#
# Copyright (c) 2013-2016 Online SAS and Contributors. All Rights Reserved.
#                         Julien Castets <jcastets@scaleway.com>
#
# Licensed under the BSD 2-Clause License (the "License"); you may not use this
# file except in compliance with the License. You may obtain a copy of the
# License at https://opensource.org/licenses/BSD-2-Clause

from . import API


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
