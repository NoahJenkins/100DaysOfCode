from twilio.rest import Client
from api_key import twilio_token, twilio_number, twilio_sid, verified_number

TWILIO_SID = twilio_sid
TWILIO_AUTH_TOKEN = twilio_token
TWILIO_VIRTUAL_NUMBER = twilio_number
TWILIO_VERIFIED_NUMBER = verified_number


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)