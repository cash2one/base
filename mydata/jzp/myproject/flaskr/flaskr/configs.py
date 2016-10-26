
class DefaultConfig(object):
    DEBUG = True
    HOST = "localhost"
    SECRET_KEY = 'development key'
    POSTGRESQL_HOST = "localhost"
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://user:password@%s/flaskr' % POSTGRESQL_HOST


APP_CONFIG = DefaultConfig

__all__ = ['APP_CONFIG']
