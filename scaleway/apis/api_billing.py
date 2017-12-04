from . import API


class BillingAPI(API):

    base_url = 'https://billing.scaleway.com'

    def __init__(self, **kwargs):
        base_url = kwargs.pop('base_url', BillingAPI.base_url)
        super(BillingAPI, self).__init__(base_url=base_url, **kwargs)
