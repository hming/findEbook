# -*- coding:UTF-8 -*-
import cookielib
import urllib
import urllib2
import re
import sys
 
import login
import commentURL


def getBookCategory():
    """

    get book category
    :return: array of book category
    """
    rt = []
    find_cat_re = re.compile(r'<li.+?<a href="(catalog.php.+?)">(.+?)</a>.+?</li>', re.DOTALL)
    indexRequest = urllib2.Request(commentURL.URL_BASE)
    index_page = urllib2.urlopen(indexRequest).read()
    index_page = index_page.decode("UTF-8")
    for cat in find_cat_re.findall(index_page):
        rt.append({'cat_url': cat[0], 'cat_name': cat[1]})
    return rt

if __name__ == '__main__':
    rt = getBookCategory()
    print rt




