import requests
import slumber


class API(object):

    base_url = None

    def __init__(self, auth_token=None):
        self.auth_token = auth_token

    def make_requests_session(self):
        """ Attaches a X-Auth-Token header to requests.Session.
        """
        if not self.auth_token:
            return None

        session = requests.Session()
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
