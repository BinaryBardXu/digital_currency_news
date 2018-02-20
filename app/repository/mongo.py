from pymongo import MongoClient
import pymongo
from manage import app

MONGO_URL = 'mongodb://%s:%s@%s:%s/%s?authSource=%s' % (app.config['MONGO_USER'],
                                                        app.config['MONGO_PASSWORD'],
                                                        app.config['MONGO_HOST'],
                                                        app.config['MONGO_HOST_PORT'],
                                                        app.config['MONGO_COLLECTION_NAME'],
                                                        app.config['MONGO_AUTH_SOURCE'])
print(MONGO_URL)

client = MongoClient(MONGO_URL)

db = client['digital_currency_news']
collect = db['articles']


def save(article):
    if collect.find({"$or": [{"link": article['link']}, {"title": article['title']}]}).count() > 0:
        return
    collect.insert_one(article)


def get_news(limit):
    news_list = []
    for news in list(collect.find().sort('date', pymongo.DESCENDING).limit(limit)):
        del news['_id']
        news_list.append(news)

    return news_list
