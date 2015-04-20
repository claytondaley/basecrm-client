__author__ = 'Clayton Daley'

import logging
logger = logging.getLogger(__name__)

import requests
from prototypes import BaseCrmAuthentication


class Password(BaseCrmAuthentication):
    def __init__(self, username, password):
        """
        Authenticate with an email and password

        Keyword arguments;
        email -- user's BaseCRM email
        password -- user's BaseCRM password
        """
        super(Password, self).__init__()

        data = {
            'grant_type': 'password',
            'username': username,
            'password': password,
        }
        url = "https://api.getbase.com/oauth2/token"
        headers = {
            # APP_ID: APP_SECRET
        }

        logger.debug("Preparing POST with:")
        logger.debug("url:  %s" % url)
        logger.debug("params:  %s" % data)
        logger.debug("headers:  %s" % headers)
        response = requests.post(url=url, data=data, headers=headers)
        logger.debug("Password response:\n%s" % response.text)
        self._access_token = "%s" % response.json()['access_token']
        self._refresh_token = response.json()['refresh_token']


class Token(BaseCrmAuthentication):
    def __init__(self, token):
        super(Token, self).__init__()
        # TODO: Check Token
        self._access_token = token