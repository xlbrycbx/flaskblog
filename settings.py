class Config:
    SQLALCHEMY_DATABASE_URI ='sqlite:///C:/sqlite/sqlite-tools-win32-x86-3380500/flaskblog.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True
    SECRET_KEY = 'sldjfkdjkfjdkfjkdf'
    DEBUG = True


class DevelopConfig(Config):
    ENV = 'development'

class ProductionConfig(Config):
    ENV = 'production'
    DEBUG = False