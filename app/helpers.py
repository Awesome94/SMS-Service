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
        self.sms_queue = sms_queue
        africastalking.initialize(self.username, self.api_key)
        self.sms = africastalking.SMS

    def send(self, q_object):
        sender = env_var.get('AFRICAS_TALKING_SHORT_CODE')
        self.sms_queue.put(q_object)
        print("added task to queue:", q_object)
        try:
            if not sms_queue.empty():
                fifo_sms = sms_queue.get()
                to_number = [fifo_sms.get("to_number")]
                message = fifo_sms.get("message")
                response = self.sms.send(message, to_number, sender)
                print(q_object, "successfully removed from queue")
        except Exception as e:
            response = 'Encountered an error while sending: %s' % str(e)
        return response


class NexmoSMS:
    def __init__(self):
        self.api_key = env_var.get('NEXMO_KEY')
        self.api_secret = env_var.get('NEXMO_SECRET')
        self.sms_queue = sms_queue
        self.NexmoSMS = nexmo.Client(self.api_key, self.api_secret)

    def send(self, q_object):
        sender = env_var.get('NEXMO_PHONENUMBER')
        self.sms_queue.put(q_object)
        print("added task to queue:", q_object)
        try:
            if not sms_queue.empty():
                fifo_sms = sms_queue.get()
                response = self.NexmoSMS.send_message({
                    'from': sender,
                    'to': fifo_sms.get("to_number"),
                    'text': fifo_sms.get("message")
                })
                print(q_object, "successfully removed from queue")
        except Exception as e:
            response = 'Encountered an error while sending: %s' % str(e)
        return response
