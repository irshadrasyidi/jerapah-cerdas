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

# #INPUT DATA HEWAN
# def inputHewan(Kode, Tipe, Hewan, Nama, Gender):
#     r = requests.post("http://www.aditmasih.tk/api_irshad/insert.php", data={'Kode': Kode, 'Tipe': Tipe, 'Hewan': Hewan, 'Nama': Nama, 'Gender': Gender})
#     data = r.json()

#     flag = data['flag']

#     if(flag == "1"):
#         return 'Hewan '+Hewan+' Bernama '+Nama+' berhasil diimport dari hutan'
#     elif(flag == "0"):
#         return 'Hewan gk jadi masuk'

# def cariHewan(Kode):
#     URLhewan = "http://www.aditmasih.tk/api_irshad/show.php?Kode=" + Kode
#     r = requests.get(URLhewan)
#     data = r.json()
#     err = "Hewan tidak ditemukan"
    
#     flag = data['flag']
#     if(flag == "1"):
#         Kode = data['digital_zoo'][0]['Kode']
#         Tipe = data['digital_zoo'][0]['Tipe']
#         Hewan = data['digital_zoo'][0]['Hewan']
#         Nama = data['digital_zoo'][0]['Nama']
#         Gender = data['digital_zoo'][0]['Gender']

#         data= "Kode : "+Kode+"\nTipe : "+Tipe+"\nHewan : "+Hewan+"\nNama : "+Nama+"\nGender : "+Gender
#         return data

#     elif(flag == "0"):
#         return err

# def showAll():
#     r = requests.post("http://www.aditmasih.tk/api_irshad/all.php")
#     data = r.json()

#     flag = data['flag']

#     if(flag == "1"):
#         hasil = ""
#         for i in range(0,len(data['digital_zoo'])):
#             Kode = data['digital_zoo'][int(i)][0]
#             Tipe = data['digital_zoo'][int(i)][2]
#             Hewan = data['digital_zoo'][int(i)][4]
#             Nama = data['digital_zoo'][int(i)][6]
#             Gender = data['digital_zoo'][int(i)][8]
#             hasil=hasil+str(i+1)
#             hasil=hasil+".\nKode : "
#             hasil=hasil+Kode
#             hasil=hasil+"\nTipe : "
#             hasil=hasil+Tipe
#             hasil=hasil+"\nHewan : "
#             hasil=hasil+Hewan
#             hasil=hasil+"\nNama : "
#             hasil=hasil+Nama
#             hasil=hasil+"\nGender : "
#             hasil=hasil+Gender
#             hasil=hasil+"\n"
#         return hasil
#     elif(flag == "0"):
#         return 'Kebun binatang kosong'

# #DELETE DATA HEWAN
# def delHewan(Kode):
#     r = requests.post("http://www.aditmasih.tk/api_irshad/delete.php", data={'Kode': Kode})
#     data = r.json()

#     flag = data['flag']

#     if(flag == "1"):
#         return 'Hewan dengan Kode '+Kode+' berhasil dilepas'
#     elif(flag == "0"):
#         return 'Hewannya emang ga ada :/'

# #UPDATE DATA HEWAN
# def updateHewan(Kode_Lama, Kode, Tipe, Hewan, Nama, Gender):
#     URLhewan = "http://www.aditmasih.tk/api_irshad/show.php?Kode=" + Kode_Lama
#     r = requests.get(URLhewan)
#     data = r.json()
#     err = "Hewan tidak ditemukan"
#     KodeLama = Kode_Lama
#     flag = data['flag']
#     if(flag == "1"):
#         r = requests.post("http://www.aditmasih.tk/api_irshad/update.php", data={'KodeLama':KodeLama, 'Kode': Kode, 'Tipe': Tipe, 'Hewan': Hewan, 'Nama':Nama, 'Gender':Gender})
#         data = r.json()
#         flag = data['flag']

#         if(flag == "1"):
#             return 'Data '+KodeLama+' berhasil diupdate'
#         elif(flag == "0"):
#             return 'Data gagal diupdate'

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

    data = text.lower()
    data = text.split(' ')

    if text=="/menu":
        line_bot_api.reply_message(event.reply_token,TemplateSendMessage(
            alt_text='Carousel template',
            template=CarouselTemplate(
                columns=[
                    CarouselColumn(
                        thumbnail_image_url='https://i.ytimg.com/vi/mSFzdwxljog/maxresdefault.jpg',
                        title='Meme Shitpost',
                        text='My most valuable personal collection',
                        actions=[
                            PostbackAction(
                                label='Apa ini?',
                                text='Kamus Meme Shitpost',
                                data='action=buy&itemid=1'
                            ),
                            MessageAction(
                                label='Koleksi Meme',
                                text='Koleksi Meme'
                            ),
                            URIAction(
                                label='Promosi IG saya',
                                uri='https://www.instagram.com/irshadrasyidi/'
                            )
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url='http://pre13.deviantart.net/5dc4/th/pre/i/2012/359/9/6/bg_nature_stock_by_moonglowlilly-d5p5pe3.jpg',
                        title='Tuntunan Alam',
                        text='Anda bertanya, Alam menjawab',
                        actions=[
                            PostbackAction(
                                label='Ini apa?',
                                text='Tuntunan Alam',
                                data='action=buy&itemid=2'
                            ),
                            MessageAction(
                                label='Jompa-jampi',
                                text='Jompa-Jampi'
                            ),
                            URIAction(
                                label='Promosi Twitter saya',
                                uri='https://twitter.com/didotbrodot'
                            )
                        ]
                    )
                ]
            )
        ))
    if text=="/kategori-meme":
        line_bot_api.reply_message(event.reply_token,TemplateSendMessage(
            alt_text='ImageCarousel template',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://asset.kompas.com/crop/0x2:960x642/750x500/data/photo/2018/03/06/2717904116.jpg',
                        action=PostbackAction(
                            label='Anjing',
                            text='/meme-anjing',
                            data='action=buy&itemid=1'
                        )
                    ),
                    ImageCarouselColumn(
                        image_url='https://forums.lbsg.net/uploads/default/original/2X/7/7c14a99d7de45e3d691ed9cf05deec1ec69d0d78.png',
                        action=PostbackAction(
                            label='Pun',
                            text='/meme-pun',
                            data='action=buy&itemid=2'
                        )
                    ),
                    ImageCarouselColumn(
                        image_url='https://3.bp.blogspot.com/-3DCApIDpPg8/WadDwhqKGlI/AAAAAAAALVQ/cLo2R5M3C3AHmdC7WH7YZr-q_mwYu_0BACLcBGAs/s1600/kak-seto.jpg',
                        action=PostbackAction(
                            label='Kak Seto',
                            text='/meme-seto',
                            data='action=buy&itemid=3'
                        )
                    ),
                    # ImageCarouselColumn(
                    #     image_url='https://s.kaskus.id/images/2018/03/12/7034635_201803120552320355.jpg',
                    #     action=PostbackAction(
                    #         label='WikiHow',
                    #         text='/meme-wikihow',
                    #         data='action=buy&itemid=4'
                    #     )
                    # ),
                    # ImageCarouselColumn(
                    #     image_url='http://tps2u.com/wp-content/uploads/2017/11/OTHERS-1.jpg',
                    #     action=PostbackAction(
                    #         label='Others',
                    #         text='/meme-others',
                    #         data='action=buy&itemid=5'
                    #     )
                    # )
                ]
            )
        ))
    if text=="/koleksi-meme":
        kamus="kamus shitpost :\n1. /meme1 : Kecewa\n2. /meme2 : Thanks\n1. /meme1 : Kecewa\n2. /meme2 : Thanks\n1. /meme1 : Kecewa\n2. /meme2 : Thanks\n1. /meme1 : Kecewa\n2. /meme2 : Thanks\n1. /meme1 : Kecewa\n2. /meme2 : Thanks\n1. /meme1 : Kecewa\n2. /meme2 : Thanks\n1. /meme1 : Kecewa\n2. /meme2 : Thanks\n1. /meme1 : Kecewa\n2. /meme2 : Thanks\n1. /meme1 : Kecewa\n2. /meme2 : Thanks\n1. /meme1 : Kecewa\n2. /meme2 : Thanks\n1. /meme1 : Kecewa\n2. /meme2 : Thanks\n1. /meme1 : Kecewa\n2. /meme2 : Thanks\n1. /meme1 : Kecewa\n2. /meme2 : Thanks\n1. /meme1 : Kecewa\n2. /meme2 : Thanks\n1. /meme1 : Kecewa\n2. /meme2 : Thanks\n1. /meme1 : Kecewa\n2. /meme2 : Thanks\n1. /meme1 : Kecewa\n2. /meme2 : Thanks\n1. /meme1 : Kecewa\n2. /meme2 : Thanks\n1. /meme1 : Kecewa\n2. /meme2 : Thanks\n1. /meme1 : Kecewa\n2. /meme2 : Thanks\n1. /meme1 : Kecewa\n2. /meme2 : Thanks\n1. /meme1 : Kecewa\n2. /meme2 : Thanks\n1. /meme1 : Kecewa\n2. /meme2 : Thanks\n1. /meme1 : Kecewa\n2. /meme2 : Thanks\n1. /meme1 : Kecewa\n2. /meme2 : Thanks\n1. /meme1 : Kecewa\n2. /meme2 : Thanks\n1. /meme1 : Kecewa\n2. /meme2 : Thanks\n1. /meme1 : Kecewa\n2. /meme2 : Thanks\n1. /meme1 : Kecewa\n2. /meme2 : Thanks"
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=kamus))
#ANJING
    if text=="/meme-anjing":
        kamus="Kategori Anjing :\n1. /anjing-ga-jelas\n2. /anjing-ga-nyambung\n3. /anjing-ngegas\n4. /anjing-tolol\n5. /anjing-semua\n6. /anjing-jangkrik\n7. /anjing-kok\n8. /anjing-bawel\n9. /anjing-baper\n10. /anjing-kalem"
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=kamus))
    
    #1
    if text=="/anjing-ga-jelas" or text=="ga jelas":
        line_bot_api.reply_message(event.reply_token,ImageSendMessage(
    original_content_url='https://cdn.brilio.net/news/2018/04/05/141154/760223-meme-anjing.jpg',
    preview_image_url='https://cdn.brilio.net/news/2018/04/05/141154/760223-meme-anjing.jpg'
    ))
    #2
    if text=="/anjing-ga-nyambung" or text=="ga nyambung":
        line_bot_api.reply_message(event.reply_token,ImageSendMessage(
    original_content_url='https://pics.me.me/anjing-kaga-nyambung-31476214.png',
    preview_image_url='https://pics.me.me/anjing-kaga-nyambung-31476214.png'
    ))
    #3
    if text=="/anjing-ngegas" or text=="ngegas":
        line_bot_api.reply_message(event.reply_token,ImageSendMessage(
    original_content_url='https://img.duniaku.net/2018/03/1521427491-anjing-ngegas.jpg',
    preview_image_url='https://img.duniaku.net/2018/03/1521427491-anjing-ngegas.jpg'
    ))
    #4
    if text=="/anjing-tolol" or text=="tolol":
        line_bot_api.reply_message(event.reply_token,ImageSendMessage(
    original_content_url='https://pbs.twimg.com/media/DYLq_4fU0AA9b-B.jpg',
    preview_image_url='https://pbs.twimg.com/media/DYLq_4fU0AA9b-B.jpg'
    ))
    #5
    if text=="/anjing-semua" or text=="asu kabeh":
        line_bot_api.reply_message(event.reply_token,ImageSendMessage(
    original_content_url='https://1.bp.blogspot.com/-nsYjWy0W4AU/VArRtVc7MxI/AAAAAAAAM8k/SnNZKZxfNmA/s1600/bm-image-789062.jpeg',
    preview_image_url='https://1.bp.blogspot.com/-nsYjWy0W4AU/VArRtVc7MxI/AAAAAAAAM8k/SnNZKZxfNmA/s1600/bm-image-789062.jpeg'
    ))
    #6
    if text=="/anjing-jangkrik" or text=="jangkrik":
        line_bot_api.reply_message(event.reply_token,ImageSendMessage(
    original_content_url='https://pbs.twimg.com/media/DX95-GUUQAUIT7i.jpg',
    preview_image_url='https://pbs.twimg.com/media/DX95-GUUQAUIT7i.jpg'
    ))
    #7
    if text=="/anjing-kok" or text=="kok anjing":
        line_bot_api.reply_message(event.reply_token,ImageSendMessage(
    original_content_url='https://pbs.twimg.com/media/DYLLvU3VAAABy7F.jpg',
    preview_image_url='https://pbs.twimg.com/media/DYLLvU3VAAABy7F.jpg'
    ))
    #8
    if text=="/anjing-bawel" or text=="bawel":
        line_bot_api.reply_message(event.reply_token,ImageSendMessage(
    original_content_url='https://s.kaskus.id/images/2018/03/14/7034635_201803140545070870.jpg',
    preview_image_url='https://s.kaskus.id/images/2018/03/14/7034635_201803140545070870.jpg'
    ))
    #9
    if text=="/anjing-baper" or text=="baper":
        line_bot_api.reply_message(event.reply_token,ImageSendMessage(
    original_content_url='https://img.duniaku.net/2018/03/1521427445-anjing-baper.jpg',
    preview_image_url='https://img.duniaku.net/2018/03/1521427445-anjing-baper.jpg'
    ))
    #10
    if text=="/anjing-kalem" or text=="kalem":
        line_bot_api.reply_message(event.reply_token,ImageSendMessage(
    original_content_url='https://scontent-atl3-1.cdninstagram.com/vp/a5162fe74fd29170ddbbfbba71863c1b/5C5537BA/t51.2885-15/e35/29088954_1860060620959017_6436073020644655104_n.jpg',
    preview_image_url='https://scontent-atl3-1.cdninstagram.com/vp/a5162fe74fd29170ddbbfbba71863c1b/5C5537BA/t51.2885-15/e35/29088954_1860060620959017_6436073020644655104_n.jpg'
    ))

#PUN
    if text=="/meme-pun":
        kamus="Kategori Pun :\n1. /pun-asu\n2. /pun-bawel\n3. /pun-bego\n4. /pun-ngegas\n5. /pun-gas\n6. /pun-gawat\n7. /pun-gelut\n8. /pun-goblok\n9. /pun-ikan-goblok\n10. /pun-joanchok\n11. /pun-kancil\n12. /pun-kecewa\n13. /pun-keren\n14. /pun-kocak\n15. /pun-lodeh\n16. /pun-mager\n17. /pun-pinter\n18. /pun-sabi\n19. /pun-sekip\n20. /pun-siyap\n21. /pun-yamaap"
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=kamus))
    
    #2
    if text=="/pun-bawel":
        line_bot_api.reply_message(event.reply_token,ImageSendMessage(
    original_content_url='https://1.bp.blogspot.com/-AHXu8nVDgww/Wr3YdzZvCVI/AAAAAAAABPg/AO7Mnycr_oQx3bdzboe6qyW8WyqjynfXACLcBGAs/s1600/IMG_20180327_222109.jpg',
    preview_image_url='https://1.bp.blogspot.com/-AHXu8nVDgww/Wr3YdzZvCVI/AAAAAAAABPg/AO7Mnycr_oQx3bdzboe6qyW8WyqjynfXACLcBGAs/s1600/IMG_20180327_222109.jpg'
    ))
    #3
    if text=="/pun-bego":
        line_bot_api.reply_message(event.reply_token,ImageSendMessage(
    original_content_url='https://image.shutterstock.com/image-vector/error-404-page-not-found-450w-1027982980.jpg',
    preview_image_url='https://image.shutterstock.com/image-vector/error-404-page-not-found-450w-1027982980.jpg'
    ))
    #4
    if text=="/pun-ngegas":
        line_bot_api.reply_message(event.reply_token,ImageSendMessage(
    original_content_url='https://image.shutterstock.com/image-vector/error-404-page-not-found-450w-1027982980.jpg',
    preview_image_url='https://image.shutterstock.com/image-vector/error-404-page-not-found-450w-1027982980.jpg'
    ))
    #5
    if text=="/pun-gas":
        line_bot_api.reply_message(event.reply_token,ImageSendMessage(
    original_content_url='https://image.shutterstock.com/image-vector/error-404-page-not-found-450w-1027982980.jpg',
    preview_image_url='https://image.shutterstock.com/image-vector/error-404-page-not-found-450w-1027982980.jpg'
    ))
    #6
    if text=="/pun-gawat":
        line_bot_api.reply_message(event.reply_token,ImageSendMessage(
    original_content_url='https://image.shutterstock.com/image-vector/error-404-page-not-found-450w-1027982980.jpg',
    preview_image_url='https://image.shutterstock.com/image-vector/error-404-page-not-found-450w-1027982980.jpg'
    ))
    #6
    if text=="/pun-gelut":
        line_bot_api.reply_message(event.reply_token,ImageSendMessage(
    original_content_url='https://pics.me.me/gelut-29735709.png',
    preview_image_url='https://pics.me.me/gelut-29735709.png'
    ))
    #6
    if text=="/pun-goblok":
        line_bot_api.reply_message(event.reply_token,ImageSendMessage(
    original_content_url='https://image.shutterstock.com/image-vector/error-404-page-not-found-450w-1027982980.jpg',
    preview_image_url='https://image.shutterstock.com/image-vector/error-404-page-not-found-450w-1027982980.jpg'
    ))
    #7
    if text=="/pun-ikan-goblok":
        line_bot_api.reply_message(event.reply_token,ImageSendMessage(
    original_content_url='https://image.shutterstock.com/image-vector/error-404-page-not-found-450w-1027982980.jpg',
    preview_image_url='https://image.shutterstock.com/image-vector/error-404-page-not-found-450w-1027982980.jpg'
    ))
    #8
    if text=="/pun-joanchok":
        line_bot_api.reply_message(event.reply_token,ImageSendMessage(
    original_content_url='https://image.shutterstock.com/image-vector/error-404-page-not-found-450w-1027982980.jpg',
    preview_image_url='https://image.shutterstock.com/image-vector/error-404-page-not-found-450w-1027982980.jpg'
    ))
    #9
    if text=="/pun-kancil":
        line_bot_api.reply_message(event.reply_token,ImageSendMessage(
    original_content_url='https://image.shutterstock.com/image-vector/error-404-page-not-found-450w-1027982980.jpg',
    preview_image_url='https://image.shutterstock.com/image-vector/error-404-page-not-found-450w-1027982980.jpg'
    ))
    #10
    if text=="/pun-kecewa":
        line_bot_api.reply_message(event.reply_token,ImageSendMessage(
    original_content_url='https://pics.me.me/kecewa-31619297.png',
    preview_image_url='https://pics.me.me/kecewa-31619297.png'
    ))
    #11
    if text=="/pun-keren":
        line_bot_api.reply_message(event.reply_token,ImageSendMessage(
    original_content_url='http://gituaja.com/wp-content/uploads/2018/04/Pelesetan-Gambar-Yang-Super-Receh-Tapi-Ketika-Dibaca-Kalian-Mengerti-GituAja-21.jpg',
    preview_image_url='http://gituaja.com/wp-content/uploads/2018/04/Pelesetan-Gambar-Yang-Super-Receh-Tapi-Ketika-Dibaca-Kalian-Mengerti-GituAja-21.jpg'
    ))
    #12
    if text=="/pun-kocak":
        line_bot_api.reply_message(event.reply_token,ImageSendMessage(
    original_content_url='https://image.shutterstock.com/image-vector/error-404-page-not-found-450w-1027982980.jpg',
    preview_image_url='https://image.shutterstock.com/image-vector/error-404-page-not-found-450w-1027982980.jpg'
    ))
    #13
    if text=="/pun-lodeh":
        line_bot_api.reply_message(event.reply_token,ImageSendMessage(
    original_content_url='https://image.shutterstock.com/image-vector/error-404-page-not-found-450w-1027982980.jpg',
    preview_image_url='https://image.shutterstock.com/image-vector/error-404-page-not-found-450w-1027982980.jpg'
    ))
    #14
    if text=="/pun-mager":
        line_bot_api.reply_message(event.reply_token,ImageSendMessage(
    original_content_url='https://image.shutterstock.com/image-vector/error-404-page-not-found-450w-1027982980.jpg',
    preview_image_url='https://image.shutterstock.com/image-vector/error-404-page-not-found-450w-1027982980.jpg'
    ))
    #15
    if text=="/pun-pinter":
        line_bot_api.reply_message(event.reply_token,ImageSendMessage(
    original_content_url='https://image.shutterstock.com/image-vector/error-404-page-not-found-450w-1027982980.jpg',
    preview_image_url='https://image.shutterstock.com/image-vector/error-404-page-not-found-450w-1027982980.jpg'
    ))
    #16
    if text=="/pun-sabi":
        line_bot_api.reply_message(event.reply_token,ImageSendMessage(
    original_content_url='https://image.shutterstock.com/image-vector/error-404-page-not-found-450w-1027982980.jpg',
    preview_image_url='https://image.shutterstock.com/image-vector/error-404-page-not-found-450w-1027982980.jpg'
    ))
    #17
    if text=="/pun-sekip":
        line_bot_api.reply_message(event.reply_token,ImageSendMessage(
    original_content_url='https://4.bp.blogspot.com/-TXgBZ19sxHs/Wr3bhYlQy6I/AAAAAAAABPs/vbC_Be9GFmsWrhytSZXd90D9DaQymyhdQCLcBGAs/s1600/IMG_20180327_222132.jpg',
    preview_image_url='https://4.bp.blogspot.com/-TXgBZ19sxHs/Wr3bhYlQy6I/AAAAAAAABPs/vbC_Be9GFmsWrhytSZXd90D9DaQymyhdQCLcBGAs/s1600/IMG_20180327_222132.jpg'
    ))
    #18
    if text=="/pun-siyap":
        line_bot_api.reply_message(event.reply_token,ImageSendMessage(
    original_content_url='https://www.teknosaurus.com/wp-content/uploads/2018/03/sayap-e1521330529574.jpg',
    preview_image_url='https://www.teknosaurus.com/wp-content/uploads/2018/03/sayap-e1521330529574.jpg'
    ))
    #19
    if text=="/pun-yamaap":
        line_bot_api.reply_message(event.reply_token,ImageSendMessage(
    original_content_url='http://gituaja.com/wp-content/uploads/2018/04/Pelesetan-Gambar-Yang-Super-Receh-Tapi-Ketika-Dibaca-Kalian-Mengerti-GituAja-21.jpg',
    preview_image_url='http://gituaja.com/wp-content/uploads/2018/04/Pelesetan-Gambar-Yang-Super-Receh-Tapi-Ketika-Dibaca-Kalian-Mengerti-GituAja-21.jpg'
    ))
    #20
    if text=="/pun-thanks":
        line_bot_api.reply_message(event.reply_token,ImageSendMessage(
    original_content_url='https://3.bp.blogspot.com/-2bHJrd2yl7s/Wr3Sy2zDudI/AAAAAAAABNk/DKwqkIkvufUteDl_CQlvfV98EjDNeTJagCLcBGAs/s1600/IMG_20180327_221555.jpg',
    preview_image_url='https://3.bp.blogspot.com/-2bHJrd2yl7s/Wr3Sy2zDudI/AAAAAAAABNk/DKwqkIkvufUteDl_CQlvfV98EjDNeTJagCLcBGAs/s1600/IMG_20180327_221555.jpg'
    ))
    #21
    if text=="/pun-kampret":
        line_bot_api.reply_message(event.reply_token,ImageSendMessage(
    original_content_url='https://cdn2.boombastis.com/wp-content/uploads/2018/03/7kampret.jpeg',
    preview_image_url='https://cdn2.boombastis.com/wp-content/uploads/2018/03/7kampret.jpeg '
    ))
    
    
    
    
    
    
    
    if text=="/meme-wikihow":
        kamus="Kategori Wikihow :\n1. /anjing-ga-jelas\n2. /anjing-ga-nyambung\n3. /anjing-ngegas\n4. /anjing-tolol\n5. /anjing-semua\n6. /anjing-asu\n7. /anjing-ga-sopan\n8. /anjing-ga-jelas"
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=kamus))
    if text=="/meme-seto":
        kamus="Kategori Seto :\n1. /anjing-ga-jelas\n2. /anjing-ga-nyambung\n3. /anjing-ngegas\n4. /anjing-tolol\n5. /anjing-semua\n6. /anjing-asu\n7. /anjing-ga-sopan\n8. /anjing-ga-jelas"
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=kamus))
    
        
#KERANG AJAIB
    
    if(data[0]=='tambah'):
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='asd'))
    elif(data[0]=='lihat'):
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='qwe'))
#tuntunan-alam
    if(data[0]=='apa' or data[0]=='opo' or data[0]=='kuy' or data[0]='yuk' or data[0]='ayo' or data[0]=='ayok' or data[0]=='masak' or data[0]='mosok' or data[0]=='ayok' or data[0]=='ayo' or data[0]='mosok'):
        n=random.randint(0, 18)
        hasil=[""]
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=hasil[a]))

    if text=="vivat":
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='hidup its!'))
    if text=="cuy":
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='opo?'))
    if text=="/begobgt":
        if isinstance(event.source, SourceGroup):
            line_bot_api.reply_message(event.reply_token,TextSendMessage(text=profile.display_name+'jahat :('))
            line_bot_api.leave_room(event.source.group_id)
        elif isinstance(event.source, SourceRoom):
            line_bot_api.reply_message(event.reply_token,TextSendMessage(text=profile.display_name+'jahat :('))
            line_bot_api.leave_room(event.source.room_id)
    if text=="/bye":
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='gamau keluar wek!'))

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
