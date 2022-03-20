from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove

from keyboards.default.menuKeyboard import menu
from keyboards.default.otherKeyboards import botMenu

from loader import dp


# Menu

@dp.message_handler(Command("menu"))
async def cmd_start(message: Message):
    await message.answer("Choose an option:", reply_markup=menu)


@dp.message_handler(Text(equals="Bot"))
# @dp.message_handler(text="Bot")
async def get_bot(message: Message):
    await message.answer("Choose section:", reply_markup=botMenu)


@dp.message_handler(Text(equals="#0 Entering"))
async def get_entering(message: Message):
    await message.answer("https://d1z78r8i505acl.cloudfront.net/playerAssets/1.6.10/embed/index.html#190657")


@dp.message_handler(Text(equals="#1 Necessary applications"))
async def get_necessary_applications(message: Message):
    await message.answer("https://d1z78r8i505acl.cloudfront.net/playerAssets/1.6.10/embed/index.html#190657")