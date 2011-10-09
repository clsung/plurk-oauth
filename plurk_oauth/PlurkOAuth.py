import oauth2 as oauth
import urlparse
from urllib import urlencode

class PlurkOAuth:
    def __init__(self, customer_key = None, customer_secret = None):
        self.baseURL = 'http://www.plurk.com'
        self.request_token_url = '/OAuth/request_token'
        self.authorization_url = '/OAuth/authorize'
        self.access_token_url  = '/OAuth/access_token'
        self.customer_key = customer_key
        self.customer_secret = customer_secret
        self.sign_method = oauth.SignatureMethod_HMAC_SHA1()
        self.consumer = None
        self.token = None
        self.oauth_token = {}
        if self.customer_key and self.customer_secret:
            self.consumer = oauth.Consumer(self.customer_key, self.customer_secret)

    def __unicode__(self):
        return self.baseURL

    def _dump(self, data):
        #import pprint
        #pprint.pprint(data)
        pass

    def authorize(self, access_token_key = None, access_token_secret = None):
        while not self.consumer:
            self.get_consumer_token()
        if access_token_key and access_token_secret:
            self.oauth_token['oauth_token'] = access_token_key
            self.oauth_token['oauth_token_secret'] = access_token_secret
        else:
            self.get_request_token()
            verifier = self.get_verifier()
            self.get_access_token(verifier)

    def request(self, url, params = None, data = None):

        # Setup
        if self.oauth_token:
            self.token = oauth.Token(self.oauth_token['oauth_token'],
                    self.oauth_token['oauth_token_secret'])
        client = oauth.Client(self.consumer, self.token)
        req = self._make_request(self.baseURL + url, params)

        # Get Request Token
        encodedContent = None
        if data:
            encodedContent = urlencode(data)
        resp, content = client.request(self.baseURL + url, "POST",
                headers=req.to_header(), body = encodedContent)
        return resp['status'], content, resp.reason


    def get_consumer_token(self):

        # Setup
        print "Prepare the CONSUMER Info"

        verified = 'n'
        while verified.lower() != 'y':
            key = raw_input('Input the CONSUMER_KEY: ')
            secret = raw_input('Input the CONSUMER_SECRET: ')
            print 'Consumer Key: %s' % str(key)
            print 'Consumer Secret: %s' % str(secret)
            verified = raw_input('Are you sure? (y/N) ')
        self.customer_key = key
        self.customer_secret = secret
        self.consumer = oauth.Consumer(self.customer_key, self.customer_secret)

    def _make_request(self, requestURL, param = None):
        request = oauth.Request.from_consumer_and_token(consumer=self.consumer,
            token=self.token, http_method='POST',
            http_url= requestURL, parameters = param,
            is_form_encoded=True)
        request.sign_request(self.sign_method, self.consumer, self.token)
        return request

    def get_request_token(self):

        # Get Token Key/Secret
        content = self.request(self.request_token_url)
        self.oauth_token = dict(urlparse.parse_qsl(content))
        self._dump(self.oauth_token)
        #print 'Token Key: %s' % str(token['oauth_token'])
        #print 'Token Secret: %s' % str(token['oauth_token_secret'])

    def get_verifier(self):

        # Setup
        print "Open the following URL and authorize it"
        print "%s?oauth_token=%s" % (self.baseURL + self.authorization_url,
            self.oauth_token['oauth_token'])

        verified = 'n'
        while verified.lower() == 'n':
            verifier = raw_input('Input the verification number: ')
            verified = raw_input('Are you sure? (y/n) ')
        return verifier

    def get_access_token(self, verifier):

        content = self.request(self.access_token_url, {
            'oauth_token_secret': self.oauth_token['oauth_token_secret'],
            'oauth_verifier': verifier,
            } )
        # Get Token Key/Secret
        self.oauth_token = dict(urlparse.parse_qsl(content))
        self._dump(self.oauth_token)
        #print 'Access Key: %s' % str(self.oauth_token['oauth_token'])
        #print 'Access Secret: %s' % str(self.oauth_token['oauth_token_secret'])

