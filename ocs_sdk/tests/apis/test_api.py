import unittest

import slumber

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

        self.assertIsNone(API().make_requests_session())

    def test_get_api_url(self):
        self.assertEqual(SimpleAPI().get_api_url(), 'http://localhost')

    def test_safe_query(self):
        api = API()
        api.base_url = 'http://localhost/'

        self.fake_endpoint(api, 'users/', status=500)

        self.assertIsNone(
            api.safe_query(api.query().users.get, http_status_caught=[500]),
        )

        self.assertRaises(
            slumber.exceptions.HttpServerError,
            api.safe_query, api.query().users.get
        )
