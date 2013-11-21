#!/usr/bin/env python

# -*- coding: utf-8 -*-

from client import ApiClient
from pprint import pprint
from loremipsum import get_paragraphs

client = ApiClient('access_key', 'secret_key')

for i in range(1, 10):
    print('====> creating image %02d ' % i)

    image_id = client.request('/images/', method='POST', blocking=False,
                              data={'name': 'Da Super Img ' + str(i),
                                    'description': unicode(get_paragraphs(1)),
                                    'preview_images': ['http://placehold.it/400', 'http://www.afullcup.com/Grocery-Coupon-Blog/wp-content/uploads/2010/11/Sale-Tags.jpg'],
                                    })

i = client.request('/images/', method='GET', blocking=False)
pprint(i)
