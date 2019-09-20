import os

class Config:
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:12345@localhost/pitches'

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    SECRET_KEY=os.environ.get('SECRET_KEY')
    pass

class DevConfig(Config):

    SECRET_KEY = 'JHFEIEWHGOIHWEOIUGHWEPIUHP'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:12345@localhost/pitches'
    DEBUG = True

config_options = {
    'development':DevConfig,
    'production':ProdConfig
}