#app.py
from flask import Flask, request, abort

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

line_bot_api = LineBotApi('hnhGjc7uyGly+b9JxA+bAAWg/J+ZsnZD8I/64IN5Xm8MZWmjUyw722rgb1JVKnFjUaY+3cNh6KHj4xlBxM6M0RH62I5ILFyuTcEja+ncy6hErwClZZ1BtEZShiG9LDQFbi3s1MBgbYUe7PrvrUCkoAdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('b3d4e6f23d6b1d2e7acceec870dda68a')


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
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    s = '你吃飯了嗎'
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text= s))


if __name__ == "__main__":
    app.run()