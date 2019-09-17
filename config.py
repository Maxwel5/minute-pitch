import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:12345@localhost/pitches'
    SECRET_KEY='hjkhkljlekrnfqclknevn;kewrvnk'

class ProdConfig(Config):
    pass

class DevConfig(Config):

    DEBUG = True