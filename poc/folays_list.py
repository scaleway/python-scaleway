#!/usr/bin/env python

# -*- coding: utf-8 -*-

from __future__ import print_function
from os.path import expanduser

import argparse
from pprint import pprint

from client import ApiClient

from pprint import pprint
from uuid import uuid4

client = ApiClient('access_key', 'secret_key',
                   endpoint='192.168.47.134:8080',
                   debug=False)

def test():
    servers = client.request('/servers/')
    print('{} servers'.format(len(servers)))
    for server in servers:
        row = {}
        sessions = client.request('/servers/{}/sessions'.format(server['key']))
        row['server'] = server['key']
        row['state'] = server['state']
        if len(sessions):
            session = sessions[0]
            row['pimouss'] = session['pimouss']
            row['ip'] = session['pimouss_ip']
            row['started'] = session['started_at']
        print(', '.join(['{}={}'.format(k, v) for k, v in row.items()]))

if __name__ == '__main__':
    test()
