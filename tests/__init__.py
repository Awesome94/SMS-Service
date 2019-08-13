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
        """
        Define test variables and initialize app.
        Set up a blank database for each test.
        """
        app.config['TESTING'] = True
        self.app = app.test_client()

    def tearDown(self):
        """Destroy blank bank database after each test"""
        pass
