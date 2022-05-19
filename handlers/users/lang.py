from aiogram import types
from aiogram.dispatcher import FSMContext
import logging

from data.config import ADMINS
from loader import dp, db, bot
from keyboards.inline.langInline import lang, lang_callback


@dp.message_handler(commands="lang")
async def get_lang(msg: types.Message):
    await msg.answer("Choose your language", reply_markup=lang)


# @dp.callback_query_handler(lang_callback.filter(lang_name=['ru', 'uz']))
@dp.callback_query_handler(text_contains='lang:')
async def set_lang(call: types.CallbackQuery):
    language = call.data.split(':')[1]
    db.update_user_lang(lang=language, id=call.from_user.id)
    lang_name = 'russian' if language == 'ru' else 'uzbek'
    await call.message.answer(f'Language is {lang_name}')
    await bot.send_message(chat_id=ADMINS[0], text=f"The base has been updated:\n{call.from_user.first_name} > language : {language}")
    await call.message.delete()