# -*- coding:UTF-8 -*-
import cookielib
import urllib
import urllib2

import commentURL

#--
'''

'''
def login(userName, password):
    LOGIN_SUCCESS_FLAG = 'logout.php'
    cj = cookielib.LWPCookieJar()

    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
    urllib2.install_opener(opener)
    parameter = {
        "user": userName,
        "pass": password,
        "ret": commentURL.URL_BASE
    }
    req = urllib2.Request(
        url=commentURL.URL_LOGIN,
        data=urllib.urlencode(parameter)
    )
    jump = urllib2.urlopen(req)
    rs_str = jump.read()
    return rs_str.index(LOGIN_SUCCESS_FLAG) > -1


def logout():
    logout_request = urllib2.Request(commentURL.URL_LOGOUT)
    try:
        urllib2.urlopen(logout_request)
        return True
    except IOError:
        return False




