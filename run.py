#!/usr/bin/env python
# coding: utf-8

# In[ ]:

from flask import Flask, request, abort, jsonify
import numpy as np
import pandas as pd
import requests as req
from io import StringIO
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
    html = req.get('https://www.twse.com.tw/fund/BFI82U?response=html&dayDate=&weekDate=&monthDate=&type=day')
    html.encoding='utf-8'
    table = pd.read_html(StringIO(html.text),header=0)
    df = table[0]
    df.drop(labels=df.columns[1:-1],axis=1,inplace=True)
    df.drop(labels=0,axis=0,inplace=True)
    df['110年01月26日 三大法人買賣金額統計表.3'] = df['110年01月26日 三大法人買賣金額統計表.3'].apply(
    lambda x : '{:.2f}億'.format(int(x)/100000000))
    Date = list(df.columns)[0]
    a = df[:].values.reshape(-1)
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=str(Date))

if __name__ == "__main__":
    app.run()