# -*- coding: utf-8 -*-

from __future__ import print_function

import time
import requests
import json
import sys


class ApiClient(object):
    def __init__(self, access_key, secret_key, endpoint='localhost:5002',
                 endpoint_ssl=False, region='dev', debug=False):
        self.access_key = access_key
        self.secret_key = 'b080a512-8847-4f74-81df-b3c8071d45f4'
        self.endpoint = endpoint
        self.endpoint_ssl = endpoint_ssl
        self.region = region
        self.debug = debug
        self.connect()

    def connect(self):
        if self.debug:
            print('connected')
        return self

    def request(self, path, method='GET', params=None, data=None,
                blocking=False):
        path = path.lstrip('/')
        url = '%s://%s/%s' % ('http', self.endpoint, path)
        if self.debug:
            print('\n%-6s %s data=%s' % (method, url, data))
        headers = {}
        headers['x-auth-token'] = self.secret_key

        sys.stdout.write('.')
        sys.stdout.flush()
        if data:
            data = json.dumps(data)
            headers['content-type'] = 'application/json'
        r = requests.request(method, url, params=params, data=data,
                             headers=headers)
        if r.status_code in (500, 405):
            print(r.text)
            return False
        if blocking:
            if self.debug:
                print(r.json())
            res = self.wait_for_task(r.json()['response']['task_id'])
            sys.stdout.write('\n')
            return res
        else:
            return r.json()['response']

    def wait_for_task(self, task_id, sleep_time=1):
        while True:
            ret = self.request('/tasks/%s' % task_id)
            if self.debug:
                print('ret', ret)
            if int(ret.get('progress', 0)) >= 100:
                return ret
            time.sleep(sleep_time)

    def get_all_servers(self):
        return self.request('servers')
