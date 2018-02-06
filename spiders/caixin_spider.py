# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup

import requests
from article import Article

import config
from spiders.spider import Spider

site_name = '财新网'
homePageUrl = 'http://www.caixin.com/?HOLDZH'


class CaixingSpider(Spider):
    def run(self):
        news_list = load_news()
        for news in news_list:
            title = str(news.string)
            href = news['href']
            if any(keyword in title for keyword in config.keywords):
                new_article = Article(title, '', href, site_name)
                super(CaixingSpider, self).save_to_repository(new_article)


def load_news():
    home_page_data = requests.get(homePageUrl)
    home_page_html = BeautifulSoup(home_page_data.text, "html.parser")
    news_elements = home_page_html.find(class_="homepageCon")
    return news_elements.find_all('a', href=True)
