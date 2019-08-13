
"""
This file contains configuration settings for the SMS Service.
Secrets are read from environment settings.
"""
import os

basedir = os.path.abspath(os.path.dirname(__file__))

ENV = os.environ.get("ENV")


class Config(object):
    DEBUG = False
    TESTING = False
    NEXMO_SECRET = os.environ.get("NEXMO_SECRET")
    NEXMO_KEY = os.environ.get("NEXMO_KEY")
    AFRICAS_TALKING_KEY = os.environ.get("AFRICAS_TALKING_KEY")
    AFRICAS_TALKING_USERNAME = os.environ.get("AFRICAS_TALKING_USERNAME")


class ProductionConfig(Config):
    pass


class StagingConfig(Config):
    DEBUG = True
    TESTING = True


class DevelopmentConfig(Config):
    DEBUG = True
    TESTING = True


class TestingConfig(Config):
    DEBUG = False
    TESTING = True
