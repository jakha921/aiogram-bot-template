import sqlite3

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from data.config import ADMINS
from loader import dp, db, bot


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    name=message.from_user.full_name
    # Наш пользователь запписан в базе
    try:
        db.add_user (id=message.from_user.id, name=name)
    except sqlite3.IntegrityError as err:
        await bot.send_message(chat_id=ADMINS[0], text=err)
    
    await message.answer(f"Hi, {message.from_user.full_name}!")
    
    # Отправляем данный админу
    count=db.count_users()[0]
    msg=f"{message.from_user.full_name} добавлен в базу. \nВ базе {count} есть пользователей"
    await bot.send_message(chat_id=ADMINS[0], text=msg)