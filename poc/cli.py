#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function

import argparse
from os.path import expanduser
from client import ApiClient
import pprint

global_client = None


def setup_client(client):
    global global_client
    global_client = client


def get_client():
    return global_client


def create_volume(size=None, base_volume=None):
    data = {'disk_type': 'qcow2'}
    if size:
        data['size'] = size
    if base_volume:
        data['base_volume'] = base_volume
    return get_client().request(
        '/volumes/', method='POST', data=data,
        blocking=True
    )['result']


def list_servers():
    return get_client().request('/servers/')

def create_server(name, volumes=None):
    data = {'name': name}
    if volumes:
        data.update({'volumes': volumes})
    return get_client().request(
        '/servers/',
        method='POST',
        data=data,
        blocking=True
    )['result']


def act_on_server(action, server_id):
    return get_client().request(
        '/servers/{}/action/'.format(server_id),
        method='POST',
        data={'action': action},
        blocking=True
    )['result']


def get_server(server_id):
    return get_client().request('/servers/{}'.format(server_id))


def test():
    with open(expanduser('~/.base_volume'), 'r') as f:
        base_vol = f.read()
    os_vol = create_volume(base_volume=base_vol)
    empty_vol = create_volume(size=(10 * 10 ** 9))
    server_id = create_server(test, volumes=[os_vol, empty_vol])
    act_on_server('poweron', server_id)
    act_on_server('poweroff', server_id)
    return server_id


def main():
    """ main """
    parser = argparse.ArgumentParser(description='Act on a server')
    parser.add_argument('-H', '--host', type=str, default='localhost',
                        help='Endpoint host')
    parser.add_argument('-p', '--port', type=int, default='5002',
                        help='Endpoint port')
    parser.add_argument('--access-key', type=str, default='access_key',
                        help='Access key')
    parser.add_argument('--secret-key', type=str, default='secret_key',
                        help='Secret key')

    subparsers = parser.add_subparsers(help='sub-command help', dest='entity')

    server_parser = subparsers.add_parser('test', help='Act on a server')

    server_parser = subparsers.add_parser('list-servers', help='Act on a server')

    server_parser = subparsers.add_parser('server', help='Act on a server')
    server_parser.add_argument(
        'action', type=str, help='The action to do',
        choices=['powerOn', 'powerOff', 'resetHard', 'resetSoft', 'status'],
    )
    server_parser.add_argument(
        'server_id', type=str,
        help='The server id on which the actions take effect'
    )

    server_parser = subparsers.add_parser('create-server',
                                          help='Create a new server')
    server_parser.add_argument(
        'name', type=str,
        help='The name of the server to create'
    )
    server_parser.add_argument(
        '--volumes', type=str, nargs='+',
        help='The volumes which will be attached to the volume'
    )

    volume_parser = subparsers.add_parser('volume',  help='Volume parser')
    volume_subparsers = volume_parser.add_subparsers(
        help='', dest='volume_action'
    )
    volume_raw_parser = volume_subparsers.add_parser('create-raw',
                                                     help='Create a raw volume')
    volume_raw_parser.add_argument(
        'size', type=lambda x: int(x) * (10 ** 9), help='Size in GB'
    )
    volume_base_parser = volume_subparsers.add_parser(
        'create-from-base', help='Create a raw volume using an other one as base'
    )
    volume_base_parser.add_argument('base', type=str, help='Base volume id')

    parsed = parser.parse_args()

    setup_client(ApiClient(parsed.access_key, parsed.secret_key,
                           endpoint='{}:{}'.format(parsed.host, parsed.port)))

    if parsed.entity == 'test':
        res = test()
    elif parsed.entity == 'server':
        if parsed.action == 'status':
            res = get_server(parsed.server_id)
        else:
            res = act_on_server(parsed.action, parsed.server_id)
    elif parsed.entity == 'list-servers':
        res = list_servers()
    elif parsed.entity == 'create-server':
        res = create_server(parsed.name, parsed.volumes)
    elif parsed.entity == 'volume':
        if parsed.volume_action == 'create-raw':
            res = create_volume(size=parsed.size)
        elif parsed.volume_action == 'create-from-base':
            res = create_volume(base_volume=parsed.base)
    pprint.pprint(res)


main()
