#!/usr/bin/env python

# -*- coding: utf-8 -*-

import time

from client import ApiClient
from pprint import pprint

from random import randrange

client = ApiClient('access_key', 'secret_key')

raw_input('====> creating tag [press a key]')
tag_id = client.request('/tags/',
						method='POST',
						data={'name': 'tagname'+str(randrange(10)), 'metadata': {'test': 'bisou', 'commande': 'rm -rf *'}},
						blocking=True)['result']
print('tag_id', tag_id)

raw_input('====> updating tag metadata "test" key [press a key]')
client.request('/tags/%s/metadatas/%s' % (tag_id, 'test'),
				method='PUT',
				data={'value': 'bisous de bisounours'},
				blocking=True)

raw_input('====> creating & getting serv [press a key]')
server = client.request('/servers/', method='POST', blocking=True)
print('server', server)

raw_input('====> getting tag [press a key]')
tag = client.request('/tags/%s' % tag_id,
						method='GET')
print('tag', tag)

raw_input('====> attaching tag to serv [press a key]')
client.request('/servers/%s/tags/' % server['server_id'],
				method='POST',
				data={'tag': tag_id},
				blocking=True)

raw_input('====> getting serv [press a key]')
srv = client.request('/servers/%s' % server['server_id'])
print('server', srv)

raw_input('====> detaching tag from serv [press a key]')
client.request('/servers/%s/tags/%s' % (server['server_id'], tag_id),
				method='DELETE',
				blocking=True)

raw_input('====> getting serv [press a key]')
srv = client.request('/servers/%s' % server['server_id'])
print('server', srv)

raw_input('====> deleting "test" key [press a key]')
client.request('/tags/%s/metadatas/%s' % (tag_id, 'test'),
						method='DELETE')

raw_input('====> getting tag [press a key]')
tag = client.request('/tags/%s' % tag_id,
						method='GET')
print('tag', tag)

