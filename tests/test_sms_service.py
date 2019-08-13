import json
from flask_testing import TestCase
from app.routes import nexmo_client
from tests import BaseTestMixin

q_object = {
    "to_number": "+256785916689",
    "message": "testing api",
    "provider": ""
}


class TestSMSservice(BaseTestMixin, TestCase):
    def test_different_status_for_correct_and_incorrect_to_number_nexmo(self):
        response = nexmo_client.send(q_object)
        self.assertEqual(response['messages'][0].get("status"), '9')
        q_object["to_number"] = "+25678591x6689"
        response = nexmo_client.send(q_object)
        q_object["to_number"] = "+256785916689"
        self.assertEqual(response['messages'][0].get("status"), '3')

    def test_default_provider_without_specifying_one(self):
        response = self.client.post(
            '/v1/sendsms', data=json.dumps(q_object), content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_when_provider_is_specified_as_nexmo(self):
        q_object["provider"] = "nexmo"
        response = self.client.post(
            '/v1/sendsms', data=json.dumps(q_object), content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_when_provider_is_specified_as_astalking(self):
        q_object["provider"] = "astalking"
        response = self.client.post(
            '/v1/sendsms', data=json.dumps(q_object), content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_root_endpoint_loads(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_404_error_handler(self):
        response = self.client.get('/invalid_url')
        self.assertEqual(response.status_code, 404)
