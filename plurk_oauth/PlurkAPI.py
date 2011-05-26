import PlurkOAuth
import json

class PlurkAPI:
    def __init__(self, key = None, secret = None):
        if not key or not secret:
            raise ValueError, "Both CONSUMER_KEY and CONSUMER_SECRET need to be specified"
        self._oauth = PlurkOAuth.PlurkOAuth(key, secret)
        self._authorized = False
        self._error = {'code' : 200, 'reason' : ''}
        self._content = ''

    def authorize(self, access_key = None, access_secret = None):
        self._oauth.authorize(access_key, access_secret)
        self._authorized = True

    def callAPI(self, path, options = None):
#        if not self._authorized:
#            self._oauth.authorize()
        self._error['code'], self._content, self._error['reason'] = self._oauth.request(
                path, None, options)
        return json.loads(self._content)

    def error(self):
        return self._error


if __name__ == '__main__':
    import os
    plurk = PlurkAPI(os.environ["CONSUMERKEY"], os.environ["CONSUMERSECRET"])
#    plurk.authorize('tqRtGMu7Btw9','SCjkkydnkWNA7gwwuZo7y9wshVlzl7Lr')
    print plurk.callAPI('/APP/Profile/getOwnProfile')
