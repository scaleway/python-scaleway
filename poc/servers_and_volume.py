#!/usr/bin/env python

# -*- coding: utf-8 -*-

from client import ApiClient

client = ApiClient('access_key', 'secret_key')

raw_input('====> creating serv [press a key]')
server_id = client.request('/servers/', method='POST', blocking=True)['result']
print('server_id', server_id)

raw_input('====> switching on server (and thus creating session) SHOULD FAIL [press a key]')
client.request('/servers/%s/action/' % server_id, method='POST', data={'action': 'powerOn'})


raw_input('====> getting serv [press a key]')
server = client.request('/servers/%s' % server_id)
print('server', server)

raw_input('====> creating a ~1Gb volume [press a key]')
volume_id = client.request('/volumes/', method='POST', data={'disk_type': 'qcow2', "size": 1100000000}, blocking=True)['result']
print('volume_id', volume_id)

raw_input('====> updating volume of serv [press a key]')
client.request('/servers/%s' % server_id, method='PUT', data={'volumes': [volume_id]})

raw_input('====> updating volume of serv NORMALLY FAILING [press a key]')
resp = client.request('/servers/%s' % server_id, method='PUT', data={'volumes': [volume_id]})
from pprint import pprint
pprint(resp)


raw_input('====> getting serv [press a key]')
server = client.request('/servers/%s' % server_id)
print('server', server)

# Test server creation with direct volume assoc

raw_input('====> creating a NEW ~1Gb volume [press a key]')
volume_id = client.request('/volumes/', method='POST', data={'disk_type': 'qcow2', "size": 1100000000}, blocking=True)['result']
print('volume_id', volume_id)

raw_input('====> creating a NEW serv WITH a volume [press a key]')
server_id = client.request('/servers/', method='POST', data={'volumes': [volume_id]}, blocking=True)['result']
print('server_id', server_id)

raw_input('====> getting NEW serv [press a key]')
server = client.request('/servers/%s' % server_id)
print('server', server)

# end

raw_input('====> switching on server (and thus creating session) [press a key]')
client.request('/servers/%s/action/' % server_id, method='POST', data={'action': 'powerOn'})

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
