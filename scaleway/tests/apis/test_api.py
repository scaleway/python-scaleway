# -*- coding: utf-8 -*-
#
# Copyright (c) 2013-2014 Online SAS and Contributors. All Rights Reserved.
#                         Julien Castets <jcastets@scaleway.com>
#                         Kevin Deldycke <kdeldycke@scaleway.com>
#
# Licensed under the BSD 2-Clause License (the "License"); you may not use this
# file except in compliance with the License. You may obtain a copy of the
# License at http://opensource.org/licenses/BSD-2-Clause

import unittest

import requests

from scaleway.apis import API

from . import FakeAPITestCase


class SimpleAPI(API):

    base_url = 'http://localhost'


class TestAPI(FakeAPITestCase, unittest.TestCase):

    def test_make_requests_session(self):
        # normal use
        requests_session = API(
            auth_token='0xdeadbeef', user_agent='jamesb0nd'
        ).make_requests_session()

        self.assertEqual(requests_session.headers.get('X-Auth-Token'),
                         '0xdeadbeef')
        self.assertEqual(requests_session.headers.get('User-Agent'),
                         'jamesb0nd')

        # no auth provided
        session_of_no_auth_api = API().make_requests_session()
        self.assertIsInstance(session_of_no_auth_api, requests.Session)
        self.assertNotIn('X-Auth-Token', session_of_no_auth_api.headers)

        # check flag verify_ssl
        self.assertTrue(API().make_requests_session().verify)
        self.assertFalse(API(verify_ssl=False).make_requests_session().verify)

        # HTTP headers must be latin1 encoded
        token_unicode = u'éè'
        session = SimpleAPI(auth_token=token_unicode).make_requests_session()
        self.assertEqual(
            session.headers['X-Auth-Token'],
            token_unicode.encode('latin1')
        )

    def test_get_api_url(self):
        self.assertEqual(SimpleAPI().get_api_url(), 'http://localhost')

        self.assertEqual(
            SimpleAPI(base_url='http://hello').get_api_url(), 'http://hello'
        )
