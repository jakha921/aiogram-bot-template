from functools import cache
from gc import callbacks
import logging
from aiogram import types

from keyboards.inline.productInlineKeyboard import CourseInlineKeyboard, pythonInlineKeyboard, botMenu, python_django
from keyboards.inline.callback_data import course_callback, bot_callback

from loader import dp


# course default keyboard
@dp.message_handler(text_contains="Course")
async def get_product_inline_keyboard(message: types.Message):
    await message.answer("Choose section:", reply_markup=CourseInlineKeyboard)


# python inline keyboard
@dp.callback_query_handler(text="python")
async def get_python_course(call: types.CallbackQuery):
    # callback_data = call.data
    # logging.info(f'{callback_data=}')
    # logging.info(f'{call.from_user.id=}')
    
    await call.message.delete()
    await call.message.answer("Python course\nChoose lesson:", reply_markup=pythonInlineKeyboard)
    await call.answer(cache_time=60)


# bot inline keyboard
@dp.callback_query_handler(text="bot")
async def get_bot_course(call: types.CallbackQuery):    
    await call.message.delete()
    await call.message.answer("Bot course\nChoose lesson:", reply_markup=botMenu)
    await call.answer(cache_time=60)


# python django
@dp.callback_query_handler(course_callback.filter(item_name='django'))
async def get_python_django(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer("Django course:", reply_markup=python_django)
    await call.answer(cache_time=60)


# bot telegram bot
@dp.callback_query_handler(bot_callback.filter(item_name='telegram_bot'))
async def get_telegram_bot(call: types.CallbackQuery):
    # await call.message.delete()
    await call.answer('You just purchased this course!', cache_time=60, show_alert=True)
    
# back
@dp.callback_query_handler(text="back")
async def get_back(call: types.CallbackQuery):
    callback_data = call.data
    logging.info(f'{callback_data=}')
    logging.info(f'{call.from_user.id=}')
    await call.message.edit_reply_markup(reply_markup=CourseInlineKeyboard)
    await call.answer()