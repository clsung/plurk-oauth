import os
import unittest
from nose.tools import *
from plurk_oauth.PlurkAPI import PlurkAPI
import json

class TestThreeLeggedAPI(unittest.TestCase):
    def setUp(self):
        try: 
            file = open('API.keys', 'r+')
        except IOError:
            print "You need to put key/secret in API.keys"
            raise
        except:
            print "Unexpected error:", sys.exc_info()[0]
        else:
            data = json.load(file)
            file.close()
            self.plurk = PlurkAPI(data["CONSUMER_KEY"], data["CONSUMER_SECRET"])
            self.plurk.authorize(data["ACCESS_TOKEN"],data["ACCESS_TOKEN_SECRET"])

    def teardown(self):
        pass

    def test_get_ownprofile(self):
        jdata = self.plurk.callAPI('/APP/Profile/getOwnProfile')
        self.assertIsInstance(jdata, dict, "Object is a dict")
        self.assertGreater(jdata['user_info']['uid'], 0, "Self Uid > 0")
