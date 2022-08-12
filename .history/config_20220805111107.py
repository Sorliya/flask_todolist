import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'A-VERY-LONG-SECRET-KEY'
    SQLALCHEMY_DATABASE_URI = 'sqlite:////Users/jiangzihui/Downloads/flask/microblog/example.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    



