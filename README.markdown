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
format is JSON. The example is below:
> {"CONSUMER_SECRET": "<i>I_am_consumer_secret</i>", "ACCESS_TOKEN": "<i>your_access_token</i>", "ACCESS_TOKEN_SECRET": "<i>your_access_token_secret</i>", "CONSUMER_KEY": "<i>I_am_consumer_key</i>"}

For the first time use, you can omit the ACCESS_TOKEN/ACCESS_TOKEN_SECRET
, after authorize(), they will be saved.


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
