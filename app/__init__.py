from flask import Flask
from os import environ
from dotenv import load_dotenv, find_dotenv
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow


load_dotenv(find_dotenv())

# create APP
app = Flask(__name__)

# run app based on preffered or current environment


if environ.get('ENV') == 'LOCAL':
    app.config.from_object('config.DevelopmentConfig')
elif environ.get('ENV') == 'PROD':
    app.config.from_object('config.ProductionConfig')
elif environ.get('ENV') == 'TESTING':
    app.config.from_object('config.TestingConfig')
else:
    app.config.from_object('config.StagingConfig')

db = SQLAlchemy(app)
ma = Marshmallow(app)

migrate = Migrate(app, db)

from app import routes
