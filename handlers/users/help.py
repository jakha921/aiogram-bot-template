from aiogram import types
from aiogram.dispatcher.filters import builtin

from loader import dp


@dp.message_handler(builtin.CommandHelp())
async def bot_help(message: types.Message):
        text = ("Buyruqlar: ",
                "/start - Botni ishga tushirish",
                "/help - Yordam")

        await message.answer("\n".join(text))


@dp.message_handler(builtin.CommandSettings())
async def bot_settings(message: types.Message):
        text = ("you runned /settings command")

        await message.answer(text)
