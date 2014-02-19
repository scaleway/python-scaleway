import unittest

from ocs_sdk.apis import API


class SimpleAPI(API):

    base_url = 'http://localhost'


class TestAPI(unittest.TestCase):

    def test_make_requests_session(self):
        requests_session = API('0xdeadbeef').make_requests_session()
        self.assertEqual(
            requests_session.headers.get('X-Auth-Token'), '0xdeadbeef'
        )

        self.assertIsNone(API().make_requests_session())

    def test_get_api_url(self):
        self.assertEqual(SimpleAPI().get_api_url(), 'http://localhost')
