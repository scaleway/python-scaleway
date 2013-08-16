# -*- coding: utf-8 -*-

import requests

class ApiClient(object):
    def __init__(self, access_key, secret_key, endpoint='localhost:5002', endpoint_ssl=False, region='dev'):
        self.access_key = access_key
        self.secret_key = secret_key
        self.endpoint = endpoint
        self.endpoint_ssl = endpoint_ssl
        self.region = region
        self.connect()

    def connect(self):
        print('connected')
        return self

    def _request(self, path, method='GET'):
        url = '%s://%s/%s' % ('http', self.endpoint, path)
        r = requests.request(method, url)
        print(url)
        return r.json()

    def get_all_servers(self):
        return self._request('servers')
