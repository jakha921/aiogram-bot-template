from aiogram import types
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp
from keyboards.default.menuKeyboard import menu, start


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Salom, {message.from_user.full_name}!")
    await message.answer("Share your data:", reply_markup=start)
    


# start menu

@dp.message_handler(text="Contact")
async def get_bot(message: types.Message):
    await message.answer("Share your contact")


@dp.message_handler(text="Location")
async def get_bot(message: types.Message):
    await message.answer("Share your Location", request_location=True)


@dp.message_handler(Text(equals="Menu"))
async def get_menu(msg: types.Message):
    await msg.answer("Choose an option:", reply_markup=menu)
