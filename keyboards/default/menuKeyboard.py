from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


menu = ReplyKeyboardMarkup(
    keyboard=[
        [
        KeyboardButton(text='Python'),
        KeyboardButton(text='Bot'),
        ],
    ],
    resize_keyboard=True,
    )

start = ReplyKeyboardMarkup(
    keyboard=[
        [
        KeyboardButton(text='Contact', request_contact=True),
        KeyboardButton(text='Location', request_location=True),
        KeyboardButton(text='Menu'),
        ],
    ],
    resize_keyboard=True,
    )
