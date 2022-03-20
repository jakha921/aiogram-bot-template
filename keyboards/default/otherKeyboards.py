from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


botMenu = ReplyKeyboardMarkup(
    keyboard=[
            [
                KeyboardButton(text='#0 Entering'),
                KeyboardButton(text='#1 Necessary applications '),
                
            ],
            [
                KeyboardButton(text='#2 First BOT Wiki'),
                KeyboardButton(text='#3 Second BOT Speak English'),                
            ],
            [
                KeyboardButton(text='#4 Third BOT Spelling Checker'),
                KeyboardButton(text='#5 Deploying BOT'),
            ],
            [
                KeyboardButton(text='Menu'),
            ]
        ],
    resize_keyboard=True
)