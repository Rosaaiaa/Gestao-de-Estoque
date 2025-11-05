from twilio.rest import Client
import random
import os

def gera_codigo():
    numero_aleatorio = random.randint(1000, 9999)

    account_sid = f'{os.getenv("TWILIO_ACCOUNT_ID")}'
    auth_token = f'{os.getenv("TWILIO_AUTH_TOKEN")}'
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        from_='whatsapp:+14155238886',
        content_sid='HXb5b62575e6e4ff6129ad7c8efe1f983e',
        content_variables='{"1":"12/1","2":"3pm"}',
        to='whatsapp:+5511985528776'
    )

    message.sid
    return numero_aleatorio