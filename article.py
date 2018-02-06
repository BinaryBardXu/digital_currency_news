from datetime import datetime


class Article(object):
    def __init__(self, title, content, link, site_name):
        self.__title = title
        self.__content = content
        self.__date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.__link = link
        self.__site_name = site_name

    def serialize(self):
        article = {
            'title': self.__title,
            'content': self.__content,
            'date': self.__date,
            'link': self.__link,
            'site_name': self.__site_name
        }
        return article
