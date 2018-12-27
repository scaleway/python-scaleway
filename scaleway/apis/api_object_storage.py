from . import API

REGIONS = {
    'ams1': {
        'url': 'https://sis-ams1.scaleway.com/',
    }
}


class ObjectStorageAPI(API):
    """ The default region is ams1 as it was the first availability zone
    provided by Scaleway, but it could change in the future.
    """

    def __init__(self, **kwargs):
        region = kwargs.pop('region', None)
        base_url = kwargs.pop('base_url', None)

        assert region is None or base_url is None, \
            "Specify either region or base_url, not both."

        if base_url is None:
            region = region or 'ams1'

            assert region in REGIONS, \
                "'%s' is not a valid Scaleway region." % region

            base_url = REGIONS.get(region)['url']

        super(ObjectStorageAPI, self).__init__(base_url=base_url, **kwargs)
