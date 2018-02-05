# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup

import requests
from article import Article


import config
from spiders.spider import Spider

directory_name = 'caixing'
homePageUrl = 'http://www.caixin.com/?HOLDZH'


class CaixingSpider(Spider):
    def run(self):
        super(CaixingSpider, self).ensure_news_dir(directory_name)

        news_list = load_news()
        for news in news_list:
            title = str(news.string)
            href = news['href']
            if any(keyword in title for keyword in config.keywords):
                article_page_data = requests.get(href, timeout=20)

                article_page_html = BeautifulSoup(article_page_data.text, "html.parser")
                article_content = article_page_html.find(id='Main_Content_Val')
                new_article = Article(title, article_content, href)
                super(CaixingSpider, self).write_news_to_file(new_article, title)


def load_news():
    home_page_data = requests.get(homePageUrl)
    home_page_html = BeautifulSoup(home_page_data.text, "html.parser")
    news_elements = home_page_html.find(class_="news_list")
    return news_elements.find_all('a', href=True)
