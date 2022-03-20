from hashlib import algorithms_available
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline.callback_data import course_callback, bot_callback


# inline keyboard
# 1 type of inline keyboard
CourseInlineKeyboard = InlineKeyboardMarkup(
    row_width=2,
    inline_keyboard=[
        [
            InlineKeyboardButton(text='🐍Python', callback_data='python'),
        ],
        [
            InlineKeyboardButton(text='🤖Bot', callback_data='bot'),

        ]
    ]
)


# python inline keyboard
# 2 type of inline keyboard
pythonInlineKeyboard = InlineKeyboardMarkup(row_width=2)
django = InlineKeyboardButton(
    text="🌎Django", callback_data=course_callback.new(item_name='django'))
pythonInlineKeyboard.insert(django)

telegram = InlineKeyboardButton(
    text="🤖Telegram Bot", switch_inline_query='Good bot', callback_data=course_callback.new(item_name='telegram'))
pythonInlineKeyboard.insert(telegram)

algorithm = InlineKeyboardButton(
    text='📈algorithm', callback_data='course:algorithm')
pythonInlineKeyboard.insert(algorithm)

python = InlineKeyboardButton('🐍Python', callback_data='course:python')
pythonInlineKeyboard.insert(python)

back = InlineKeyboardButton(text='⬅️Back', callback_data='back')
pythonInlineKeyboard.insert(back)


# bot inline keyboard
# 3 type of inline keyboard
bots = {
    "🚙Rent car. Easy & Comfortable": "rent_car",
    "🤖Telegram Bot": "telegram_bot",
    "🌹Shop for flowers": "shop_flower",
    "📈algorithm": "algorithm",
}

botMenu = InlineKeyboardMarkup(row_width=2)
for key, value in bots.items():
    botMenu.insert(InlineKeyboardButton(text=key, callback_data=bot_callback.new(item_name=value)))
botMenu.insert(back)


# python_django
python_django = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                'Watch Django course', 'https://github.com/jakha921', None, 'python_django'),
        ],
        [
            InlineKeyboardButton(
                'Purchase Django course', 'https://www.udemy.com/course/django-the-complete-guide-to-web-development/', None, 'python_django_buy'),
        ]
    ]
)
