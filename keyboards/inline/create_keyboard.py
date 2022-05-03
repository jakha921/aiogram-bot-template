from aiogram import types



def build_keyboard(product_name):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text='Заказать', callback_data=f'product:{product_name}'))
    return keyboard