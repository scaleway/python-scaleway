#!/usr/bin/env python

# -*- coding: utf-8 -*-

import time

from client import ApiClient
from pprint import pprint

from random import randrange

client = ApiClient('access_key', 'secret_key')

raw_input('creating serv [press a key]')
server_id = client.request('/servers/', method='POST', blocking=True)['server_id']
print('server_id', server_id)

raw_input('getting serv [press a key]')
server = client.request('/servers/%s' % server_id)
print('server', server)

raw_input('creating tag [press a key]')
tag_id = client.request('/tags/', method='POST', data={'tag': str(randrange(10))}, blocking=True)['tag_id']
print('tag_id', tag_id)

raw_input('getting tag [press a key]')
tag_id = client.request('/tags/%s' % tag_id)
print('tag_id', tag_id)

raw_input('assoc tag to serv [press a key]')
client.request('/servers/%s/tags/' % server_id, method='POST', data={'tag': tag_id})

raw_input('getting tags [press a key]')
for tag_id in server['tags']:
    client.request('/tags/%s/metadatas/' % tag_id, method='POST', data={'test': 'toto', 'rand': 'rand'}, blocking=True)
    tag = client.request('/tags/%s' % tag_id)
    print(tag)

