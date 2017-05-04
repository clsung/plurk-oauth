# -*- coding: utf-8 -*-
from oauth2 import (
    Client, Consumer, Request,
    SignatureMethod_HMAC_SHA1, Token,
)

# compatible python3
import sys
if sys.version_info >= (3, 0, 0):
    from urllib.parse import parse_qsl
    from urllib.parse import urlencode
else:
    from urlparse import parse_qsl
    from urllib import urlencode
    input = raw_input


class PlurkOAuth:
    def __init__(self, customer_key=None, customer_secret=None):
        self.base_url = 'https://www.plurk.com'
        self.request_token_url = '/OAuth/request_token'
        self.authorization_url = '/OAuth/authorize'
        self.access_token_url = '/OAuth/access_token'
        self.customer_key = customer_key
        self.customer_secret = customer_secret
        self.sign_method = SignatureMethod_HMAC_SHA1()
        self.consumer = None
        self.token = None
        self.oauth_token = {}
        if self.customer_key and self.customer_secret:
            self.consumer = Consumer(self.customer_key, self.customer_secret)

    def __unicode__(self):
        return self.base_url

    def _dump(self, data):
        # import pprint
        # pprint.pprint(data)
        pass

    def authorize(self, access_token_key=None, access_token_secret=None):
        while not self.consumer:
            self.get_consumer_token()
        if access_token_key and access_token_secret:
            self.oauth_token['oauth_token'] = access_token_key
            self.oauth_token['oauth_token_secret'] = access_token_secret
        else:
            self.get_request_token()
            verifier = self.get_verifier()
            self.get_access_token(verifier)

    def request(self, url, params=None, data=None):

        # Setup
        if self.oauth_token:
            self.token = Token(self.oauth_token['oauth_token'],
                               self.oauth_token['oauth_token_secret'])
        client = Client(self.consumer, self.token)
        req = self._make_request(self.base_url + url, params)

        # Get Request Token
        encoded_content = None
        if data:
            encoded_content = urlencode(data)
        resp, content = client.request(self.base_url + url, "POST",
                                       headers=req.to_header(), body=encoded_content)
        # for python3
        if isinstance(content, bytes):
            content = content.decode('utf-8')

        return resp['status'], content, resp.reason

    def get_consumer_token(self):

        # Setup
        print("Prepare the CONSUMER Info")

        verified = 'n'
        while verified.lower() != 'y':
            key = input('Input the CONSUMER_KEY: ')
            secret = input('Input the CONSUMER_SECRET: ')
            print('Consumer Key: %s' % str(key))
            print('Consumer Secret: %s' % str(secret))
            verified = input('Are you sure? (y/N) ')
        self.customer_key = key
        self.customer_secret = secret
        self.consumer = Consumer(self.customer_key, self.customer_secret)

    def _make_request(self, requestURL, param=None):
        request = Request.from_consumer_and_token(consumer=self.consumer,
                                                  token=self.token,
                                                  http_method='POST',
                                                  http_url=requestURL,
                                                  parameters=param,
                                                  is_form_encoded=True)
        request.sign_request(self.sign_method, self.consumer, self.token)
        return request

    def _has_pending_oauth_token(self):
        # TODO we dont know this is request or access token, may ambiguous
        return self.oauth_token \
            and 'oauth_token' in self.oauth_token \
            and 'oauth_token_secret' in self.oauth_token

    def get_request_token(self):

        if self._has_pending_oauth_token():
            # Already has a request/access token
            return

        # Get Token Key/Secret
        status, content, reason = self.request(self.request_token_url)
        if str(status) != '200':
            # TODO Declare an exception
            raise Exception(reason)
        self.oauth_token = dict(parse_qsl(content))
        self._dump(self.oauth_token)
        # print('Token Key: %s' % str(token['oauth_token']))
        # print('Token Secret: %s' % str(token['oauth_token_secret']))

    def get_verifier(self):

        # Setup
        print("Open the following URL and authorize it")
        print("%s?oauth_token=%s" % (self.base_url + self.authorization_url,
                                     self.oauth_token['oauth_token']))

        verified = 'n'
        while verified.lower() == 'n':
            verifier = input('Input the verification number: ')
            verified = input('Are you sure? (y/n) ')
        return verifier

    def get_verifier_url(self):

        if not self.oauth_token or 'oauth_token' not in self.oauth_token:
            # TODO Declare an exception
            raise Exception('Please request a token first')
        return '{0}{1}?oauth_token={2}'.format(self.base_url,
                                               self.authorization_url,
                                               self.oauth_token['oauth_token'])

    def get_access_token(self, verifier):

        status, content, reason = self.request(self.access_token_url, {
            'oauth_token_secret': self.oauth_token['oauth_token_secret'],
            'oauth_verifier': verifier,
        })
        if str(status) != '200':
            # TODO Declare an exception
            raise Exception(reason)
        # Get Token Key/Secret
        self.oauth_token = dict(parse_qsl(content))
        self._dump(self.oauth_token)
        # print('Access Key: %s' % str(self.oauth_token['oauth_token']))
        # print('Access Secret: %s' % str(self.oauth_token['oauth_token_secret']))
