from http import client
from twilio.rest import Client
account_sid ='AC5f68d66034fb99fbc946c046d7bf7040'
auth_token ='924e93c4ae3529dfd9c37648da2a8b64'
client=Client(account_sid,auth_token)
call =client.calls.create( twiml='<Response><Say>welcome to the world of jarivs!!</Say></Response>',
    to='+918770165793',
    from_='+16083364156')
print(call)