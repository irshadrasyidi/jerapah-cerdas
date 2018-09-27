from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *
import requests, json

import random

import errno
import os
import sys, random
import tempfile
import requests
import re

from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
    SourceUser, SourceGroup, SourceRoom,
    TemplateSendMessage, ConfirmTemplate, MessageAction,
    ButtonsTemplate, ImageCarouselTemplate, ImageCarouselColumn, URIAction,
    PostbackAction, DatetimePickerAction,
    CarouselTemplate, CarouselColumn, PostbackEvent,
    StickerMessage, StickerSendMessage, LocationMessage, LocationSendMessage,
    ImageMessage, VideoMessage, AudioMessage, FileMessage,
    UnfollowEvent, FollowEvent, JoinEvent, LeaveEvent, BeaconEvent,
    FlexSendMessage, BubbleContainer, ImageComponent, BoxComponent,
    TextComponent, SpacerComponent, IconComponent, ButtonComponent,
    SeparatorComponent,
)

app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi('u/HC0JwWnT0bZ62dGFiU3ewK50M68nvOgXi6SMDCnJ/TK07kCMFEDbaMqtXGpYOCPgRAaNH27m66RXcGnAHizI8fXUj5mEChhd2ikqGQ+y9/AAvB0TUFjM6q79pBEPAIHjCv7ttW0o50W0woztRGsgdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('6b3652ce6db6b622101382eba4c3fd25')
#===========[ NOTE SAVER ]=======================
notes = {""}

# Post Request
@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    import random
    text = event.message.text #simplify for receove message
    sender = event.source.user_id #get usesenderr_id
    gid = event.source.sender_id #get group_id
    profile = line_bot_api.get_profile(sender)
    value = random.randint(1, 10)
    if text=="meme":
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='siap bos '+value+' mantap'))
    if text=="mail":
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='Kamu jahat mail'))
    if text=="djohan":
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='Kamu jahat djohan'))
    if text=="cuy":
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='oposeduh'))
    if text=="tyo":
        line_bot_api.reply_message(event.reply_token,ImageSendMessage(
    original_content_url='https://s0.bukalapak.com/img/0343005662/w-1000/Boneka_Anak_Jerapah_Imut_Menggemaskan.jpg',
    preview_image_url='https://s0.bukalapak.com/img/0343005662/w-1000/Boneka_Anak_Jerapah_Imut_Menggemaskan.jpg'
    ))
    if text=="bego":
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='Kamu jahat, '+profile.display_name+' :('))
        line_bot_api.leave_group(group_id)

    line_bot_api.reply_message(event.reply_token,TextSendMessage(text='Sorry '+profile.display_name+'\nAku g ngerti km ngomong apa\nKetik "cuy" klo bingung mo ngomong apa'))
        
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
