import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'change_this_secret')
    SQLALCHEMY_DATABASE_URI = (
        os.environ.get('DATABASE_URL') or
        'mysql://root@localhost:3306/todolist_db'
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False