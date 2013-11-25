#!/usr/bin/env python

# -*- coding: utf-8 -*-

from __future__ import print_function
from os.path import expanduser

import argparse
from pprint import pprint

from client import ApiClient

from pprint import pprint
from uuid import uuid4

client = ApiClient('access_key', 'secret_key', endpoint='192.168.47.134:8080')

def test():
    folays_id = 'folays-{}'.format(str(uuid4()).split('-')[0])

    base_vol = 'Volume-bb5915d2-c6a8-472d-8458-ac88b4229e30'
    volume0_id = client.request(
        '/volumes/',
        method='POST',
        data={'disk_type': 'qcow2',
              "base_volume": base_vol,
              'name': folays_id},
        blocking=True
    )['result']
    print('Successfully cloned volume {} : {}', base_vol, volume0_id)

    server_id = client.request(
        '/servers/',
        method='POST',
        data={"volumes":[volume0_id],
              'name': folays_id},
        blocking=True
    )['result']
    print('server_id', server_id)

    status = client.request(
        '/servers/{}/action/'.format(server_id),
        method='POST',
        data={'action': 'poweron'},
        blocking=True
    )
    pprint(status)

    session = client.request('/servers/{}/sessions/'.format(server_id))
    pprint(session)

if __name__ == '__main__':
    test()
