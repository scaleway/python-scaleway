import json
import urlparse

import httpretty


class FakeAPITestCase(object):

    def setUp(self):
        httpretty.enable()

    def tearDown(self):
        httpretty.disable()
        httpretty.reset()

    def fake_endpoint(self, api, endpoint, method=httpretty.GET, body=None):
        httpretty.register_uri(
            method,
            urlparse.urljoin(api.get_api_url(), endpoint),
            body=json.dumps(body),
            content_type='application/json'
        )
