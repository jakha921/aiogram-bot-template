from aiogram import types
from aiogram.dispatcher import filters
from loader import dp


# @dp.message_handler(content_types='photo')
# async def get_photo(msg: types.Message):
#     await msg.answer(f'What is this?')

@dp.message_handler(content_types=types.ContentType.PHOTO)
async def get_photo(msg: types.Message):
    await msg.answer(f'Is it photo?')


@dp.message_handler(content_types=types.ContentType.VOICE)
async def get_photo(msg: types.Message):
    await msg.answer(f'Is it voice?')


@dp.message_handler(content_types=types.ContentType.VIDEO)
@dp.message_handler(content_types=['document', 'location'])
async def get_file(msg: types.Message):
    await msg.answer(f'Is it kind of file?')


@dp.message_handler(content_types='sticker')
async def get_sticker(msg: types.Message):
    await msg.answer('😀')


@dp.message_handler(content_types=types.ContentType.CONTACT)
async def get_sticker(msg: types.Message):
    await msg.answer('📝')
