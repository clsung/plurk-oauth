Plurk-OAuth
======

Simple Wrapper of Plurk OAuth API

About
----
Plurk-OAuth is a wrapper for [Plurk API 2.0 beta](http://www.plurk.com/API/2)
You will need to [Sign Up](http://www.plurk.com/PlurkApp/register) for your own CUSTOMER TOKENs.

API.keys
----
You will need to save CONSUMER_KEY/CONSUMER_SECRET in API.keys, the
format is JSON. The example is below: (Replace contents in <...>)
{"CONSUMER_SECRET": "<SECERT>", "ACCESS_TOKEN": "<TOKEN>", "ACCESS_TOKEN_SECRET": "<TOKEN_SECRET>", "CONSUMER_KEY": "<KEY>"}

Example with ACCESS_TOKEN
----
``` python
from PlurkAPI import PlurkAPI

    plurk = PlurkAPI(CONSUMER_KEY, CONSUMER_SECRET)
    plurk.authorize(ACCESS_TOKEN,ACCESS_TOKEN_SECRET)
    print plurk.callAPI('/APP/Profile/getOwnProfile')
```


Example without ACCESS_TOKEN
----
``` python
from PlurkAPI import PlurkAPI

    plurk = PlurkAPI(CONSUMER_KEY, CONSUMER_SECRET)
    plurk.authorize()
    print plurk.callAPI('/APP/Profile/getOwnProfile')
```


Meta
----

* Code: `git clone git://github.com/clsung/plurk-oauth.git`
* Home: <http://github.com/clsung/plurk-oauth>
* Bugs: <http://github.com/clsung/plurk-oauth/issues>

Author
------

Cheng-Lung Sung :: clsung@gmail.com :: @clsung
