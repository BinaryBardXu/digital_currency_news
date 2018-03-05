import os
import logging
from time import strftime
from logging.handlers import RotatingFileHandler

application_name = 'digital_currency_news_spiders'
application_display_name = '数字货币新闻抓取'

default_log_path = 'logs'

swagger_config = {
    'title': application_display_name,
    'version': 'All',
    'uiversion': 3,
    "description": "仅供测试使用。"
}


def config_logging(log_path):
    if log_path is None:
        log_path = default_log_path

    if not log_path.endswith('/'):
        log_path += '/'

    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    default_handler = RotatingFileHandler(strftime(log_path + 'log.%Y_%m_%d_%H_%M'), maxBytes=1024 * 10,
                                          backupCount=100)
    default_handler.setLevel(logging.INFO)
    default_handler.setFormatter(formatter)
    logger.addHandler(default_handler)

    error_handler = RotatingFileHandler(strftime(log_path + 'error.log.%Y_%m_%d_%H_%M'), maxBytes=1024 * 10,
                                        backupCount=100)
    error_handler.setLevel(logging.ERROR)
    error_handler.setFormatter(formatter)
    logger.addHandler(error_handler)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    console_handler.setLevel(logging.INFO)
    logger.addHandler(console_handler)


class Config:
    DEBUG = True
    MONGO_USER = ''
    MONGO_PASSWORD = ''
    MONGO_HOST = '127.0.0.1'
    MONGO_HOST_PORT = '27017'
    MONGO_COLLECTION_NAME = 'digital_currency_news'
    MONGO_AUTH_SOURCE = 'admin'

    @staticmethod
    def init_app(app):
        app.config['SWAGGER'] = swagger_config

    @staticmethod
    def merge_args(args):
        if args.mongo_user is not None:
            Config.MONGO_USER = args.mongo_user
        if args.mongo_password is not None:
            Config.MONGO_PASSWORD = args.mongo_password
        config_logging(args.log_path)


class LocalConfig(Config):
    MONGO_USER = 'tao'
    MONGO_PASSWORD = '000000'


class DevelopmentConfig(Config):
    pass


class ProductionConfig(Config):
    pass


profiles = {
    'dev': DevelopmentConfig,
    'prod': ProductionConfig,

    'default': LocalConfig
}
