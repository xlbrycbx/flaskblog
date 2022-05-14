class Config:
    DEBUG=True
    SQLALCHEMY_DATABASE_URI ='sqlite:///sqlite/sqlite-tools-win32-x86-3380500/flaskblog.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True

class DevelopConfig(Config):
    ENV = 'development'

class ProductionConfig(Config):
    ENV = 'production'
    DEBUG = False