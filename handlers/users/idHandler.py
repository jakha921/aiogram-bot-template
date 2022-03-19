from aiogram import types
from aiogram.dispatcher import filters


from loader import dp


SUPER_USERS = [256841597, 123654789]
BLACK_LIST = [123654789, 123654789]


@dp.message_handler(chat_id=SUPER_USERS, text='secret')
async def id_filter(msg: types.Message):
    await msg.answer('Welcome Admin!')
