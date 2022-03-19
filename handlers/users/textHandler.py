from aiogram import types
from aiogram.dispatcher import filters

from loader import dp


@dp.message_handler(filters.Text(equals='Hi', ignore_case=True))    # должен прити этот текст
async def bot_greeting(msg: types.Message):
    await msg.answer(f"Hello, How are you?!")

@dp.message_handler(filters.Text(contains='hi', ignore_case=True))  # в тексте должно содержаться это слова
async def bot_say(msg: types.Message):
    await msg.answer('Are you greeting?')

# start with
#end with