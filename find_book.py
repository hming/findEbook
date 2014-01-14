# -*- coding:UTF-8 -*-
import Queue

__author__ = 'Minco'
import urllib
import urllib2
import re
import os
import threading
from pymongo import MongoClient

import commentURL
import login
from dao.book_dao import BookDAO

queue = Queue.Queue()
db = MongoClient('mongodb://localhost:27017/').test
book_dao = BookDAO(db)


class FindBook(threading.Thread):
    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.queue = queue

    def run(self):
        while True:
            cate = self.queue.get()
            get_book_list_page(cate.get('cat_url', ''), cate.get('cat_name', ''))
            self.queue.task_done()


def get_book_category():
    """

    get book category
    :return: array of book category
    """
    rt = []
    find_cat_re = re.compile(r'<li.+?<a href="(catalog.php.+?)">(.+?)</a>.+?</li>', re.DOTALL)
    index_request = urllib2.Request(commentURL.URL_BASE)
    index_page = urllib2.urlopen(index_request).read()
    index_page = index_page.decode("UTF-8")
    for cat in find_cat_re.findall(index_page):
        rt.append({'cat_url': commentURL.URL_BASE + '/' + cat[0], 'cat_name': cat[1]})
    return rt


def get_cate_page(cate_url):
    item_re = re.compile(r'<div class="r_b">.+?href="(u_book.php.+?)">.+?</a>', re.DOTALL)
    cate_page_request = urllib2.Request(cate_url)
    cate_page = urllib2.urlopen(cate_page_request).read()
    for item in item_re.findall(cate_page):
        print item


def get_cate_max_page(cate_url):
    max_page_re = re.compile(r'后十页</a>.+?p=(.+?)&amp;.+?title="最后页">', re.DOTALL)
    cate_page_request = urllib2.Request(cate_url)
    cate_page = urllib2.urlopen(cate_page_request).read()
    page_nums = max_page_re.findall(cate_page)
    if len(page_nums) > 0:
        return page_nums[0]
    return 0


def get_book_list_page(cate_url, cate_name):
    max_page = get_cate_max_page(cate_url)
    print cate_url
    print max_page
    for i in range(1, int(max_page)):
        url_new = '%s&p=%d' % (cate_url, i)
        print url_new
        item_re = re.compile(r'<div class="r_b">.+?href="(u_book.php.+?)">.+?</a>', re.DOTALL)
        list_page_request = urllib2.Request(url_new)
        list_page = urllib2.urlopen(list_page_request).read()
        for item in item_re.findall(list_page):
            book = getBook(commentURL.URL_BASE + '/' + item, cate_name)
            if not book_dao.is_book_in_db(book):
                book_dao.insert_book(book)
                print book


def getBook(book_url, cate_name):
    book_detail_re = re.compile(r"<h1>(.+?)</h1>.+?作者：(.+?)</p>.+?字数：(.+?)</p>.+?下载电子书.+?location='(.+?)'",
                                re.DOTALL)
    book_page_request = urllib2.Request(book_url)
    book_detail_page = urllib2.urlopen(book_page_request).read()
    items = book_detail_re.findall(book_detail_page)
    real_download_request = urllib2.Request(commentURL.URL_BASE + '/' + items[0][3])
    real_download_page = urllib2.urlopen(real_download_request)
    real_download_url = real_download_page.url
    book = {
        'category': cate_name,
        'name': items[0][0],
        'author': items[0][1],
        'worlds': items[0][2],
        'downloadUrl': real_download_url
    }
    return book


def download_book(self, download_url, target_dir):
    """
    :downloadUrl donload url
    """
    if target_dir == '' or target_dir is None:
        target_dir = '/'
    local = download_url.split(target_dir)[-1]
    local = os.path.join('/', local)
    urllib.urlretrieve(download_url, local, schedule)


def schedule(a, b, c):
    '''''

    a:已经下载的数据块
    b:数据块的大小
    c:远程文件的大小
   '''
    per = 100.0 * a * b / c
    if per > 100:
        per = 100
    print '%.2f%%' % per


def init_cate():
    cates = get_book_category()
    cates_in_db = book_dao.get_cates_from_db()
    for cat in cates:
        in_db = False
        for old_cat in cates_in_db:
            if old_cat.get('cat_name', '') == cat.get('cat_name', ''):
                in_db = True
                break
        if not in_db:
            db.book_cate.insert(cat)


def main():
    if not login.login('m221221', 'mm221221'):
        print 'Login Fail!'
        return
    for i in xrange(4):
        find_book = FindBook(queue)
        find_book.setDaemon(True)
        find_book.start()
    init_cate()#find category into db, if the cate have been in the db the ignore it.
    cates = book_dao.get_cates_from_db()
    for cate in cates:
        queue.put(cate)
        print cate
    queue.join()


if __name__ == '__main__':
    main()

