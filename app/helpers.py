import os
import africastalking
import nexmo
import queue

env_var = os.environ

sms_queue = queue.Queue(maxsize=0)


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
