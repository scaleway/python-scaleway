#!/usr/bin/env python

# -*- coding: utf-8 -*-

from client import ApiClient

client = ApiClient('access_key', 'secret_key')

for i in range(1, 19):
	print('====> creating serv %02d ' % i)

	server_id = client.request('/servers/', method='POST', blocking=True, data={'name':'srv'+str(i)})['result']

	server = client.request('/servers/%s' % server_id)

	client.request('/tags/%s/metadatas/root' % server['tags'][0],
							method='PUT',
							data={'value': '/dev/nbd0'},
							blocking=False)

	if i == 1:
		client.request('/tags/%s/metadatas/kernel' % server['tags'][0],
								method='PUT',
								data={'value': 'toto'},
								blocking=False)
	elif i == 2:
		client.request('/tags/%s/metadatas/initrd' % server['tags'][0],
								method='PUT',
								data={'value': 'tata'},
								blocking=False)


	client.request('/tags/%s/metadatas/nbdroot' % server['tags'][0],
							method='PUT',
							data={'value': '192.168.55.19,12%02d' % i},
							blocking=False)

	client.request('/servers/%s/action/' % server_id, 
					method='POST',
					data={'action': 'powerOn', 'pimoussip': 'Pimouss-1-1-1-%d' % i},
					blocking=False)
