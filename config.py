class Config(object):
    SQLALCHEMY_DATABASE_URI = "sqlite://database.db"
    DEBUG = True

class DevelopmentConfig(Config):
    SQLALCHEMY_ECHO = True

class ProductionConfig(Config):
    DEBUG = False

class TestingConfig(Config):
    SQLALCHEMY_DATABASE_URI = "sqlite://test_database.db"
    TESTING = True

app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig
}