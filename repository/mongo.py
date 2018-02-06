from pymongo import MongoClient

uri = "mongodb://tao:000000@127.0.0.1:27017/digital_currency_news?authSource=admin"
client = MongoClient(uri)

db = client['digital_currency_news']
collect = db['articles']


def save(article):
    if collect.find({"link": article['link']}).count() > 0:
        return
    collect.insert_one(article)
