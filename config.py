application_name = 'digital_currency_news_spiders'


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
        pass

    @staticmethod
    def merge_args(args):
        if args.mongo_user is not None:
            Config.MONGO_USER = args.mongo_user
        if args.mongo_password is not None:
            Config.MONGO_PASSWORD = args.mongo_password


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
