from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton 


links = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton('👨‍💻 Профиль', 'https://github.com/jakha921', None, 'profile'),
            InlineKeyboardButton('📞 Контакт', callback_data='contact')
            
        ],
        [
            InlineKeyboardButton('📍Локация', callback_data='location')
        ]
    ],
)