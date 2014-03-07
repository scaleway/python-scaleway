import requests
import slumber


class API(object):

    base_url = None

    def __init__(self, auth_token=None, base_url=None):
        self.auth_token = auth_token

        if base_url:
            self.base_url = base_url

    def make_requests_session(self):
        """ Attaches a X-Auth-Token header to requests.Session.
        """
        session = requests.Session()
        if self.auth_token:
            session.headers.update({
                'X-Auth-Token': self.auth_token
            })
        return session

    def get_api_url(self):
        # XXX: get url from environ or from config file
        return self.base_url

    def query(self):
        """ Gets a configured slumber.API object.
        """
        return slumber.API(
            self.get_api_url(),
            session=self.make_requests_session()
        )


from .api_account import AccountAPI
from .api_compute import ComputeAPI
