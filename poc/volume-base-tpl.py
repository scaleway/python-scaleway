#!/usr/bin/env python

# -*- coding: utf-8 -*-

from client import ApiClient

from pprint import pprint

client = ApiClient('access_key', 'secret_key')

volume_id = client.request(
    '/volumes_internal/',
    method='POST',
    data={'size':4294967296,
          'internal_s3_uuid': '778160a8-0962-4692-8fcf-a50f638eb78b'},
    blocking=True
)['result']
print('volume_id', volume_id)
