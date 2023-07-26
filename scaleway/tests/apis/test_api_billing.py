import unittest

from scaleway.apis.api_billing import BillingAPI


class TestBillingAPI(unittest.TestCase):

    def test_valid_endpoint(self):
        self.assertEqual(BillingAPI().base_url, 'https://api.scaleway.com/billing/v1')
