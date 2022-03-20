from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove

from keyboards.default.menuPython import menuPython
from keyboards.default.menuKeyboard import menu, start

from loader import dp


# Menu

@dp.message_handler(Command("menu"))
async def cmd_start(message: Message):
    await message.answer("Choose an option:", reply_markup=menu)


@dp.message_handler(Text(equals="Python"))
async def get_bot(msg: Message):
    await msg.answer("You choose python menu", reply_markup=menuPython)


# python menu

@dp.message_handler(Text(equals="#1 Beginner"))
async def get_bot(msg: Message):
    await msg.answer("https://d1z78r8i505acl.cloudfront.net/playerAssets/1.6.10/embed/index.html#190657", reply_markup=menuPython)
