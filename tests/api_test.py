import os
import unittest
from nose.tools import *
from plurk_oauth.PlurkAPI import PlurkAPI
import json

class Test0ConsumerTokenSecret(unittest.TestCase):
    def setUp(self):
        pass

    def teardown(self):
        pass

    def test_no_consumer_key(self):
        with self.assertRaises(ValueError):
            self.plurk = PlurkAPI()
            self.plurk.callAPI('/APP/Profile/getPublicProfile',
                {'user_id': 'clsung'})

    def test_invalid_consumer_key(self):
        self.plurk = PlurkAPI("token", "secret")
        r = self.plurk.callAPI('/APP/Profile/getPublicProfile',
                {'user_id': 'clsung'})
        self.assertIsNone(r)
        err = self.plurk.error()
        self.assertEqual(err['code'], "400")
        self.assertEqual(err['reason'], "BAD REQUEST")
        self.assertEqual(err['content']['error_text'],
            "40101:unknown application key")

class Test1AccessTokenSecret(unittest.TestCase):
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

    def teardown(self):
        pass

    def test_invalid_access_key(self):
        self.plurk.authorize("foor", "bar")
        r = self.plurk.callAPI('/APP/Profile/getOwnProfile')
        self.assertIsNone(r)
        err = self.plurk.error()
        self.assertEqual(err['code'], "400")
        self.assertEqual(err['reason'], "BAD REQUEST")
        self.assertEqual(err['content']['error_text'],
            "40106:invalid access token")

class TestThreeLeggedAPI(unittest.TestCase):
    def setUp(self):
        self.plurk = PlurkAPI.fromfile('API.keys')
        if not self.plurk.is_authorized:
            raise KeyError("You need to put cunsomer/access key/secret in API.keys")

    def teardown(self):
        pass

    def test_get_ownprofile(self):
        jdata = self.plurk.callAPI('/APP/Profile/getOwnProfile')
        self.assertIsInstance(jdata, dict, "Object is a dict")
        self.assertGreater(jdata['user_info']['uid'], 0, "Self Uid > 0")

class TestTwoLeggedAPI(unittest.TestCase):
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

    def teardown(self):
        pass

    def test_get_public_profile(self):
        jdata = self.plurk.callAPI('/APP/Profile/getPublicProfile',
                {'user_id': 'clsung'})
        self.assertIsInstance(jdata, dict, "Object is a dict")
        self.assertGreater(jdata['user_info']['uid'], 0, "Self Uid > 0")
        self.assertEqual(jdata['user_info']['nick_name'],
                "clsung", "Author's Name ;)")
