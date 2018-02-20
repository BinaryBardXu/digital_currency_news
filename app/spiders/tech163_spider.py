# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup

import requests
from app.article import Article

import config
from app.spiders.spider import Spider

site_name = '网易科技'
homePageUrl = 'http://tech.163.com/'


class Tech163Spider(Spider):
    def run(self):
        super(Tech163Spider, self).banner(site_name)

        news_list = load_news()
        for news in news_list:
            title = str(news.string)
            href = news['href']
            if any(keyword in title for keyword in config.keywords):
                new_article = Article(title, '', href, site_name)
                super(Tech163Spider, self).save_to_repository(new_article)


def load_news():
    home_page_data = requests.get(homePageUrl)
    home_page_html = BeautifulSoup(home_page_data.text, "html.parser")
    news_elements = home_page_html.find(class_="main-news-area")
    return news_elements.find_all('a', href=True)
