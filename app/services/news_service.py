from app.repository.article_repo import get_news


def get_latest_news():
    return get_news(50)
