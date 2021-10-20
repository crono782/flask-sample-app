"""Application config module"""
import os


class Config:
    """Base config class"""

    SECRET_KEY = os.environ.get("SECRET_KEY", "donotusethiskey")


class DevConfig(Config):
    """Dev config class"""

    DEBUG = True


class TestConfig(Config):
    """Testing config class"""

    TESTING = True


class ProdConfig(Config):
    """Production config class"""

    DEBUG = False


config = {
    "development": DevConfig,
    "testing": TestConfig,
    "production": ProdConfig,
    "default": DevConfig,
}
