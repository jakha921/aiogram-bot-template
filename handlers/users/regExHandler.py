from aiogram import types
from aiogram.dispatcher import filters

from loader import dp


email_regexp = r'[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+'
phone_regexp = r'^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$'
command_email_regexp = r'/email:' + email_regexp

@dp.message_handler(filters.Regexp(email_regexp))   
async def regexp_email(msg: types.Message):
    await msg.answer(f"Email is correct")

@dp.message_handler(filters.Regexp(phone_regexp))
async def regexp_phone(msg: types.Message):
    await msg.answer(f"Phone is correct")

@dp.message_handler(regexp_commands=[command_email_regexp])
async def regexp_command_email(msg: types.Message):
    await msg.answer(f"Email command is correct")