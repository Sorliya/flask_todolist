import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'A-VERY-LONG-SECRET-KEY'
    SQLALCHEMY_DATABASE_URI = 'sqlite:////Users/jiangzihui/Downloads/flask/microblog/app.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USERNAME = os.environ.get('GMAIL_USERNAME') or 'MAIL_USERNAME'
    MAIL_PASSWORD = os.environ.get('GMAIL_PASSWORD') or 'MAIL_PASSWORD'
    



