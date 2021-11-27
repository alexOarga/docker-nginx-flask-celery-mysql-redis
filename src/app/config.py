import os

class Config(object):
    DEBUG = True
    TESTING = False

    CSRF_ENABLED = True
    SECRET_KEY = os.environ.get('SECRET_KEY')

    DICT_LOGGER = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "simple": {
                "format": ("%(asctime)s [%(levelname)s] [%(name)s] | %(message)s")
            },
        },
    }


class ProductionConfig(Config):
    DEBUG = False

    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql:" \
                              + f"//{os.environ.get('MYSQL_USER')}:" \
                              + f"{os.environ.get('MYSQL_PASSWORD')}" \
                              + f"@{os.environ.get('MYSQL_HOST')}" \
                                f"/{os.environ.get('MYSQL_DATABASE')}"
    SQLALCHEMY_POOL_SIZE = 1

    CELERY_IMPORTS = ("app")
    CELERY_BROKER_URL = os.environ.get('CELERY_BROKER_URL')
    CELERY_RESULT_BACKEND = os.environ.get('CELERY_RESULT_BACKEND')
    REDIS_BROKER_URL = os.environ.get('REDIS_BROKER_URL')


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True

    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql:" \
                              + f"//{os.environ.get('MYSQL_USER')}:" \
                              + f"{os.environ.get('MYSQL_PASSWORD')}" \
                              + f"@{os.environ.get('MYSQL_HOST')}" \
                                f"/{os.environ.get('MYSQL_DATABASE')}"
    SQLALCHEMY_POOL_SIZE = 1

    CELERY_IMPORTS = ("app")
    CELERY_BROKER_URL = "redis://localhost:6379"
    CELERY_RESULT_BACKEND = "redis://localhost:6379"
    REDIS_BROKER_URL = "redis://localhost:6379"


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True

    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql:" \
                              + f"//{os.environ.get('MYSQL_USER')}:" \
                              + f"{os.environ.get('MYSQL_PASSWORD')}" \
                              + f"@{os.environ.get('MYSQL_HOST')}" \
                                f"/{os.environ.get('MYSQL_DATABASE')}"
    SQLALCHEMY_POOL_SIZE = 1

    CELERY_IMPORTS = ("app")
    CELERY_BROKER_URL = "redis://localhost:6379"
    CELERY_RESULT_BACKEND = "redis://localhost:6379"
    REDIS_BROKER_URL = "redis://localhost:6379"


class TestingConfig(Config):
    TESTING = True
    DEBUG = False

    SQLALCHEMY_DATABASE_URI = "sqlite://"
    SQLALCHEMY_POOL_SIZE = None
    SQLALCHEMY_POOL_TIMEOUT = None

    CELERY_IMPORTS = ("app")
    CELERY_BROKER_URL = "redis://localhost:6379"
    CELERY_RESULT_BACKEND = "redis://localhost:6379"
    REDIS_BROKER_URL = "redis://localhost:6379"


