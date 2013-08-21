# -*- coding: utf-8 -*-

import time
import requests
import json


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

    def request(self, path, method='GET', params=None, data=None, blocking=False):
        path = path.lstrip('/')
        url = '%s://%s/%s' % ('http', self.endpoint, path)
        print('\n%-6s %s data=%s' % (method, url, data))
        headers = {}
        if data:
            data = json.dumps(data)
            headers['content-type'] = 'application/json'
        r = requests.request(method, url, params=params, data=data, headers=headers)
        if r.status_code in (500, 405):
            print(r.text)
            return False
        if blocking:
            print(r.json())
            return self.wait_for_task(r.json()['response']['task_id'])
        else:
            return r.json()['response']

    def wait_for_task(self, task_id, sleep_time=.2):
        while True:
            ret = self.request('/tasks/%s' % task_id)
            print('ret', ret)
            if int(ret.get('progress', 0)) >= 100:
                return ret
            time.sleep(sleep_time)

    def get_all_servers(self):
        return self.request('servers')
