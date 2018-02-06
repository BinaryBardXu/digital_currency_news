# -*- coding: utf-8 -*-
import sys
import pickle
from datetime import datetime
from utils.file_utils import ensure_dir
from utils.file_utils import is_file_already_exist

from repository.mongo import save

sys.setrecursionlimit(10000)

date = datetime.now().strftime("%Y-%m-%d")

base_directory_name = '/data/python/digital_currency_news_files/'


class Spider(object):
    def __init__(self):
        self.__directory_name = ''
        self.__full_directory_path = ''

    def run(self):
        pass

    def ensure_news_dir(self, directory_name):
        self.__directory_name = directory_name
        self.__full_directory_path = base_directory_name + directory_name + '/' + date
        ensure_dir(self.__full_directory_path)

    def write_news_to_file(self, new_article, title):
        file_name = self.__full_directory_path + '/' + title + '.json'
        if is_file_already_exist(file_name):
            return

        with open(file_name, 'wb+') as f:
            pickle.dump(new_article.serialize(), f)

    @staticmethod
    def save_to_repository(new_article):
        save(new_article.serialize())
