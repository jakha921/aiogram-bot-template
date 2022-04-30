from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

send_location = ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
send_location.add(KeyboardButton('📍Локация', request_location=True))
send_location.add(KeyboardButton('📱 Номер телефона', request_contact=True))