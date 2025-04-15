import os
from twilio.rest import Client

account_sid = ""
auth_token = ""

client = Client(account_sid, auth_token)

call = client.calls.create(
    url = "https://handler.twilio.com/twiml/",
    to = "+34 878 87 96 88",
    from_ = "+18474613533"
    )

