#!/usr/bin/env python
# coding: utf-8

# In[ ]:

from flask import Flask, request, abort, jsonify
import function 

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('Fx8Vyx/7ZThHhwUGbAEd5E5EdPgDw8Vr8601EUSfiS5ANZH/363uXhtc5OuxbDWLwMrXh0wFKYfYnk1EYX0tIiyhi87aYMnYwm0aej2RMJdLX1MWtypL8rZDV+5QfWqZE4dCfBrJ6ZWUtywIRY/y6AdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('3349934a19a854ea387d4ac55c88c175')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    result = function.stock()
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=result))
     line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text='Done!'))

if __name__ == "__main__":
    app.run()