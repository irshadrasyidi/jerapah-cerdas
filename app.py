from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *
import requests, json

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
    text = event.message.text #simplify for receove message
    sender = event.source.user_id #get usesenderr_id
    gid = event.source.sender_id #get group_id
    profile = line_bot_api.get_profile(sender)
    if text=="vivat":
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='hidup its 3x'))
    if text=="cuy":
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='opo?'))
    if text=="/shit1":
        line_bot_api.reply_message(event.reply_token,ImageSendMessage(
    original_content_url='https://media.keepo.me/20180306164707/800x532--28795197_1460633330725188_9160489402158820484_n.jpg',
    preview_image_url='https://media.keepo.me/20180306164707/800x532--28795197_1460633330725188_9160489402158820484_n.jpg'
    ))
    if text=="/shit2":
        line_bot_api.reply_message(event.reply_token,ImageSendMessage(
    original_content_url='https://i.pinimg.com/474x/64/f4/73/64f47325fd093120d8e16e7759fc5224.jpg',
    preview_image_url='https://i.pinimg.com/474x/64/f4/73/64f47325fd093120d8e16e7759fc5224.jpg'
    ))
    if text=="/shit3":
        line_bot_api.reply_message(event.reply_token,ImageSendMessage(
    original_content_url='https://3.bp.blogspot.com/-2bHJrd2yl7s/Wr3Sy2zDudI/AAAAAAAABNk/DKwqkIkvufUteDl_CQlvfV98EjDNeTJagCLcBGAs/s1600/IMG_20180327_221555.jpg',
    preview_image_url='https://3.bp.blogspot.com/-2bHJrd2yl7s/Wr3Sy2zDudI/AAAAAAAABNk/DKwqkIkvufUteDl_CQlvfV98EjDNeTJagCLcBGAs/s1600/IMG_20180327_221555.jpg'
    ))
    if text=="/shit4":
        line_bot_api.reply_message(event.reply_token,ImageSendMessage(
    original_content_url='http://ekspresia.com/wp-content/uploads/2018/03/19.jpg',
    preview_image_url='http://ekspresia.com/wp-content/uploads/2018/03/19.jpg'
    ))
    if text=="/begobgt":
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='Kamu jahat, '+profile.display_name+' :('))
        line_bot_api.leave_group(group_id)
    if text=="/bego":
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='yah, '+profile.display_name+' diboongi bot'))
    else:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='Sorry '+profile.display_name+'\nAku gk ngerti artinya "'+event.message.text+'" apa:('))

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
