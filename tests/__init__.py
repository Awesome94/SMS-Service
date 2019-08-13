from app import app
from flask_testing import TestCase


class BaseTestMixin(TestCase):
    def create_app(self):
        """
        Configure and return the Flask app
        """
        app.config.from_object('config.TestingConfig')
        return app

    def setUp(self):
 
        app.config['TESTING'] = True
        self.app = app.test_client()

    def tearDown(self):
        pass
