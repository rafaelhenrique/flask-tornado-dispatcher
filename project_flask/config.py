import os


class base_config(object):
    SITE_NAME = 'Flask + Tornado is cool ;)'
    SERVER_NAME = os.environ.get('SERVER_NAME')
    SECRET_KEY = os.environ.get('SECRET_KEY')
    MEU_SALT = b"my preciousssssssssssssss"
    SECRET_KEY = os.urandom(24) + MEU_SALT
    LOGENABLE = True


class dev_config(base_config):
    DEBUG = True
    ASSETS_DEBUG = True
    WTF_CSRF_ENABLED = False


class test_config(base_config):
    TESTING = True
    WTF_CSRF_ENABLED = False
