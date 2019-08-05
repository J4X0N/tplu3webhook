from linebot import LineBotApi
from linebot.models import TextSendMessage
from linebot.exceptions import LineBotApiError

line_bot_api = LineBotApi('Ny2sBxF9f3GrKcq3ZZTqLpOyUXjFOi/HK6PHC4ecUDk7t65YlTR0hmUOAYjdZxUgx4Rgt0bzTaPQQgNMqemmrqiXyYXeI/QH0vndjSoljYfhuZiM2ivaEsYeSos27Oz+rKQYW1NwZARV7hGyjpM8PwdB04t89/1O/w1cDnyilFU=
')

try:
    line_bot_api.push_message('<to>', TextSendMessage(text='Hello World!'))
except LineBotApiError as e:
    # error handle



import base64
import hashlib
import hmac

channel_secret = 968e28402f9b9007fc94ab37cf688a83 # Channel secret string
body = ... # Request body string
hash = hmac.new(channel_secret.encode('utf-8'),
    body.encode('utf-8'), hashlib.sha256).digest()
signature = base64.b64encode(hash)
# Compare X-Line-Signature request header and the signature