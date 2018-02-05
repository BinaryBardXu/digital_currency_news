from datetime import datetime


class Article(object):
    def __init__(self, title, content, link):
        self.__title = title
        self.__content = content
        self.__date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.__link = link

    def serialize(self):
        json = {
            'title': self.__title,
            'content': self.__content,
            'date': self.__date,
            'link': self.__link
        }
        print(str(json))
        return str(json)
