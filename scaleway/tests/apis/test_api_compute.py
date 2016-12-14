import unittest

from scaleway.apis.api_compute import REGIONS, ComputeAPI


class TestComputeAPI(unittest.TestCase):

    def test_set_region(self):
        # Default region: par1.
        self.assertEqual(ComputeAPI().base_url,
                         'https://cp-par1.scaleway.com/')

        # Explicit "region".
        self.assertEqual(ComputeAPI(region='par1').base_url,
                         'https://cp-par1.scaleway.com/')

        self.assertEqual(ComputeAPI(region='ams1').base_url,
                         'https://cp-ams1.scaleway.com/')

        # Explicit "base_url"
        self.assertEqual(ComputeAPI(base_url='http://whatever').base_url,
                         'http://whatever')

        # Explicit "region" AND "base_url" doesn't make sense.
        self.assertRaises(
            AssertionError,
            ComputeAPI, region='par1', base_url='http://whatever'
        )
