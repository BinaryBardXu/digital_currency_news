from app.services.news_service import get_latest_news
from flask import jsonify

from . import api


@api.route('/')
def hello_world():
    return 'Hello, World!'


@api.route('/news', methods=['GET'])
def get():
    news_list = get_latest_news()
    print(news_list)
    return jsonify(news_list)
