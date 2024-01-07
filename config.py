import os

class Config():
    SECRET_KEY = os.environ.get('SECRET_KEY', 'default_secret_key')
    FLASK_DEBUG =  os.environ.get('FLASK_DEBUG')
    FLASK_APP = os.environ.get('FLASK_APP')