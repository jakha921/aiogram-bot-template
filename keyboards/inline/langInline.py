from aiogram import types

from aiogram.utils.callback_data import CallbackData

# callback for lang
lang_callback=CallbackData("lang","lang_name")


# ru = types.InlineKeyboardButton(text="🇷🇺", callback_data=lang_callback.new(lang_name="ru")),
# uz = types.InlineKeyboardButton(text="🇺🇿", callback_data=lang_callback.new(lang_name="uz")),
ru = types.InlineKeyboardButton(text="🇷🇺", callback_data="lang:ru"),
uz = types.InlineKeyboardButton(text="🇺🇿", callback_data="lang:uz"),
lang = types.InlineKeyboardMarkup(inline_keyboard=[ru, uz])