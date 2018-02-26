from pymongo import MongoClient
import application
import pymongo

MONGO_URL = 'mongodb://%s:%s@%s:%s/%s?authSource=%s' % (application.config.MONGO_USER,
                                                        application.config.MONGO_PASSWORD,
                                                        application.config.MONGO_HOST,
                                                        application.config.MONGO_HOST_PORT,
                                                        application.config.MONGO_COLLECTION_NAME,
                                                        application.config.MONGO_AUTH_SOURCE)
client = MongoClient(MONGO_URL)

db = client.digital_currency_news
articles_collection = db.articles


def get_news(limit):
    news_list = []
    for news in list(articles_collection.find().sort('date', pymongo.DESCENDING).limit(limit)):
        del news['_id']
        news_list.append(news)

    return news_list
