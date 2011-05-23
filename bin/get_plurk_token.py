import oauth2 as oauth
import urlparse
import httplib

#Plurk OAuth service endpoints:
#obtain request token:
REQUEST_TOKEN_URL = 'http://www.plurk.com/OAuth/request_token'
#authorization page:
AUTHORIZE_URL = 'http://www.plurk.com/OAuth/authorize'
#obtain access token:
ACCESS_TOKEN_URL = 'http://www.plurk.com/OAuth/access_token'

CONSUMER_KEY = 'qybNeecuywIO'
CONSUMER_SECRET = 'CkVuCnhbO3V8xf78HyxC7X25HMs6wbgi'

def get_consumer_token():

    # Setup
    print "Prepare the CONSUMER Info"

    verified = 'n'
    while verified.lower() != 'y':
        key = raw_input('Input the CONSUMER_KEY: ')
        secret = raw_input('Input the CONSUMER_SECRET: ')
        print 'Consumer Key: %s' % str(key)
        print 'Consumer Secret: %s' % str(secret)
        verified = raw_input('Are you sure? (y/N) ')
    return dict({'KEY':key,'SECRET':secret})

def get_request_token(key, secret):

    # Setup
    consumer = oauth.Consumer(key, secret)
    client = oauth.Client(consumer)
    sign_method = oauth.SignatureMethod_HMAC_SHA1()
    request = oauth.Request.from_consumer_and_token(consumer=consumer,
        http_method='POST', http_url=REQUEST_TOKEN_URL,
        is_form_encoded=True)
    request.sign_request(sign_method, consumer, None)

    # Get Request Token
    resp, content = client.request(REQUEST_TOKEN_URL, "POST", 
            headers=request.to_header())
    if resp['status'] != '200':
        raise Exception("Invalid response %s." % resp['status'])

    # Get Token Key/Secret
    token = dict(urlparse.parse_qsl(content))
    print 'Token Key: %s' % str(token['oauth_token'])
    print 'Token Secret: %s' % str(token['oauth_token_secret'])
    return token

def get_verifier(token_key):

    # Setup
    print "Open the following URL and authorize it"
    print "%s?oauth_token=%s" % (AUTHORIZE_URL, token_key)

    verified = 'n'
    while verified.lower() == 'n':
        verifier = raw_input('Input the verification number: ')
        verified = raw_input('Are you sure? (y/n) ')
    return verifier

def get_access_token(token_key, token_secret, verifier):

    # Setup
    consumer = oauth.Consumer(CONSUMER_KEY, CONSUMER_SECRET)
    token = oauth.Token(token_key, token_secret)
    token.set_verifier(verifier)
    client = oauth.Client(consumer,token)
    request = oauth.Request.from_consumer_and_token(consumer=consumer,
        token=token, http_method='POST', http_url=ACCESS_TOKEN_URL,
        parameters = {'oauth_token_secret': token_secret,},
        is_form_encoded=True)
    sign_method = oauth.SignatureMethod_HMAC_SHA1()
    request.sign_request(sign_method, consumer, token)
    #print request.get_normalized_parameters()
    #print request.to_header()

    # Get Access Token
    resp, content = client.request(ACCESS_TOKEN_URL, "POST", 
            headers=request.to_header())
    if resp['status'] != '200':
        print content
        raise Exception("Invalid response %s." % resp['status'])

    # Get Token Key/Secret
    token = dict(urlparse.parse_qsl(content))
    print 'Access Key: %s' % str(token['oauth_token'])
    print 'Access Secret: %s' % str(token['oauth_token_secret'])
    return token

if __name__ == '__main__':
    consumer = get_consumer_token()
    token = get_request_token(consumer['KEY'], consumer['SECRET'])
    verifier = get_verifier(token['oauth_token'])
    access_token = get_access_token(token['oauth_token'], token['oauth_token_secret'],
            verifier)
