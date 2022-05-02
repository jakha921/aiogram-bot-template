from aiogram import types
from loader import dp

from data.pizzas import inline_result_pizza


@dp.inline_handler(text='pizza')
async def inline_pizza(query: types.InlineQuery):
    await query.answer(inline_result_pizza)

@dp.inline_handler(text='image')
async def photo(query: types.InlineQuery):
    await query.answer(
        results=[
            types.InlineQueryResultPhoto(
                id='photo001',
                photo_url='https://raw.githubusercontent.com/aiogram/aiogram/master/docs/static/images/logo.png',
                thumb_url='https://raw.githubusercontent.com/aiogram/aiogram/master/docs/static/images/logo.png',
                caption='photo number 1',
            ),
            types.InlineQueryResultVideo(
                id='video001',
                video_url='https://youtu.be/aHci5xAnByY',
                caption='video number 1',
                description='short stuped video',
                title='Floating house',
                thumb_url='https://avatars.mds.yandex.net/i?id=cb0ac9b0fa70a5641cb9d15cf79d2569-5384577-images-thumbs&n=13',
                mime_type='video/mp4',
            )
        ]
    )

@dp.inline_handler(text='start')
async def empty_query(query: types.InlineQuery):
    await query.answer(
        results=[
            types.InlineQueryResultArticle(
                id=1,
                title='Start',
                input_message_content=types.InputTextMessageContent(
                    message_text='some text will be there!',
                ),
                url='https://github.com/jakha921',
                thumb_url='https://avatars.githubusercontent.com/u/80573464?v=4',
                description='GitHub',
            ),
            types.InlineQueryResultArticle(
                id=2,
                title='Bellisimo pizza',
                input_message_content=types.InputTextMessageContent(
                    message_text='use this to order Bellisimo pizza',
                ),
                url='https://bellissimo.uz/ru#Pizza',
                thumb_url='https://bellissimo.uz/_next/image?url=https%3A%2F%2Fio.bellissimo.uz%2Fimages%2F2c814f26-9d3c-4b66-ae54-003fe4db2cb4.jpg&w=750&q=75',
                description='pizza belissimo',
            ),
            types.InlineQueryResultArticle(
                id=3,
                title='Apex pizza',
                input_message_content=types.InputTextMessageContent(
                    message_text='use this to order apex pizza',
                ),
                url='https://apexpizza.uz/',
                thumb_url='https://bellissimo.uz/_next/image?url=https%3A%2F%2Fio.bellissimo.uz%2Fimages%2F94844930-5c66-4c12-a670-93b048169dbe.jpg&w=750&q=75',
                description='pizza apex',
            ),
        ]
    )