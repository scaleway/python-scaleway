import unittest

from scaleway.apis.api_object_storage import ObjectStorageAPI


class TestObjectStorageAPI(unittest.TestCase):

    def test_set_region(self):
        # Default region: ams1.
        self.assertEqual(ObjectStorageAPI().base_url,
                         'https://sis-ams1.scaleway.com/')

        # Explicit "region".
        self.assertEqual(ObjectStorageAPI(region='ams1').base_url,
                         'https://sis-ams1.scaleway.com/')

        # Explicit "base_url"
        self.assertEqual(ObjectStorageAPI(base_url='http://whatever').base_url,
                         'http://whatever')

        # Explicit "region" AND "base_url" doesn't make sense.
        self.assertRaises(
            AssertionError,
            ObjectStorageAPI, region='ams1', base_url='http://whatever'
        )
