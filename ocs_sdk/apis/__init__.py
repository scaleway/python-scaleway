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

    def safe_query(self, callable_query, args=None, kwargs=None,
                   http_status_caught=[404], default=None):
        """ Prevents slumber raising an exception when it can be handled.

        :param default: the value returned if an exception occured
        :param http_status_caught: list or HTTP error codes, catches 404 errors
                                   by default
        """
        try:
            return callable_query(*(args or tuple()), **(kwargs or {}))

        except slumber.exceptions.SlumberHttpBaseException as exc:
            if exc.response.status_code in http_status_caught:
                return default
            raise


from .api_account import AccountAPI
from .api_compute import ComputeAPI
