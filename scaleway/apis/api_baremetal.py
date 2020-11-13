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
    'fr-par-2': {
        'url': 'https://api.scaleway.com/baremetal/v1/zones/fr-par-2/',
    },
}


class BaremetalAPI(API):
    """ The default region is fr-par-2 as it was the first availability zone
    provided by Scaleway for baremetal servers, but it could change in the future.
    """

    def __init__(self, **kwargs):
        region = kwargs.pop('region', None)
        base_url = kwargs.pop('base_url', None)

        assert region is None or base_url is None, \
            "Specify either region or base_url, not both."

        if base_url is None:
            region = region or 'fr-par-2'

            assert region in REGIONS, \
                "'%s' is not a valid Scaleway region." % region

            base_url = REGIONS.get(region)['url']

        super(BaremetalAPI, self).__init__(base_url=base_url, **kwargs)
