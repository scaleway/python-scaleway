#!/usr/bin/env python

# -*- coding: utf-8 -*-

import time

from client import ApiClient
from pprint import pprint

from random import randrange

client = ApiClient('access_key', 'secret_key')

raw_input('====> creating serv [press a key]')
server_id = client.request('/servers/', method='POST', blocking=True)['server_id']
print('server_id', server_id)

raw_input('====> creating tag [press a key]')
tag_id = client.request('/tags/',
						method='POST',
						data={'name': 'tagname'+str(randrange(10)), 'metadata': {'test': 'bisou', 'commande': 'rm -rf *'}},
						blocking=True)['tag_id']

raw_input('====> creating tag [press a key]')
second_tag_id = client.request('/tags/',
								method='POST',
								data={'name': str(randrange(10)), 'metadata': {'super2': 'chouette', 'helloworld': 'echo "hello, world!";'}},
								blocking=True)['tag_id']

raw_input('====> switching on server (and thus creating session) [press a key]')
client.request('/servers/%s/action/' % server_id, method='POST', data={'action':'powerOn'})

raw_input('====> attaching tag 1 to serv [press a key]')
client.request('/servers/%s/tags/' % server_id,
				method='POST',
				data={'tag': tag_id},
				blocking=True)

raw_input('====> attaching tag 2 to serv [press a key]')
client.request('/servers/%s/tags/' % server_id,
				method='POST',
				data={'tag': second_tag_id},
				blocking=True)

raw_input('====> getting serv [press a key]')
server = client.request('/servers/%s' % server_id)
print('server', server)

raw_input('====> getting tags attached to serv [press a key]')
for tag_id in server['tags']:
	print(client.request('/tags/%s/metadatas/' % tag_id, method='GET'))
	print(client.request('/tags/%s' % tag_id))

