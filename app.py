from flask import Flask
from services.news_service import get_latest_news
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


@app.route('/')
def hello_world():
    return 'Hello, World!'


class News(Resource):
    def get(self):
        news_list = get_latest_news()
        print(news_list)
        return news_list


api.add_resource(News, '/api/news')

if __name__ == '__main__':
    app.run()
