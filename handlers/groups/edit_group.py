import io

from aiogram import types
from aiogram.dispatcher.filters import Command

from filters import IsGroup
from filters.admins import AdminFilter
from loader import dp, bot


@dp.message_handler(IsGroup(), Command("set_photo", prefixes="!/"), AdminFilter())
async def set_new_photo(message: types.Message):
    source_message = message.reply_to_message
    photo = source_message.photo[-1]
    photo = await photo.download(destination=io.BytesIO())
    input_file = types.InputFile(photo)
    #1-usul
    try:
        await message.chat.set_photo(photo=input_file)
        await message.answer("Photo successfully loaded!")
    except:
        await message.answer("You can't set photo!")

@dp.message_handler(IsGroup(), Command("set_title", prefixes="!/"), AdminFilter())
async def set_new_title(message: types.Message):
    try:
        source_message = message.reply_to_message
        title = source_message.text
        #2-usul
        await bot.set_chat_title(message.chat.id, title=title)
        await message.answer(f"Title changed to 👇\n{title}")
    except:
        await message.answer("You can't change title of this group")


@dp.message_handler(IsGroup(), Command("set_description", prefixes="!/"), AdminFilter())
async def set_new_description(message: types.Message):
    try:
        source_message = message.reply_to_message
        # print(source_message)
        description = source_message.text
        # 1-usul
        # await bot.set_chat_description(message.chat.id, description=description)
        # 2-usul
        await message.chat.set_description(description=description)
        await message.answer('Chat description is modified')
    except:
        await message.reply('Chat description is not modified. Because you are not Admin')
        