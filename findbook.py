# -*- coding:UTF-8 -*-
import urllib
import urllib2
import re
import os
from pymongo import MongoClient

import commentURL
import login

db = MongoClient('mongodb://localhost:27017/').test


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
        rt.append({'cat_url': commentURL.URL_BASE + '/' + cat[0], 'cat_name': cat[1]})
    return rt


def getCatePage(cateUrl):
    item_re = re.compile(r'<div class="r_b">.+?href="(u_book.php.+?)">.+?</a>', re.DOTALL)
    catePageRequest = urllib2.Request(cateUrl)
    catePage = urllib2.urlopen(catePageRequest).read()
    for item in item_re.findall(catePage):
        print item


def getCateMaxPage(cateUrl):
    maxPage_re = re.compile(r'<a href=".+?p=(.+?)(?=&amp;.+?title="最后页">)', re.DOTALL)
    catePageRequest = urllib2.Request(cateUrl)
    catePage = urllib2.urlopen(catePageRequest).read()
    pageNums = maxPage_re.findall(catePage)
    if len(pageNums) > 0:
        return pageNums[-1]


def getBookListPage(cateUrl, cateName):
    maxPage = getCateMaxPage(cateUrl)
    print maxPage
    for i in range(1, int(maxPage)):
        url_new = '%s&p=%d' % (cateUrl, i)
        print url_new
        item_re = re.compile(r'<div class="r_b">.+?href="(u_book.php.+?)">.+?</a>', re.DOTALL)
        listPageRequest = urllib2.Request(url_new)
        listPage = urllib2.urlopen(listPageRequest).read()
        for item in item_re.findall(listPage):
            book = getBook(commentURL.URL_BASE + '/' + item, cateName)
            if not isBookInDB(book):
                db.book_detail.insert(book)
                print book


def getBook(bookUrl, cateName):
    bookDetail_re = re.compile(r"<h1>(.+?)</h1>.+?作者：(.+?)</p>.+?字数：(.+?)</p>.+?下载电子书.+?location='(.+?)'",
                               re.DOTALL)
    bookPageRequest = urllib2.Request(bookUrl)
    bookDetailPage = urllib2.urlopen(bookPageRequest).read()
    items = bookDetail_re.findall(bookDetailPage)
    realDownloadRequest = urllib2.Request(commentURL.URL_BASE + '/' + items[0][3])
    realDownloadPage = urllib2.urlopen(realDownloadRequest)
    realDownloadUrl = realDownloadPage.url
    book = {
        'category': cateName,
        'name': items[0][0],
        'author': items[0][1],
        'worlds': items[0][2],
        'downloadUrl': realDownloadUrl
    }
    return book

#--
def downloadBook(downloadUrl, targetDir):
    """
    :downloadUrl donload url
    """
    if targetDir == '' or targetDir is None:
        targetDir = '/'
    local = downloadUrl.split(targetDir)[-1]
    local = os.path.join('/', local)
    urllib.urlretrieve(downloadUrl, local, Schedule)


def Schedule(a, b, c):
    '''''

    a:已经下载的数据块
    b:数据块的大小
    c:远程文件的大小
   '''
    per = 100.0 * a * b / c
    if per > 100:
        per = 100
    print '%.2f%%' % per


def getCatesFromDB():
    return db.book_cate.find()


def findBookFromDBByUrl(bookUrl):
    return db.book_detail.find_one({"downloadUrl": bookUrl})


def isBookInDB(book):
    return findBookFromDBByUrl(book.get('downloadUrl')) is not None


def initCate():
    cates = getBookCategory()
    catesInDB = getCatesFromDB()
    for cat in cates:
        inDB = False
        for oldCat in catesInDB:
            if oldCat.get('cat_name', '') == cat.get('cat_name', ''):
                inDB = True
                break
        if not inDB:
            db.book_cate.insert(cat)


def main():
    if not login.login('m221221', 'mm221221'):
        print 'Login Fail!'
        return
    initCate()#find category into db, if the cate have been in the db the ignore it.
    cates = getCatesFromDB()
    for cate in cates:
        print getBookListPage(cate.get('cat_url', ''), cate.get('cat_name', ''))


if __name__ == '__main__':
    main()










