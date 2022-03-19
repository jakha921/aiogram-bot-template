from aiogram import types
from aiogram.dispatcher.filters.builtin import Command
from loader import dp

@dp.message_handler(Command("language"))
async def set_language(message: types.Message):
    await message.answer(f'language is changed')



@dp.message_handler(Command(["menu", "lang"]))
# @dp.message_handler(commands=['menu', 'lang'])
async def bot_menu(message: types.Message):
    await message.answer(f'you runned /menu command')