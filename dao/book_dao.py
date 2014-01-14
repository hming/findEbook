# -*- coding:UTF-8 -*-
class BookDAO(object):
    def __init__(self, db):
        self.db = db

    def set_db(self, db):
        self.db = db

    def get_cates_from_db(self):
        return self.db.book_cate.find()

    def find_book_from_db_by_url(self, book_url):
        return self.db.book_detail.find_one({"downloadUrl": book_url})

    def is_book_in_db(self, book):
        return self.find_book_from_db_by_url(book.get('downloadUrl')) is not None

    def insert_category(self, category):
        self.db.book_cate.insert(category)

    def insert_book(self, book):
        self.db.book_detail.insert(book)

