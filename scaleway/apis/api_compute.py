# -*- coding: utf-8 -*-
#
# Copyright (c) 2013-2015 Online SAS and Contributors. All Rights Reserved.
#                         Julien Castets <jcastets@scaleway.com>
#                         Kevin Deldycke <kdeldycke@scaleway.com>
#
# Licensed under the BSD 2-Clause License (the "License"); you may not use this
# file except in compliance with the License. You may obtain a copy of the
# License at http://opensource.org/licenses/BSD-2-Clause

from . import API


REGIONS = {
    'par1': {
        'url': 'https://cp-par1.scaleway.com/',
    },
    'ams1': {
        'url': 'https://cp-ams1.scaleway.com/',
    }
}


class ComputeAPI(API):
    """ The default region is par1 as it was the first availability zone
    provided by Scaleway, but it could change in the future.
    """

    def __init__(self, region='par1', **kwargs):
        assert region in REGIONS
        base_url = REGIONS[region]['url']
        super(ComputeAPI, self).__init__(base_url=base_url, **kwargs)
