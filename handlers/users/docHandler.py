from loader import dp, bot
from aiogram.types import ContentType, Message
from pathlib import Path

import logging


# 'download', 'categories' -> downloads/categories/ (audio, video, doc and etc)
download_path = Path().joinpath('downloads')
download_path.mkdir(parents=True, exist_ok=True)


@dp.message_handler()
async def text_handler(message: Message):
    await message.reply('You send me a text')


@dp.message_handler(content_types=ContentType.DOCUMENT)
async def doc_handler(msg: Message):
    await msg.document.download(destination=download_path)
    doc_id = msg.document.file_id
    await msg.reply(f'You send me a document\n'
                    f'Document ID: {doc_id}')


@dp.message_handler(content_types='video')
async def video_handler(msg: Message):
    await msg.video.download(destination=download_path)
    video_id = msg.video.file_id
    await msg.reply(f'You send me a video\n'
                    f'Video ID: {video_id}')


@dp.message_handler(content_types='photo')
async def photo_handler(msg: Message):
    # await msg.photo[0].download(destination=download_path/'small')
    await msg.photo[-1].download(destination=download_path)
    photo_id = msg.photo[-1].file_id
    await msg.reply(f'You send me a photo\n'
                    f'Photo ID: {photo_id}')
