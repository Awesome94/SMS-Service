import africastalking


class SMS:
    def __init__(self):
        self.username = "YOUR_USERNAME"
        self.api_key = "YOUR_API_KEY"
        africastalking.initialize(self.username, self.api_key)
        self.sms = africastalking.SMS

    def send(self, recipients, message, sender):
        if isinstance(recipients, []):
            for reciever in recipients:
                try:
                    response = self.sms.send(
                        self.message, reciever, sender)
                    return response
                except Exception as e:
                    print('Encountered an error while sending: %s' % str(e))
        else:
            print("recipients should be a type of list")
