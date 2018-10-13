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
import requests, json

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

#INPUT DATA HEWAN
def inputHewan(Kode, Tipe, Hewan, Nama, Gender):
    r = requests.post("http://www.aditmasih.tk/api_irshad/insert.php", data={'Kode': Kode, 'Tipe': Tipe, 'Hewan': Hewan, 'Nama': Nama, 'Gender': Gender})
    data = r.json()

    flag = data['flag']
   
    if(flag == "1"):
        return 'Hewan '+Hewan+' Bernama '+Nama+' berhasil diimport dari hutan'
    elif(flag == "0"):
        return 'Hewan gk jadi masuk'

def showAll():
    r = requests.post("http://www.aditmasih.tk/api_irshad/all.php")
    data = r.json()

    flag = data['flag']
   
    if(flag == "1"):
        hasil = ""
        for i in range(0,len(data['digital_zoo'])):
            Kode = data['digital_zoo'][int(i)][0]
            Tipe = data['digital_zoo'][int(i)][2]
            Hewan = data['digital_zoo'][int(i)][4]
            # Nama = data['digital_zoo'][int(i)][6]
            # Gender = data['digital_zoo'][int(i)][8]
            hasil=hasil+str(i+1)
            # hasil=hasil+".\nKode : "
            hasil=hasil+Kode
            # hasil=hasil+"\nTipe : "
            hasil=hasil+Tipe
            # hasil=hasil+"\nHewan : "
            hasil=hasil+Hewan
            # hasil=hasil+"\nNama : "
            # hasil=hasil+Nama
            # hasil=hasil+"\nGender : "
            # hasil=hasil+Gender
            hasil=hasil+"\n"
        return hasil
    elif(flag == "0"):
        return 'Kebun binatang kosong'

#DELETE DATA HEWAN
def delHewan(Kode):
    r = requests.post("http://www.aditmasih.tk/api_irshad/delete.php", data={'Kode': Kode})
    data = r.json()

    flag = data['flag']
   
    if(flag == "1"):
        return 'Hewan dengan Kode '+Kode+' berhasil dilepas'
    elif(flag == "0"):
        return 'Hewannya emang ga ada :/'

# def updateHewan(nrpLama,nrp,nama,kosan):
#     URLmhs = "http://www.aditmasih.tk/api_irshad/show.php?nrp=" + nrpLama
#     r = requests.get(URLmhs)
#     data = r.json()
#     err = "data tidak ditemukan"
#     nrp_lama=nrpLama
#     flag = data['flag']
#     if(flag == "1"):
#         r = requests.post("http://www.aditmasih.tk/api_irshad/update.php", data={'nrp': nrp, 'nama': nama, 'kosan': kosan, 'nrp_lama':nrp_lama})
#         data = r.json()
#         flag = data['flag']

#         if(flag == "1"):
#             return 'Data '+nrp_lama+'berhasil diupdate\n'
#         elif(flag == "0"):
#             return 'Data gagal diupdate\n'

#     elif(flag == "0"):
#         return err
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
    
    data=text.split('-')
    if(data[0]=='tambah'):
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=inputHewan(data[1], data[2], data[3], data[4], data[5])))
    # elif(data[0]=='lihat'):
    #     line_bot_api.reply_message(event.reply_token, TextSendMessage(text=showHewan(data[1],data[2],data[3])))
    elif(data[0]=='hapus'):
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=delHewan(data[1])))
    elif(data[0]=='all'):
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=showAll()))
    # elif(data[0]=='ganti'):
    #     line_bot_api.reply_message(event.reply_token, TextSendMessage(text=updateHewan(data[1],data[2],data[3],data[4])))
    # elif(data[0]=='semwa'):
    #     line_bot_api.reply_message(event.reply_token, TextSendMessage(text=allsmhs()))
    # elif(data[0]=='menu'):
        # menu = "1. lihat-[nrp]\n2. tambah-[nrp]-[nama]-[kosan]\n3. hapus-[nrp]\n4. ganti-[nrp lama]-[nrp baru]-[nama baru]-[kosan baru]\n5. semwa"
        # line_bot_api.reply_message(event.reply_token, TextSendMessage(text=menu))
    
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
        line_bot_api.leave_room(event.source.room_id)
        #line_bot_api.leave_group(event.source.group_id)
    if text=="/bego":
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='yah, '+profile.display_name+' diboongi bot'))
    else:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='Sorry '+profile.display_name+'\nAku gk ngerti artinya "'+event.message.text+'" apa:('))

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
