#!/usr/bin/env python

# -*- coding: utf-8 -*-

from client import ApiClient

client = ApiClient('access_key', 'secret_key')

for i in range(1, 10):
    print('====> creating image %02d ' % i)

    image_id = client.request('/images/', method='POST', blocking=False,
            data={'name':'img'+str(i),
                  'imgs': ['http://placehold.it/400', 'http://www.afullcup.com/Grocery-Coupon-Blog/wp-content/uploads/2010/11/Sale-Tags.jpg'],
                  'type':'OCS-Approved'})

    # image = client.request('/images/%s' % image_id)

    # client.request('/tags/%s/metadatas/root' % server['tags'][0],
    #                         method='PUT',
    #                         data={'value': '/dev/nbd0'},
    #                         blocking=False)

    # if i == 1:
    #     client.request('/tags/%s/metadatas/kernel' % server['tags'][0],
    #                             method='PUT',
    #                             data={'value': 'toto'},
    #                             blocking=False)
    # elif i == 2:
    #     client.request('/tags/%s/metadatas/initrd' % server['tags'][0],
    #                             method='PUT',
    #                             data={'value': 'tata'},
    #                             blocking=False)


    # client.request('/tags/%s/metadatas/nbdroot' % server['tags'][0],
    #                         method='PUT',
    #                         data={'value': '192.168.55.19,12%02d' % i},
    #                         blocking=False)

    # client.request('/servers/%s/action/' % server_id, 
    #                 method='POST',
    #                 data={'action': 'powerOn', 'pimoussip': 'Pimouss-1-1-1-%d' % i},
    #                 blocking=False)
