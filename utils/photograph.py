from io import BytesIO
import aiohttp
from aiogram import types
from loader import bot


async def photo_link(photo: types.photo_size.PhotoSize) -> str:
    with await photo.download(BytesIO()) as file:
        form = aiohttp.FormData()
        form.add_field(
            name='file',
            value=file,
        )
        
        # async with bot.session.post('https://telegra.ph/upload', data=form) as response:
        #     img_src = await response.json()
        
        from aiohttp import ClientSession

        async with ClientSession() as sess:
            async with sess.post('https://telegra.ph/upload', data=form) as resp:
                img_src = await resp.json()

    link = 'http://telegra.ph/' + img_src[0]["src"]
    # print(link)
    return link