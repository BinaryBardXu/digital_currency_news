from app.repository.mongo import get_news


def get_latest_news():
    return get_news(50)
