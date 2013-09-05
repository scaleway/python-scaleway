#!/usr/bin/env python

# -*- coding: utf-8 -*-

import time

from client import ApiClient
from pprint import pprint

from random import randrange

client = ApiClient('access_key', 'secret_key')

raw_input('====> creating serv [press a key]')
server_id = client.request('/servers/', method='POST', blocking=True)['result']
print('server_id', server_id)

raw_input('====> getting serv [press a key]')
server = client.request('/servers/%s' % server_id)
print('server', server)

raw_input('====> updating image of serv [press a key]')
client.request('/servers/%s' % server_id, method='PUT', data={'image':'topdelire'})

raw_input('====> getting serv [press a key]')
server = client.request('/servers/%s' % server_id)
print('server', server)

raw_input('====> switching on server (and thus creating session) [press a key]')
client.request('/servers/%s/action/' % server_id, method='POST', data={'action':'powerOn'})

raw_input('====> getting serv [press a key]')
server = client.request('/servers/%s' % server_id)
print('server', server)

raw_input('====> getting session [press a key]')
session = client.request('/servers/%s/sessions/%s' % (server_id, server['current_session']))
print('session', session)

raw_input('====> deleting serv [press a key]')
server = client.request('/servers/%s' % server_id, method='DELETE')
print('server', server)

raw_input('====> getting serv [press a key]')
server = client.request('/servers/%s' % server_id, method='GET')
print('server', server)
