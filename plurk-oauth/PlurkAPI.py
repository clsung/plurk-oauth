import PlurkOAuth
import json

class PlurkAPI:
    def __init__(self, key = None, secret = None):
        self._oauth = PlurkOAuth.PlurkOAuth(key, secret)
        self._authorized = False

    def authorize(self, access_key = None, access_secret = None):
        self._oauth.authorize(access_key, access_secret)
        self._authorized = True

    def callAPI(self, path, options = None):
        if not self._authorized:
            self._oauth.authorize()
        return self._oauth.request(path, options)

if __name__ == '__main__':
    import os
    plurk = PlurkAPI(os.environ["CONSUMERKEY"], os.environ["CONSUMERSECRET"])
#    plurk.authorize('tqRtGMu7Btw9','SCjkkydnkWNA7gwwuZo7y9wshVlzl7Lr')
    print plurk.callAPI('/APP/Profile/getOwnProfile')
