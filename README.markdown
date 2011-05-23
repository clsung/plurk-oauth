Plurk-OAuth
======

Simple Wrapper of Plurk OAuth API


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
