from aiogram import types

from loader import dp

import wikipedia


# Echo bot
@dp.message_handler()
async def sendWiki(message: types.Message):
    try:
        lang = wikipedia.set_lang("ru")
        searched = wikipedia.summary(message.text)
        await message.answer(searched)
    except:
        await message.answer("Не нашел нечего")