# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup

import requests
from article import Article

import config
from spiders.spider import Spider

site_name = 'ZAKER'
homePageUrl = 'https://www.myzaker.com/channel/4'


class ZakerSpider(Spider):
    def run(self):
        print(site_name + ' spider is running...')
        news_list = load_news()
        for news in news_list:
            title = str(news.string)
            href = 'http:' + news['href']
            if any(keyword in title.lower() for keyword in config.keywords):
                new_article = Article(title, '', href, site_name)
                super(ZakerSpider, self).save_to_repository(new_article)


def load_news():
    home_page_data = requests.get(homePageUrl)
    home_page_html = BeautifulSoup(home_page_data.text, "html.parser")
    news_elements = home_page_html.find_all(class_="main")
    all_news_list = []
    for news_element in news_elements:
        news_list = news_element.find_all('a', href=True)
        all_news_list += news_list
    return all_news_list
