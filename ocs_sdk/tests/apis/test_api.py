import unittest

import slumber
import requests

from ocs_sdk.apis import API

from . import FakeAPITestCase


class SimpleAPI(API):

    base_url = 'http://localhost'


class TestAPI(FakeAPITestCase, unittest.TestCase):

    def test_make_requests_session(self):
        requests_session = API('0xdeadbeef').make_requests_session()
        self.assertEqual(
            requests_session.headers.get('X-Auth-Token'), '0xdeadbeef'
        )

        session_of_no_auth_api = API().make_requests_session()
        self.assertIsInstance(session_of_no_auth_api, requests.Session)
        self.assertNotIn('X-Auth-Token', session_of_no_auth_api.headers)

    def test_get_api_url(self):
        self.assertEqual(SimpleAPI().get_api_url(), 'http://localhost')
