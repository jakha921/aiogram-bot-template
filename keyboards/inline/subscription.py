from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from aiogram import types

from loader import dp

check_button = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🔔 Subscribed", callback_data="subscribed"),
        ]
    ]
)


