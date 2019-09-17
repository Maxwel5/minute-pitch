import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:12345@localhost/pitches'
    SECRET_KEY='hjkhkljlekrnfqclknevn;kewrvnk'

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:12345@localhost/pitches'
    pass

class DevConfig(Config):

    DEBUG = True

config_options = {
    'development':DevConfig,
    'production':ProdConfig
}