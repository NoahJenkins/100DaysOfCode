from twilio.rest import Client
from api_key import TW_SID, TW_AUTH

account_sid = TW_SID
auth_token = TW_AUTH
client = Client(account_sid, auth_token)

message = client.messages.create(
  from_='+18333241411',
  body= "Hello World",
  to='+18178980345'
)

print(message.sid)