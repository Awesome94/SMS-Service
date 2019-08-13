import os
import africastalking
import nexmo

env_var = os.environ


class SMS:
    def __init__(self):
        self.username = env_var.get('AFRICAS_TALKING_USERNAME')
        self.api_key = env_var.get('AFRICAS_TALKING_KEY')
        africastalking.initialize(self.username, self.api_key)
        self.sms = africastalking.SMS

    def send(self, recipients, message, sender):
        if isinstance(recipients, []):
            for reciever in recipients:
                try:
                    response = self.sms.send(
                        self.message, reciever, sender)
                    print(response)
                except Exception as e:
                    print('Encountered an error while sending: %s' % str(e))
        else:
            print("recipients should be a type of list")


class NexmoSMS:
    def __init__(self):
        self.api_key = env_var.get('NEXMO_API_KEY')
        self.api_secret = env_var.get('NEXMO_API_SECRET')
        self.NexmoSMS = nexmo.Client(self.api_key, self.api_secret)

    def send(self, recipients, message, sender):
        if isinstance(recipients, []):
            for reciever in recipients:
                try:
                    response = self.NexmoSMS.send_message({
                        'from': sender,
                        'to': reciever,
                        'text': message
                    })
                    print(response)
                except Exception as e:
                    print('Encountered an error while sending: %s' % str(e))
        else:
            print("recipients should be a type of list")
