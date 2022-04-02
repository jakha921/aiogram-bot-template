from aiogram import types

from filters import IsPrivet

from loader import dp


# Echo bot
@dp.message_handler(IsPrivet(), state=None)
async def bot_echo(message: types.Message):
    await message.answer(message.text)
