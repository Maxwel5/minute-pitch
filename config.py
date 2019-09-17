import os

class Config:
    DEBUG=True
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:12345@localhost/pitches'
    SECRET_KEY='hjkhkljlekrnfqclknevn;kewrvnk'