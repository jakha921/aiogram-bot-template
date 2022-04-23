from aiogram import types

from loader import dp, bot
from aiogram.dispatcher.filters.builtin import Command
import logging


@dp.message_handler(content_types='photo')
async def photo_handler(msg: types.Message):
    photo = msg.photo[-1].file_id
    await msg.answer(photo)

@dp.message_handler(content_types='video')
async def photo_handler(msg: types.Message):
    video = msg.video[-1].file_id
    await msg.answer(video)
    
@dp.message_handler(commands='profile')
async def profile_info(msg: types.Message):
    photo_link = 'AgACAgIAAxkBAAIlZ2Jj75A8BHv1k-Ji62QxNLPkLxjDAAKdvDEbRA8hSwjBl-D3Zzq3AQADAgADeAADJAQ'
    photo_url = 'https://instagram.ftas3-2.fna.fbcdn.net/v/t51.2885-15/106626783_1707628682726730_6732860763337866783_n.jpg?stp=dst-jpg_e35&_nc_ht=instagram.ftas3-2.fna.fbcdn.net&_nc_cat=106&_nc_ohc=Ae52MdZAEw4AX87Dgc6&edm=ALQROFkBAAAA&ccb=7-4&ig_cache_key=MjM0ODExOTUzMDAyMDMzNTc2OQ%3D%3D.2-ccb7-4&oh=00_AT-qA8WoI2tE0b4_4VRN4Di-xRLJLRQSIHaiXdROCQy3tw&oe=626A50E3&_nc_sid=30a2ef'
    photo_path = types.InputFile('media/photos/avatar.jpg')
    await msg.answer_photo(photo_path, caption='Привет, меня зовут Джахангир\nМой GitHub : https://github.com/jakha921/')
    await msg.reply_photo(photo_url, caption='Привет, меня зовут Джахангир\nМой GitHub : https://github.com/jakha921/')
    await bot.send_photo(msg.from_user.id, photo=photo_url, caption='Привет, меня зовут Джахангир\nМой GitHub : https://github.com/jakha921/')
    
@dp.message_handler(commands='album')
async def send_album(msg: types.Message):
    album = types.MediaGroup()
    p1 = 'https://instagram.ftas3-1.fna.fbcdn.net/v/t51.2885-15/20184145_1328704343894632_5133196770167226368_n.jpg?stp=dst-jpg_e35&_nc_ht=instagram.ftas3-1.fna.fbcdn.net&_nc_cat=104&_nc_ohc=baIa54WIPv8AX-zt5Qu&edm=ALQROFkBAAAA&ccb=7-4&ig_cache_key=MTU2MTQyMTk3NDQ5MjEwNDkzMg%3D%3D.2-ccb7-4&oh=00_AT8_uq5iM62ieqksVfkzuUKLEmet5-Ihgn_4jv4xAd9XpA&oe=6269FD41&_nc_sid=30a2ef'
    p2 = 'https://instagram.ftas3-2.fna.fbcdn.net/v/t51.2885-15/20225722_1880366578954085_4843883207558430720_n.jpg?stp=dst-jpg_e35&_nc_ht=instagram.ftas3-2.fna.fbcdn.net&_nc_cat=105&_nc_ohc=GZY20c3sWLYAX-ugRJN&tn=1yzX_LPGPOZnPcB8&edm=ALQROFkBAAAA&ccb=7-4&ig_cache_key=MTU2NjkxMzQzNTExMTAzODgxMw%3D%3D.2-ccb7-4&oh=00_AT-TpChRrM_4Htmb-5K2eYuW2n6Dz0l1VSYWX2Bqdpdo_Q&oe=626A5ECF&_nc_sid=30a2ef'
    p3 = 'https://instagram.ftas3-2.fna.fbcdn.net/v/t51.2885-15/29400847_422850991498736_5222286507989008384_n.jpg?stp=dst-jpg_e35&_nc_ht=instagram.ftas3-2.fna.fbcdn.net&_nc_cat=108&_nc_ohc=oCusW_Em7r4AX85NqVz&edm=ALQROFkBAAAA&ccb=7-4&ig_cache_key=MTc0MjkyMjgyMjUwMDM5NDc4Nw%3D%3D.2-ccb7-4&oh=00_AT-fkqoof7lavo0N5EFaqGs-gCDIXD6yBQB8U06jOslxPg&oe=626B8A73&_nc_sid=30a2ef'
    p4 = 'https://instagram.ftas3-1.fna.fbcdn.net/v/t51.2885-15/106186282_210588496797628_5749851095977718593_n.jpg?stp=dst-jpg_e35&_nc_ht=instagram.ftas3-1.fna.fbcdn.net&_nc_cat=104&_nc_ohc=RiRykPKeUE4AX9jMt5D&edm=ALQROFkBAAAA&ccb=7-4&ig_cache_key=MjM0NDY3MTE2OTE5NTk1MzI0MA%3D%3D.2-ccb7-4&oh=00_AT85_YpQ6wVVCH64tecv4DQIWz4KB5Lmgb_hIO0Vi5m4GQ&oe=626A3541&_nc_sid=30a2ef'
    
    v1 = 'https://instagram.ftas3-1.fna.fbcdn.net/v/t50.16885-16/278788110_491533632696355_7363398483358632352_n.mp4?efg=eyJ2ZW5jb2RlX3RhZyI6InZ0c192b2RfdXJsZ2VuLjcyMC5pZ3R2LmJhc2VsaW5lIiwicWVfZ3JvdXBzIjoiW1wiaWdfd2ViX2RlbGl2ZXJ5X3Z0c19vdGZcIl0ifQ&_nc_ht=instagram.ftas3-1.fna.fbcdn.net&_nc_cat=107&_nc_ohc=gXzFlGriSCcAX_gDsp8&edm=ALQROFkBAAAA&vs=3267682776798128_673119131&_nc_vs=HBksFQAYJEdBNzRuUkFqY0pJWERMOEJBS0RKUFZ6b0N6Qm1idlZCQUFBRhUAAsgBABUAGCRHR0FXblJCMjdtb1dhNzBGQUhxWHM4M0pjWjVlYnZWQkFBQUYVAgLIAQAoABgAGwGIB3VzZV9vaWwBMRUAACbAjIqouM%2FCQBUCKAJDMywXP%2FEOVgQYk3UYEmRhc2hfYmFzZWxpbmVfMV92MREAdewHAA%3D%3D&_nc_rid=79ac6e30e3&ccb=7-4&oe=6266811C&oh=00_AT--pBtfuKgLDoNffsbHZBihbkWfLpSdXidZfGAv58TtRg&_nc_sid=30a2ef'
    
    album.attach_photo(p1)
    album.attach_photo(p2)
    album.attach_photo(p3)
    album.attach_photo(p4)
    album.attach_video(v1, caption='album')
    
    await msg.answer_media_group(album)