#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
sys.path.append('plurk_oauth/')
from plurk_oauth import PlurkAPI
import getopt
import json


def usage():
    print('''Help Information:
    -h: Show help information
    ''')


if __name__ == '__main__':
    try:
        opts, args = getopt.getopt(sys.argv[1:], "ho:v", ["help", "output="])
    except getopt.GetoptError as err:
        print(str(err))  # will print something like "option -a not recognized"
        usage()
        sys.exit(2)
    with open('API.keys', 'r+') as f:
        data = json.load(f)
        plurk = PlurkAPI(data["CONSUMER_KEY"], data["CONSUMER_SECRET"])
        if data.get('ACCESS_TOKEN'):
            plurk.authorize(data["ACCESS_TOKEN"], data["ACCESS_TOKEN_SECRET"])
        else:
            plurk.authorize()
            data["ACCESS_TOKEN"] = plurk._oauth.oauth_token['oauth_token']
            data["ACCESS_TOKEN_SECRET"] = plurk._oauth.oauth_token['oauth_token_secret']
            f.seek(0)
            json.dump(data, f)

    content = 'Test from Plurk OAuth API'
    if len(sys.argv) > 1:
        content = sys.argv[1]
    qualifier = 'says'
    if len(sys.argv) > 2:
        qualifier = sys.argv[2]
    print(plurk.callAPI('/APP/Timeline/plurkAdd', {
        'content': content,
        'qualifier': qualifier
    }))
