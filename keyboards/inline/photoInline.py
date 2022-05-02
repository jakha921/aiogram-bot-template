from aiogram import types

photo_key = types.InlineKeyboardMarkup(row_width=2)
photo_key.add(types.InlineKeyboardButton('Подробнее', 'https://bellissimo.uz/ru#Pizza'))
photo_key.add(types.InlineKeyboardButton('Заказать', callback_data='bellissimo : pizza'))
photo_key.add(types.InlineKeyboardButton('Поделиться', switch_inline_query='pizza'))