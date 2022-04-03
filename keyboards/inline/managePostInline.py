from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData

post_callback = CallbackData("create_post", "action")

confirmation_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[[
        InlineKeyboardButton(text="🆗 Print out", callback_data=post_callback.new(action="post")),
        InlineKeyboardButton(text="❌ Cancel", callback_data=post_callback.new(action="cancel")),
    ]]
)