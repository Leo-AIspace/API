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

line_bot_api = LineBotApi('qgKEIN8g0IoO/Pu2iLX9qu/kgSvYltvyLO1hYLOuOLxTEEqe0RTzb9igyi2GCaTp0itkD1pG7ZPIPg/5k0ueWc9J+cBOej+wksxbnG6tz8vDvtKlNha4cegeG/EZbDflbzLY6+UsoEs8s/tyXvirXgdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('cae0a21bc70d9fe927110b86068bc3db')


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

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3000,debug=False)