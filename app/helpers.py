import os
from app import app
from flask import jsonify, make_response
import africastalking
import nexmo
import queue

env_var = os.environ

sms_queue = queue.Queue(maxsize=0)


@app.errorhandler(404)
def route_not_found(e):
    return response('failed', 'Endpoint not found', 404)


@app.errorhandler(405)
def method_not_found(e):
    """
    Custom response for methods not allowed for the requested URLs
    """
    return response('failed', 'The method is not allowed for the requested URL', 405)


@app.errorhandler(500)
def internal_server_error(e):
    """
    Return a custom message for a 500 internal error
    """
    return response('failed', 'Internal server error', 500)


def response(status, message, status_code):
    return make_response(jsonify({
        'status': status,
        'message': message
    })), status_code


class SMS:
    def __init__(self):
        self.username = env_var.get('AFRICAS_TALKING_USERNAME')
        self.api_key = env_var.get('AFRICAS_TALKING_KEY')
        africastalking.initialize(self.username, self.api_key)
        self.sms = africastalking.SMS

    def send(self, reciever, message, q_object):
        sender = env_var.get('AFRICAS_TALKING_SHORT_CODE')
        to_number = [reciever]
        sms_queue.put(q_object)
        print("added task to queue:", q_object)
        try:
            response = self.sms.send(message, to_number, sender)
            sms_queue.get(q_object)
            print(q_object, "successfully removed from queue")
        except Exception as e:
            print('Encountered an error while sending: %s' % str(e))
        return response


class NexmoSMS:
    def __init__(self):
        self.api_key = env_var.get('NEXMO_KEY')
        self.api_secret = env_var.get('NEXMO_SECRET')
        self.NexmoSMS = nexmo.Client(self.api_key, self.api_secret)

    def send(self, reciever, message, q_object):
        sms_queue.put(q_object)
        sender = env_var.get('NEXMO_PHONENUMBER')
        print("added task to queue:", q_object)
        try:
            response = self.NexmoSMS.send_message({
                'from': sender,
                'to': reciever,
                'text': message
            })
            print(q_object, "successfully removed from queue")
        except Exception as e:
            print('Encountered an error while sending: %s' % str(e))
        return response
