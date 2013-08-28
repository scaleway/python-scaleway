#!/usr/bin/env python

# -*- coding: utf-8 -*-

import time

from client import ApiClient
from printr import printr

from random import randrange

client = ApiClient('access_key', 'secret_key')


# rootfs=/dev/nbd0 nbdroot=192.168.50.19:1201 (pimouss-1-1-1-1 192.168.55.1)

for i in range(1, 19):
	print('====> creating serv %02d ' % i)

	server_id = client.request('/servers/', method='POST', blocking=True)['server_id']

	server = client.request('/servers/%s' % server_id)

	client.request('/tags/%s/metadatas/rootfs' % server['tags'][0],
							method='PUT',
							data={'value': '/dev/nbd0'},
							blocking=True)

	client.request('/tags/%s/metadatas/nbdroot' % server['tags'][0],
							method='PUT',
							data={'value': '192.168.50.19:12%02d' % i},
							blocking=True)

	client.request('/servers/%s/action/' % server['key'], 
					method='POST',
					data={'action': 'powerOn', 'pimoussip': 'Pimouss-1-1-1-%d' % i},
					blocking=True)
