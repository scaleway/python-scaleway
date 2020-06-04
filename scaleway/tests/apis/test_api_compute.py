import unittest

from scaleway.apis.api_compute import REGIONS, ComputeAPI


class TestComputeAPI(unittest.TestCase):

    def test_set_region(self):
        # Default region: par1.
        self.assertEqual(
            ComputeAPI().base_url,
            'https://api-fr-par.scaleway.com/instance/v1/zones/fr-par-1/'
        )

        # Explicit "region".
        self.assertEqual(
            ComputeAPI(region='par1').base_url,
            'https://api-fr-par.scaleway.com/instance/v1/zones/fr-par-1/'
        )

        self.assertEqual(
            ComputeAPI(region='ams1').base_url,
            'https://api-nl-ams.scaleway.com/instance/v1/zones/nl-ams-1/'
        )

        # Explicit "base_url"
        self.assertEqual(ComputeAPI(base_url='http://whatever').base_url,
                         'http://whatever')

        # Explicit "region" AND "base_url" doesn't make sense.
        self.assertRaises(
            AssertionError,
            ComputeAPI, region='par1', base_url='http://whatever'
        )
