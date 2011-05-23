Plurk-OAuth
======

Simple Wrapper of Plurk OAuth API


Example with ACCESS_TOKEN
----
from PlurkAPI import PlurkAPI

    plurk = PlurkAPI(CONSUMER_KEY, CONSUMER_SECRET)
    plurk.authorize(ACCESS_TOKEN,ACCESS_TOKEN_SECRET)
    print plurk.callAPI('/APP/Profile/getOwnProfile')


Example without ACCESS_TOKEN
----
from PlurkAPI import PlurkAPI

    plurk = PlurkAPI(CONSUMER_KEY, CONSUMER_SECRET)
    plurk.authorize()
    print plurk.callAPI('/APP/Profile/getOwnProfile')
