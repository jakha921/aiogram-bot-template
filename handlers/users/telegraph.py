from aiogram import types

from loader import dp
from utils import photo_link, remove_background
import logging


@dp.message_handler(content_types='photo')
async def photo_handler(msg: types.Message):
    photo = msg.photo[-1]
    # print(photo)
    link = await photo_link(photo)
    await msg.answer(link)
    removed_back = await remove_background(link)
    # await msg.answer_document(removed_back)   # just send
    await msg.reply_document(removed_back)      # reply to the msg 
    



if __name__ == '__main__':
    photo_handler()