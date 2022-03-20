from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menuStart = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='💻Course'),
            KeyboardButton(text='ℹ️About'),
        ]
    ],
    resize_keyboard=True,
    
)