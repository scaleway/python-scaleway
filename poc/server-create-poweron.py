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

raw_input('====> switching on server (and thus creating session) [press a key]')
client.request('/servers/%s/action/' % server_id, method='POST', data={'action':'powerOn'})

raw_input('====> getting serv [press a key]')
server = client.request('/servers/%s' % server_id)
print('server', server)

