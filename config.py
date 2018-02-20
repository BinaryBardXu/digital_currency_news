keywords = ['虚拟货币',
            '数字货币',
            '加密货币',
            '加密货币',
            '区块链',
            '比特币',
            '币圈',
            'bitcoin',
            'cryptocurrency']


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


class DevelopmentConfig(Config):
    MONGO_USER = 'tao'
    MONGO_PASSWORD = '000000'


class ProductionConfig(Config):
    MONGO_USER = 'tao_prod'
    MONGO_PASSWORD = '000000'


config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}
