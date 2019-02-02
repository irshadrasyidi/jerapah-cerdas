from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *
import requests, json

from random import randint

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
    rawText = event.message.text
    text = rawText.lower().strip()
    sender = event.source.user_id
    gid = event.source.sender_id
    profile = line_bot_api.get_profile(sender)

    data=text.split(' ')

    if text=="/menu":
        line_bot_api.reply_message(event.reply_token,TemplateSendMessage(
            alt_text='Carousel template',
            template=CarouselTemplate(
                columns=[
                    CarouselColumn(
                        thumbnail_image_url='https://example.com/item1.jpg',
                        title='Meme Shitpost',
                        text='Koleksi Personal Paling Berharga',
                        actions=[
                            PostbackAction(
                                label='Apa ini?',
                                text='kamus meme',
                                data='action=buy&itemid=1'
                            ),
                            MessageAction(
                                label='Kategori Meme',
                                text='kategori meme'
                            ),
                            URIAction(
                                label='Akun Twitter saya',
                                uri='https://twitter.com/didotbrodot'
                            )
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://static.family.ca/rendition/17001/1058/595',
                        title='Sound of Nature',
                        text='Anda bertanya, alam menjawab',
                        actions=[
                            PostbackAction(
                                label='Ini apa?',
                                text='Tuntunan Alam',
                                data='action=buy&itemid=2'
                            ),
                            MessageAction(
                                label='Jompa-Jampi',
                                text='Jompa-Jampi'
                            ),
                            URIAction(
                                label='Akun Twitter saya',
                                uri='https://twitter.com/didotbrodot'
                            )
                        ]
                    )
                ]
            )
        ))

    if text=="kamus meme":
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='Sebuah koleksi pribadi berisikan meme-meme yang dapat memberi warna dalam bercakap online'))
    if text=="kategori meme":
        line_bot_api.reply_message(event.reply_token,TemplateSendMessage(
            alt_text='ImageCarousel template',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        #image_url='https://asset.kompas.com/crop/0x2:960x642/750x500/data/photo/2018/03/06/2717904116.jpg',
                        image_url='https://i.imgur.com/ywKZuaB.gifv',
                        action=PostbackAction(
                            label='Anjing',
                            text='meme anjing',
                            data='action=buy&itemid=1'
                        )
                    ),
                    ImageCarouselColumn(
                        image_url='https://forums.lbsg.net/uploads/default/original/2X/7/7c14a99d7de45e3d691ed9cf05deec1ec69d0d78.png',
                        action=PostbackAction(
                            label='Pun',
                            text='meme pun',
                            data='action=buy&itemid=2'
                        )
                    ),
                    ImageCarouselColumn(
                        image_url='https://s.kaskus.id/images/2018/03/12/7034635_201803120552320355.jpg',
                        action=PostbackAction(
                            label='WikiHow',
                            text='meme wikihow',
                            data='action=buy&itemid=3'
                        )
                    ),
                    ImageCarouselColumn(
                        image_url='https://i.imgur.com/SBUbHHN.gif',
                        action=PostbackAction(
                            label='Others',
                            text='meme etcetera',
                            data='action=buy&itemid=4'
                        )
                    )
                ]
            )
        ))

#MULT CHOICE
    #BAWEL
    #ANJING 8, PUN 2
    if text=="bawel" or data[0]=="bawel" or data[1]=="bawel":
        a = random.randint(0, 1)
        b = ["https://s.kaskus.id/images/2018/03/14/7034635_201803140545070870.jpg", "https://1.bp.blogspot.com/-AHXu8nVDgww/Wr3YdzZvCVI/AAAAAAAABPg/AO7Mnycr_oQx3bdzboe6qyW8WyqjynfXACLcBGAs/s1600/IMG_20180327_222109.jpg"]
        line_bot_api.reply_message(event.reply_token,ImageSendMessage(
    original_content_url=b[a],
    preview_image_url=b[a]
    ))

    #BODOH
    #WIKIHOW 9, WIKIHOW 10
    if text=="bodoh" or data[0]=="bodoh" or data[1]=="bodoh" or data[0]=="bodo" or data[1]=="bodo":
        a = random.randint(0, 1)
        b = ["https://ktawa.com/wp-content/uploads/2018/05/2761997_201803120735020920.jpg", "https://ktawa.com/wp-content/uploads/2018/09/DXgqnNRVwAA-_6F.jpg"]
        line_bot_api.reply_message(event.reply_token,ImageSendMessage(
    original_content_url=b[a],
    preview_image_url=b[a]
    ))

#ANJING
    if text=="meme anjing":
        kamus="Kategori Anjing :\n1. /anjing-ga-jelas :\n'ga jelas', 'gaje', 'geje', 'gj'\n2. /anjing-ga-nyambung :\n'ga nyambung'\n3. /anjing-ngegas :\n'ngegas'\n4. /anjing-tolol :\n'tolol'\n5. /anjing-semua :\n'asu kabeh'\n6. /anjing-jangkrik :\n'jangkrik'\n7. /anjing-kok :\n'kok anjing'\n8. /anjing-bawel :\n'bawel'\n9. /anjing-baper :\n'baper'\n10. /anjing-kalem :\n'kalem'"
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=kamus))
    
    #1 MULT CHOICE
    if text=="/anjing-ga-jelas" or text=="ga jelas" or text=="g jelas" or text=="gaje" or text=="geje" or text=="gj" or data[0]=="gaje" or data[0]=="geje" or data[0]=="gj" or data[1]=="gaje" or data[1]=="geje" or data[1]=="gj":
        line_bot_api.reply_message(event.reply_token,ImageSendMessage(
    original_content_url='https://cdn.brilio.net/news/2018/04/05/141154/760223-meme-anjing.jpg',
    preview_image_url='https://cdn.brilio.net/news/2018/04/05/141154/760223-meme-anjing.jpg'
    ))
    #2
    if text=="/anjing-ga-nyambung" or text=="ga nyambung" or text=="g nyambung":
        line_bot_api.reply_message(event.reply_token,ImageSendMessage(
    original_content_url='https://pics.me.me/anjing-kaga-nyambung-31476214.png',
    preview_image_url='https://pics.me.me/anjing-kaga-nyambung-31476214.png'
    ))
    #3 MULT CHOICE
    if text=="/anjing-ngegas" or text=="ngegas" or data[0]=="ngegas" or data[1]=="ngegas":
        line_bot_api.reply_message(event.reply_token,ImageSendMessage(
    original_content_url='https://img.duniaku.net/2018/03/1521427491-anjing-ngegas.jpg',
    preview_image_url='https://img.duniaku.net/2018/03/1521427491-anjing-ngegas.jpg'
    ))
    #4
    if text=="tolol" or data[0]=="tolol" or data[1]=="tolol":
        line_bot_api.reply_message(event.reply_token,ImageSendMessage(
    original_content_url='https://pbs.twimg.com/media/DYLq_4fU0AA9b-B.jpg',
    preview_image_url='https://pbs.twimg.com/media/DYLq_4fU0AA9b-B.jpg'
    ))
    #5
    if text=="/anjing-semua" or text=="asu kabeh" or text=="anjing semua":
        line_bot_api.reply_message(event.reply_token,ImageSendMessage(
    original_content_url='https://1.bp.blogspot.com/-nsYjWy0W4AU/VArRtVc7MxI/AAAAAAAAM8k/SnNZKZxfNmA/s1600/bm-image-789062.jpeg',
    preview_image_url='https://1.bp.blogspot.com/-nsYjWy0W4AU/VArRtVc7MxI/AAAAAAAAM8k/SnNZKZxfNmA/s1600/bm-image-789062.jpeg'
    ))
    #6
    if text=="/anjing-jangkrik" or text=="jangkrik" or data[0]=="jangkrik" or data[1]=="jangkrik":
        line_bot_api.reply_message(event.reply_token,ImageSendMessage(
    original_content_url='https://pbs.twimg.com/media/DX95-GUUQAUIT7i.jpg',
    preview_image_url='https://pbs.twimg.com/media/DX95-GUUQAUIT7i.jpg'
    ))
    #7
    if text=="/anjing-kok" or text=="kok anjing" or text=="koq anjg":
        line_bot_api.reply_message(event.reply_token,ImageSendMessage(
    original_content_url='https://pbs.twimg.com/media/DYLLvU3VAAABy7F.jpg',
    preview_image_url='https://pbs.twimg.com/media/DYLLvU3VAAABy7F.jpg'
    ))
    #8 MULT CHOICE
    if text=="/anjing-bawel":
        line_bot_api.reply_message(event.reply_token,ImageSendMessage(
    original_content_url='https://s.kaskus.id/images/2018/03/14/7034635_201803140545070870.jpg',
    preview_image_url='https://s.kaskus.id/images/2018/03/14/7034635_201803140545070870.jpg'
    ))
    #9 IMG LOST
    if text=="/anjing-baper" or text=="baper" or data[0]=="baper" or data[1]=="baper":
        line_bot_api.reply_message(event.reply_token,ImageSendMessage(
    original_content_url='https://img.duniaku.net/2018/03/1521427445-anjing-baper.jpg',
    preview_image_url='https://img.duniaku.net/2018/03/1521427445-anjing-baper.jpg'
    ))
    #10
    if text=="/anjing-kalem" or text=="kalem" or data[0]=="kalem" or data[1]=="kalem":
        line_bot_api.reply_message(event.reply_token,ImageSendMessage(
    original_content_url='https://scontent-atl3-1.cdninstagram.com/vp/a5162fe74fd29170ddbbfbba71863c1b/5C5537BA/t51.2885-15/e35/29088954_1860060620959017_6436073020644655104_n.jpg',
    preview_image_url='https://scontent-atl3-1.cdninstagram.com/vp/a5162fe74fd29170ddbbfbba71863c1b/5C5537BA/t51.2885-15/e35/29088954_1860060620959017_6436073020644655104_n.jpg'
    ))



#PUN
    if text=="meme pun":
        kamus="Kategori Pun :\n1. /pun-bawel\n2. /pun-bego\n3. /pun-ngegas\n4. /pun-gas\n5. /pun-gawat\n6. /pun-ikan-goblok\n7. /pun-gelut\n8. /pun-bubar\n9. /pun-ikan-goblok\n11. /pun-kancil\n12. /pun-kecewa\n13. /pun-keren\n14. /pun-kocak\n15. /pun-lodeh\n16. /pun-mager\n17. /pun-pinter\n18. /pun-sabi\n19. /pun-sekip\n20. /pun-siyap\n21. /pun-thanks\n22. /pun-kampret"
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=kamus))
    
    #2 MULT CHOICE
    if text=="/pun-bawel":
        line_bot_api.reply_message(event.reply_token,ImageSendMessage(
    original_content_url='https://1.bp.blogspot.com/-AHXu8nVDgww/Wr3YdzZvCVI/AAAAAAAABPg/AO7Mnycr_oQx3bdzboe6qyW8WyqjynfXACLcBGAs/s1600/IMG_20180327_222109.jpg',
    preview_image_url='https://1.bp.blogspot.com/-AHXu8nVDgww/Wr3YdzZvCVI/AAAAAAAABPg/AO7Mnycr_oQx3bdzboe6qyW8WyqjynfXACLcBGAs/s1600/IMG_20180327_222109.jpg'
    ))
    #3 MULT CHOICE
    if text=="/pun-bego" or data[0]=="bego" or data[1]=="bego":
        line_bot_api.reply_message(event.reply_token,ImageSendMessage(
    original_content_url='https://pbs.twimg.com/media/DYaIxpdU0AE2UcO.jpg',
    preview_image_url='https://pbs.twimg.com/media/DYaIxpdU0AE2UcO.jpg'
    ))
    #4 MULT CHOICE
    if text=="/pun-ngegas" or data[0]=="ngegas" or data[1]=="ngegas":
        line_bot_api.reply_message(event.reply_token,ImageSendMessage(
    original_content_url='https://s.kaskus.id/images/2017/10/07/9824467_201710070650410306.jpg',
    preview_image_url='https://s.kaskus.id/images/2017/10/07/9824467_201710070650410306.jpg'
    ))
    #5 MULT CHOICE
    if text=="/pun-gas" or data[0]=="gas" or data[1]=="gas":
        line_bot_api.reply_message(event.reply_token,ImageSendMessage(
    original_content_url='https://s.kaskus.id/images/2017/05/01/9437462_201705010152380796.jpg',
    preview_image_url='https://s.kaskus.id/images/2017/05/01/9437462_201705010152380796.jpg'
    ))
    #6
    if text=="/pun-gawat" or text=="gawat" or data[0]=="gawat" or data[1]=="gawat":
        line_bot_api.reply_message(event.reply_token,ImageSendMessage(
    original_content_url='https://em.wattpad.com/a597dfd0d5b0115078e72028c89b42f412c398e2/68747470733a2f2f73332e616d617a6f6e6177732e636f6d2f776174747061642d6d656469612d736572766963652f53746f7279496d6167652f4c346e547651464b426c66765a513d3d2d3532352e313531613331396163343031306232343335303035353539383537312e6a7067?s=fit&w=720&h=720',
    preview_image_url='https://em.wattpad.com/a597dfd0d5b0115078e72028c89b42f412c398e2/68747470733a2f2f73332e616d617a6f6e6177732e636f6d2f776174747061642d6d656469612d736572766963652f53746f7279496d6167652f4c346e547651464b426c66765a513d3d2d3532352e313531613331396163343031306232343335303035353539383537312e6a7067?s=fit&w=720&h=720'
    ))
    #6
    if text=="/pun-gelut" or data[0]=="gelut" or data[1]=="gelut":
        line_bot_api.reply_message(event.reply_token,ImageSendMessage(
    original_content_url='https://pics.me.me/gelut-29735709.png',
    preview_image_url='https://pics.me.me/gelut-29735709.png'
    ))
    #7 MULT CHOICE
    if text=="/pun-ikan-goblok" or data[0]=="goblok" or data[1]=="goblok" or data[0]=="gblk" or data[1]=="gblk" or data[0]=="goblog" or data[1]=="goblog" or data[0]=="gblg" or data[1]=="gblg":
        line_bot_api.reply_message(event.reply_token,ImageSendMessage(
    original_content_url='https://i.pinimg.com/236x/d2/55/46/d25546911ab75e65de5d0e5b6f267c5c.jpg',
    preview_image_url='https://i.pinimg.com/236x/d2/55/46/d25546911ab75e65de5d0e5b6f267c5c.jpg'
    ))
    #8
    if text=="/pun-bubar" or data[0]=="bubar" or data[0]=="leren" or data[1]=="bubar" or data[1]=="leren":
        line_bot_api.reply_message(event.reply_token,ImageSendMessage(
    original_content_url='https://pbs.twimg.com/media/DY9OLOLVwAEadK7.jpg',
    preview_image_url='https://pbs.twimg.com/media/DY9OLOLVwAEadK7.jpg'
    ))
    #9
    if text=="/pun-kancil" or data[0]=="kancil" or data[1]=="kancil":
        line_bot_api.reply_message(event.reply_token,ImageSendMessage(
    original_content_url='https://pbs.twimg.com/media/DjSIfjUVAAAX5WQ.jpg:large',
    preview_image_url='https://pbs.twimg.com/media/DjSIfjUVAAAX5WQ.jpg:large'
    ))
    #10
    if text=="/pun-kecewa" or data[0]=="kecewa" or data[1]=="kecewa":
        line_bot_api.reply_message(event.reply_token,ImageSendMessage(
    original_content_url='https://pics.me.me/kecewa-31619297.png',
    preview_image_url='https://pics.me.me/kecewa-31619297.png'
    ))
    #11
    if text=="/pun-keren" or data[0]=="keren" or data[0]=="cool" or data[0]=="kewl" or data[1]=="keren" or data[1]=="cool" or data[1]=="kewl":
        line_bot_api.reply_message(event.reply_token,ImageSendMessage(
    original_content_url='https://media.keepo.me/20180306164724/511x288--28872329_1460633664058488_1580595060448431199_n.jpg',
    preview_image_url='https://media.keepo.me/20180306164724/511x288--28872329_1460633664058488_1580595060448431199_n.jpg'
    ))
    #12
    if text=="/pun-kocak" or data[0]=="kocak" or data[0]=="ngakak" or data[1]=="kocak" or data[1]=="ngakak":
        line_bot_api.reply_message(event.reply_token,ImageSendMessage(
    original_content_url='https://pbs.twimg.com/media/DYL2-5dVoAARtb4.jpg',
    preview_image_url='https://pbs.twimg.com/media/DYL2-5dVoAARtb4.jpg'
    ))
    #13
    if text=="/pun-lodeh" or data[1]=="terserah" or data[1]=="serah" or data[1]=="seterah" or data[0]=="terserah" or data[0]=="serah" or data[0]=="seterah":
        line_bot_api.reply_message(event.reply_token,ImageSendMessage(
    original_content_url='https://pics.me.me/terserah-lodeh-31686397.png',
    preview_image_url='https://pics.me.me/terserah-lodeh-31686397.png'
    ))
    #14
    if text=="/pun-mager" or data[0]=="mager" or data[1]=="mager":
        line_bot_api.reply_message(event.reply_token,ImageSendMessage(
    original_content_url='https://storage.jualo.com/original/12555347/bengkel-las-aneka-kar-alat-musik-lainnya-12555347.jpg',
    preview_image_url='https://storage.jualo.com/original/12555347/bengkel-las-aneka-kar-alat-musik-lainnya-12555347.jpg'
    ))
    #15
    if text=="/pun-pinter" or data[0]=="pinter" or data[0]=="pintar" or data[0]=="smart" or data[1]=="pinter" or data[1]=="pintar" or data[1]=="smart":
        line_bot_api.reply_message(event.reply_token,ImageSendMessage(
    original_content_url='https://pbs.twimg.com/media/DkNtokXVAAA3gdr.jpg',
    preview_image_url='https://pbs.twimg.com/media/DkNtokXVAAA3gdr.jpg'
    ))
    #16
    if text=="/pun-sabi" or data[0]=="sabi" or data[0]=="bisa" or data[1]=="sabi" or data[1]=="bisa":
        line_bot_api.reply_message(event.reply_token,ImageSendMessage(
    original_content_url='https://pbs.twimg.com/media/DbI1oKdUMAAKHl3.jpg',
    preview_image_url='https://pbs.twimg.com/media/DbI1oKdUMAAKHl3.jpg'
    ))
    #17
    if text=="/pun-sekip" or data[0]=="skip" or data[0]=="sekip" or data[0]=="sqip" or data[0]=="sqiv" or data[1]=="skip" or data[1]=="sekip" or data[1]=="sqip" or data[1]=="sqiv":
        line_bot_api.reply_message(event.reply_token,ImageSendMessage(
    original_content_url='https://4.bp.blogspot.com/-TXgBZ19sxHs/Wr3bhYlQy6I/AAAAAAAABPs/vbC_Be9GFmsWrhytSZXd90D9DaQymyhdQCLcBGAs/s1600/IMG_20180327_222132.jpg',
    preview_image_url='https://4.bp.blogspot.com/-TXgBZ19sxHs/Wr3bhYlQy6I/AAAAAAAABPs/vbC_Be9GFmsWrhytSZXd90D9DaQymyhdQCLcBGAs/s1600/IMG_20180327_222132.jpg'
    ))
    #18
    if text=="/pun-siyap" or data[0]=="siap" or data[0]=="siyap" or data[0]=="shap" or data[0]=="ready" or data[0]=="siaap" or data[1]=="siap" or data[1]=="siyap" or data[1]=="shap" or data[1]=="ready" or data[1]=="siaap":
        line_bot_api.reply_message(event.reply_token,ImageSendMessage(
    original_content_url='https://www.teknosaurus.com/wp-content/uploads/2018/03/sayap-e1521330529574.jpg',
    preview_image_url='https://www.teknosaurus.com/wp-content/uploads/2018/03/sayap-e1521330529574.jpg'
    ))
    #20
    if text=="/pun-thanks" or data[0]=="thanks" or data[0]=="thank" or data[0]=="makasih" or data[0]=="trims" or data[0]=="thx" or data[0]=="maaci" or data[1]=="thanks" or data[1]=="thank" or data[1]=="makasih" or data[1]=="trims" or data[1]=="thx" or data[1]=="maaci":
        line_bot_api.reply_message(event.reply_token,ImageSendMessage(
    original_content_url='https://3.bp.blogspot.com/-2bHJrd2yl7s/Wr3Sy2zDudI/AAAAAAAABNk/DKwqkIkvufUteDl_CQlvfV98EjDNeTJagCLcBGAs/s1600/IMG_20180327_221555.jpg',
    preview_image_url='https://3.bp.blogspot.com/-2bHJrd2yl7s/Wr3Sy2zDudI/AAAAAAAABNk/DKwqkIkvufUteDl_CQlvfV98EjDNeTJagCLcBGAs/s1600/IMG_20180327_221555.jpg'
    ))
    #21
    if text=="/pun-kampret" or data[0]=="kampret" or data[1]=="kampret":
        line_bot_api.reply_message(event.reply_token,ImageSendMessage(
    original_content_url='https://cdn2.boombastis.com/wp-content/uploads/2018/03/7kampret.jpeg',
    preview_image_url='https://cdn2.boombastis.com/wp-content/uploads/2018/03/7kampret.jpeg '
    ))
    
    
    
    
    
    
#WIKIHOW
    if text=="meme wikihow":
        kamus="Meme Wikihow"
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=kamus))
    #1
    if text=="/wkh-terciduk" or data[0]=="terciduk" or data[0]=="tercyduk" or data[0]=="tercyduck" or data[0]=="diciduk" or data[0]=="dicyduk" or data[0]=="dicyduck"  or data[1]=="terciduk" or data[1]=="tercyduk" or data[1]=="tercyduck" or data[1]=="diciduk" or data[1]=="dicyduk" or data[1]=="dicyduck":
        line_bot_api.reply_message(event.reply_token,ImageSendMessage(
    original_content_url='https://pbs.twimg.com/media/DUnGmbTVAAYbI8w.jpg',
    preview_image_url='https://pbs.twimg.com/media/DUnGmbTVAAYbI8w.jpg'
    ))
    #2
    if text=="/wkh-berkelahi1" or data[0]=="berkelahi" or data[0]=="tengkar" or data[1]=="berkelahi" or data[1]=="tengkar":
        line_bot_api.reply_message(event.reply_token,ImageSendMessage(
    original_content_url='https://ktawa.com/wp-content/uploads/2018/03/DXvYNzGUMAAc6wT.jpg',
    preview_image_url='https://ktawa.com/wp-content/uploads/2018/03/DXvYNzGUMAAc6wT.jpg'
    ))
    #3
    if text=="/wkh-tabok" or data[0]=="tabok" or data[1]=="tabok":
        line_bot_api.reply_message(event.reply_token,ImageSendMessage(
    original_content_url='https://s.kaskus.id/images/2018/03/12/7034635_201803120552320355.jpg',
    preview_image_url='https://s.kaskus.id/images/2018/03/12/7034635_201803120552320355.jpg'
    ))
    #4
    if text=="/wkh-kalem" or data[0]=="kalem" or data[1]=="kalem" or data[0]=="calm" or data[1]=="calm":
        line_bot_api.reply_message(event.reply_token,ImageSendMessage(
    original_content_url='https://s.kaskus.id/images/2018/03/12/7034635_201803120524290806.jpg',
    preview_image_url='https://s.kaskus.id/images/2018/03/12/7034635_201803120524290806.jpg'
    ))
    #5
    if text=="/wkh-maksiat" or data[0]=="maksiat" or data[1]=="maksiat":
        line_bot_api.reply_message(event.reply_token,ImageSendMessage(
    original_content_url='https://pbs.twimg.com/media/DUnCIAUUMAArpyA.jpg',
    preview_image_url='https://pbs.twimg.com/media/DUnCIAUUMAArpyA.jpg'
    ))
    #6
    if text=="/wkh-bacot" or data[0]=="bacot" or data[1]=="bacot" or data[0]=="bct" or data[1]=="bct" or data[0]=="bacod" or data[1]=="bacod" or data[0]=="bcd" or data[1]=="bcd":
        line_bot_api.reply_message(event.reply_token,ImageSendMessage(
    original_content_url='https://s.kaskus.id/images/2018/03/12/7034635_201803120533550838.jpg',
    preview_image_url='https://s.kaskus.id/images/2018/03/12/7034635_201803120533550838.jpg'
    ))
    #7
    if text=="/wkh-sabar" or data[0]=="sabar" or data[1]=="sabar":
        line_bot_api.reply_message(event.reply_token,ImageSendMessage(
    original_content_url='https://i.pinimg.com/750x/f3/83/c3/f383c3106936a4728d924dd7ff945c20.jpg',
    preview_image_url='https://i.pinimg.com/750x/f3/83/c3/f383c3106936a4728d924dd7ff945c20.jpg'
    ))
    #8
    if text=="/wkh-posthink" or data[0]=="positif" or data[1]=="positif" or data[0]=="positive" or data[1]=="positive" or text=="positive thinking":
        line_bot_api.reply_message(event.reply_token,ImageSendMessage(
    original_content_url='https://pbs.twimg.com/media/DU3n1OuV4AE9sZg.jpg',
    preview_image_url='https://pbs.twimg.com/media/DU3n1OuV4AE9sZg.jpg'
    ))
    #9
    if text=="/wkh-bodoh":
        line_bot_api.reply_message(event.reply_token,ImageSendMessage(
    original_content_url='https://ktawa.com/wp-content/uploads/2018/05/2761997_201803120735020920.jpg',
    preview_image_url='https://ktawa.com/wp-content/uploads/2018/05/2761997_201803120735020920.jpg'
    ))
    #10
    if text=="/wkh-bodo":
        line_bot_api.reply_message(event.reply_token,ImageSendMessage(
    original_content_url='https://ktawa.com/wp-content/uploads/2018/09/DXgqnNRVwAA-_6F.jpg',
    preview_image_url='https://ktawa.com/wp-content/uploads/2018/09/DXgqnNRVwAA-_6F.jpg'
    ))
    #11
    if text=="/wkh-bomat":
        line_bot_api.reply_message(event.reply_token,ImageSendMessage(
    original_content_url='https://s.kaskus.id/images/2018/03/12/7034635_201803120525540375.jpg',
    preview_image_url='https://s.kaskus.id/images/2018/03/12/7034635_201803120525540375.jpg'
    ))
    #12
    if text=="/wkh-diam":
        line_bot_api.reply_message(event.reply_token,ImageSendMessage(
    original_content_url='https://pbs.twimg.com/media/DXgpJPMU8AAxjFm.jpg',
    preview_image_url='https://pbs.twimg.com/media/DXgpJPMU8AAxjFm.jpg'
    ))
    #13
    if text=="/wkh-kesel":
        line_bot_api.reply_message(event.reply_token,ImageSendMessage(
    original_content_url='https://pbs.twimg.com/media/DVtT5HfVoAA74P3.jpg',
    preview_image_url='https://pbs.twimg.com/media/DVtT5HfVoAA74P3.jpg'
    ))

#etc
    if text=="cuy":
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='oposeduh'))
    if text=="tyo":
        line_bot_api.reply_message(event.reply_token,ImageSendMessage(
    original_content_url='https://s0.bukalapak.com/img/0343005662/w-1000/Boneka_Anak_Jerapah_Imut_Menggemaskan.jpg',
    preview_image_url='https://s0.bukalapak.com/img/0343005662/w-1000/Boneka_Anak_Jerapah_Imut_Menggemaskan.jpg'
    ))
        

#LEAVE GRUP / MPC
    if text=="/bye":
        if isinstance(event.source, SourceGroup):
            line_bot_api.push_message(event.source.group_id, TextSendMessage(text='***Snap!***'))
            line_bot_api.push_message(event.source.group_id, TextSendMessage(text="Mr. Stark, I don't feel so good" ))
            line_bot_api.push_message(event.source.group_id, TextSendMessage(text='Parah, '+profile.display_name+' jahat bgt'))
            line_bot_api.leave_group(event.source.group_id)
        elif isinstance(event.source, SourceRoom):
            line_bot_api.push_message(event.source.group_id, TextSendMessage(text='***Snap!***'))
            line_bot_api.push_message(event.source.group_id, TextSendMessage(text="Mr. Stark, I don't feel so good" ))
            line_bot_api.push_message(event.source.group_id, TextSendMessage(text='Parah, '+profile.display_name+' jahat bgt'))
            line_bot_api.leave_room(event.source.room_id)
    
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)