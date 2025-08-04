import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'this_should_be_secret'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://mim9:mahmud123@localhost/todolist_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
