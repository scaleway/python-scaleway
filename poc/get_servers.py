#!/usr/bin/env python

# -*- coding: utf-8 -*-

from client import ApiClient

client = ApiClient('access_key', 'secret_key')

for server in client.get_all_servers():
    print(server)
