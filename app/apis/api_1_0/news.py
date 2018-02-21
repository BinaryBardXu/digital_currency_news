from app.services.news_service import get_latest_news
from flask import jsonify

from . import api_1_0


@api_1_0.route('/')
def hello_world():
    return 'Hello, World!'


@api_1_0.route('/news', methods=['GET'])
def get():
    news_list = get_latest_news()
    print(news_list)
    return jsonify(news_list)
