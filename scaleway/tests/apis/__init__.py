# -*- coding: utf-8 -*-
#
# Copyright (c) 2013-2016 Online SAS and Contributors. All Rights Reserved.
#                         Julien Castets <jcastets@scaleway.com>
#                         Kevin Deldycke <kdeldycke@scaleway.com>
#
# Licensed under the BSD 2-Clause License (the "License"); you may not use this
# file except in compliance with the License. You may obtain a copy of the
# License at https://opensource.org/licenses/BSD-2-Clause

import json

import httpretty
from six.moves.urllib.parse import urljoin


class FakeAPITestCase(object):

    def setUp(self):
        httpretty.enable()

    def tearDown(self):
        httpretty.disable()
        httpretty.reset()

    def fake_endpoint(self, api, endpoint, method=httpretty.GET,
                      body=None, status=200):

        if not callable(body):
            body = json.dumps(body)

        httpretty.register_uri(
            method,
            urljoin(api.get_api_url(), endpoint),
            body=body,
            content_type='application/json',
            status=status
        )
