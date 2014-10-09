import unittest

import requests

from ocs_sdk.apis import API

from . import FakeAPITestCase


class SimpleAPI(API):

    base_url = 'http://localhost'


class TestAPI(FakeAPITestCase, unittest.TestCase):

    def test_make_requests_session(self):
        # normal use
        requests_session = API('0xdeadbeef').make_requests_session()
        self.assertEqual(
            requests_session.headers.get('X-Auth-Token'), '0xdeadbeef'
        )

        # no auth provided
        session_of_no_auth_api = API().make_requests_session()
        self.assertIsInstance(session_of_no_auth_api, requests.Session)
        self.assertNotIn('X-Auth-Token', session_of_no_auth_api.headers)

        # check flag verify_ssl
        self.assertTrue(API().make_requests_session().verify)
        self.assertFalse(API(verify_ssl=False).make_requests_session().verify)

    def test_get_api_url(self):
        self.assertEqual(SimpleAPI().get_api_url(), 'http://localhost')

        self.assertEqual(
            SimpleAPI(base_url='http://hello').get_api_url(), 'http://hello'
        )
