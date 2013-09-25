#!/usr/bin/env python

# -*- coding: utf-8 -*-

from __future__ import print_function
from os.path import expanduser

import argparse
from pprint import pprint

from client import ApiClient

client = ApiClient('access_key', 'secret_key')

def test():
    with open(expanduser('~/.base_volume'), 'r') as f:
        base_vol = f.read()
    volume0_id = client.request(
        '/volumes/',
        method='POST',
        data={'disk_type': 'qcow2',
              "base_volume": base_vol},
        blocking=True
    )['result']
    print('Successfully cloned volume {} : {}', base_vol, volume0_id)

    volume1_id = client.request(
        '/volumes/',
        method='POST',
        data={'disk_type': 'qcow2', "size":4294967296},
        blocking=True
    )['result']
    print('volume_id', volume1_id)
    
    
    server_id = client.request(
        '/servers/',
        method='POST',
        data={"volumes":[volume0_id, volume1_id]},
        blocking=True
    )['result']
    print('server_id', server_id)
    
    act_on_server('powerOn', server_id)
#    act_on_server('powerOff', server_id)

def act_on_server(action, server_id):
    client.request(
        '/servers/{}/action/'.format(server_id),
        method='POST',
        data={'action': action},
        blocking=True
    )

def main():
    """ main """

    parser = argparse.ArgumentParser(description='Act on a server')
    parser.add_argument('action', type=str, choices=['powerOn', 'powerOff'],
                        help='The action to do')

    parser.add_argument('server_id', type=str,
                        help='The server id on which the actions take effect')

    parsed = parser.parse_args()

    act_on_server(parsed.action, parsed.server_id)

#main()
test()
