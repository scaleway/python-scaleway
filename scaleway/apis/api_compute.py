# -*- coding: utf-8 -*-
#
# Copyright (c) 2013-2016 Online SAS and Contributors. All Rights Reserved.
#                         Julien Castets <jcastets@scaleway.com>
#                         Kevin Deldycke <kdeldycke@scaleway.com>
#
# Licensed under the BSD 2-Clause License (the "License"); you may not use this
# file except in compliance with the License. You may obtain a copy of the
# License at https://opensource.org/licenses/BSD-2-Clause

from . import API

REGIONS = {
    'par1': {
        'url': 'https://api-fr-par.scaleway.com/instance/v1/zones/fr-par-1/',
    },
    'ams1': {
        'url': 'https://api-nl-ams.scaleway.com/instance/v1/zones/nl-ams-1/',
    },
    'fr-par-1': {
        'url': 'https://api-fr-par.scaleway.com/instance/v1/zones/fr-par-1/',
    },
    'fr-par-2': {
        'url': 'https://api-fr-par.scaleway.com/instance/v1/zones/fr-par-2/',
    },
    'fr-par-3': {
        'url': 'https://api-fr-par.scaleway.com/instance/v1/zones/fr-par-3/',
    },
    'nl-ams-1': {
        'url': 'https://api-nl-ams.scaleway.com/instance/v1/zones/nl-ams-1/',
    },
    'nl-ams-2': {
        'url': 'https://api-nl-ams.scaleway.com/instance/v1/zones/nl-ams-2/',
    },
    'pl-waw-1': {
        'url': 'https://api-pl-waw.scaleway.com/instance/v1/zones/pl-waw-1/',
    },
    'pl-waw-2': {
        'url': 'https://api-pl-waw.scaleway.com/instance/v1/zones/pl-waw-2/',
    }
}


class ComputeAPI(API):
    """ The default region is par1 as it was the first availability zone
    provided by Scaleway, but it could change in the future.
    """

    def __init__(self, **kwargs):
        region = kwargs.pop('region', None)
        base_url = kwargs.pop('base_url', None)

        assert region is None or base_url is None, \
            "Specify either region or base_url, not both."

        if base_url is None:
            region = region or 'par1'

            assert region in REGIONS, \
                "'%s' is not a valid Scaleway region." % region

            base_url = REGIONS.get(region)['url']

        super(ComputeAPI, self).__init__(base_url=base_url, **kwargs)
