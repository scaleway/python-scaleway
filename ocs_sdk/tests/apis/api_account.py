import unittest

from ocs_sdk.apis.api_account import AccountAPI


class TestComputeAPI(unittest.TestCase):

    def setUp(self):
        self.api = AccountAPI()

    def test_perm_matches(self):
        # simple permissions
        self.assertTrue(self.api.perm_matches('read', 'read'))
        self.assertTrue(self.api.perm_matches(None, 'read'))
        self.assertFalse(self.api.perm_matches('write', 'read'))
        # wildcard
        self.assertTrue(self.api.perm_matches('read', '*'))

        # nested permissions
        self.assertTrue(self.api.perm_matches('object:read', 'object:read'))
        self.assertTrue(self.api.perm_matches('object:read', 'object:*'))
        self.assertTrue(self.api.perm_matches(None, 'object:*'))
        self.assertFalse(self.api.perm_matches('object:write', 'object:read'))

        # different nested sizes
        self.assertTrue(self.api.perm_matches('object:read:subperm', '*'))
        self.assertTrue(self.api.perm_matches('object:read:hello', 'object'))
        self.assertFalse(self.api.perm_matches('object', 'object:read:hello'))
