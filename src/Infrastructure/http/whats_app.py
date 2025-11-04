from twilio.rest import Client
import random

def gera_codigo():
  numero_aleatorio = random.randint(1000, 9999)

  account_sid = ''
  auth_token = ''
  client = Client(account_sid, auth_token)

  message = client.messages.create(
    from_='whatsapp:+14155238886',
    content_sid='HX229f5a04fd0510ce1b071852155d3e75',
    content_variables='{"1":"'+ str(numero_aleatorio) +'"}',
    to='whatsapp:+5511995634027'
  )

  message.sid
  return numero_aleatorio