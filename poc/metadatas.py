#!/usr/bin/env python

# -*- coding: utf-8 -*-

import time

from client import ApiClient


client = ApiClient('access_key', 'secret_key')

server_id = client.request('/servers/', method='POST', blocking=True)['server_id']

server = client.request('/servers/%s' % server_id)

for tag_id in server['tags']:
    client.request('/tags/%s/metadatas/' % tag_id, method='POST', data={'test': 'toto', 'rand': 'rand'}, blocking=True)
    tag = client.request('/tags/%s' % tag_id)
    print(tag)
