from email import message_from_bytes
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp


# get deep link from user | like referral link
@dp.message_handler(CommandStart(deep_link='jakha921'))
async def bot_start(message: types.Message):
    link = message.get_args()
    text = f'you are welcome, {message.from_user.full_name}!\n'
    text += f'You recommended by {link}'
    await message.answer(text)


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Salom, {message.from_user.full_name}!")
