# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup

import requests
from article import Article

import config
from spiders.spider import Spider

site_name = '华尔街见闻'
homePageUrl = 'https://wallstreetcn.com'


class WSJCNSpider(Spider):
    def run(self):
        super(WSJCNSpider, self).banner(site_name)

        news_list = load_news()
        for news in news_list:
            title = str(news.string)
            href = homePageUrl + news['href']
            if any(keyword in title for keyword in config.keywords):
                new_article = Article(title, '', href, site_name)
                super(WSJCNSpider, self).save_to_repository(new_article)


def load_news():
    home_page_data = requests.get(homePageUrl)
    home_page_html = BeautifulSoup(home_page_data.text, "html.parser")
    news_elements = home_page_html.find(class_="home-news-item__main")
    return news_elements.find_all('a', href=True)
