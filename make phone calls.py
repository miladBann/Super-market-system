from twilio.rest import Client


auth_key = "36a9c902b942e22b60e5589432b8cc95"
acc_sid = "AC65bad8d2579e711ed04969b7e99f976a"


client = Client(acc_sid, auth_key)

call = client.calls.create(
    to="+972523543093", from_="+97293762128", url="http://demo.twilio.com/docs/voice.xml")

print(call.sid)
