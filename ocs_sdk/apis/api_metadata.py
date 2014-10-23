# -*- coding: utf-8 -*-

from . import API


class MetadataAPI(API):
    """ The metadata API is used to get info about a running instance.

    To authenticate the client, the API uses its IP address. The header
    X-Auth-Token is not needed.
    """

    base_url = 'http://169.254.42.42/'

    def __init__(self, base_url=None, verify_ssl=False):
        super(MetadataAPI, self).__init__(
            auth_token=None, base_url=base_url, verify_ssl=verify_ssl
        )

    def get(self, as_shell=False):
        """ Returns server metadata.

        If `as_shell` is True, return a string easily parsable by a shell. If
        False, return a dictionary.
        """
        if as_shell:
            return self.query().conf.get()
        return self.query().conf.get(format='json')
