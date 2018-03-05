from . import mongo_client
import logging
import pymongo

logger = logging.getLogger(__name__)

articles_collection = 'articles'

def get_news(limit):
    news_list = []
    for news in list(mongo_client.collection(articles_collection).find().sort('date', pymongo.DESCENDING).limit(limit)):
        del news['_id']
        news_list.append(news)

    return news_list
