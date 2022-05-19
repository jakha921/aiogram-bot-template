from aiogram import types

from data.config import ADMINS


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("email", "Mail"),
            types.BotCommand("lang", "Language"),
            types.BotCommand("start", "Launch the bot"),
            types.BotCommand("help", "Help"),
        ]
    )
