from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


menuPython = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='#1 Beginner'),
            KeyboardButton(text='#2 Intermediate'),
            KeyboardButton(text='#3 Advanced'),
        ],
        [
            KeyboardButton(text='Back'),
            KeyboardButton(text='Menu'),
        ]
    ],
    resize_keyboard=True,
    )
