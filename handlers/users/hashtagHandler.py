from aiogram import types
from loader import dp


@dp.message_handler(hashtags='money')
@dp.message_handler(cashtags=['eur', 'usd'])
async def get_hashtag(msg: types.Message):
    await msg.answer('💰')
