from flask import Flask
from os import environ
from dotenv import load_dotenv, find_dotenv
from app.helpers import SMS, NexmoSMS


load_dotenv(find_dotenv())

# Creating a nexmo client object
nexmo_client = NexmoSMS()

# creating africa's talking client object
africas_talking_client = SMS()

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


from app import routes
