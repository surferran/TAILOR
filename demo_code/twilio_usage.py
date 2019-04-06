# -*- coding: utf-8 -*-
"""
Created on Sat Dec 15 17:31:26 2018

example from :
    https://www.twilio.com/docs/libraries/python
    
  

Test Your Installation

Try sending yourself an SMS message. 
Save the code sample on this page to your computer with a text editor. 
Be sure to update the account_sid, auth_token, and from_ phone number with values from your Twilio account. 
The to phone number can be your own mobile phone.

You should receive the text message on your phone.
    
"""

from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
# Your Auth Token from twilio.com/console
auth_token  = "your_auth_token"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+15558675309", 
    from_="+15017250604",
    body="Hello from Python!")

print(message.sid)