from pymongo import MongoClient
from config import app_config
import logging

logger = logging.getLogger(__name__)


def collection(_collection_name):
    if 'db' not in globals():
        init_db()
    return db[_collection_name]


def init_db():
    mongo_url = 'mongodb://%s:%s@%s:%s/%s?authSource=%s' % (app_config().MONGO_USER,
                                                            app_config().MONGO_PASSWORD,
                                                            app_config().MONGO_HOST,
                                                            app_config().MONGO_HOST_PORT,
                                                            app_config().MONGO_COLLECTION_NAME,
                                                            app_config().MONGO_AUTH_SOURCE)
    logger.info(mongo_url)
    client = MongoClient(mongo_url)
    global db
    db = client.digital_currency_news
