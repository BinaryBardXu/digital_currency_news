from app.services.news_service import get_latest_news
from flask_restful import Api, Resource

from . import api_1_0
from flasgger import swag_from

api = Api(api_1_0)


class NewsResource(Resource):
    @swag_from('api_docs/news.yml')
    def get(self):
        news_list = get_latest_news()
        return news_list


api.add_resource(NewsResource, '/news')
