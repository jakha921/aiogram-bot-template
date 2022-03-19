from aiogram import types
from aiogram.dispatcher import filters

from loader import dp


# isReplyFilter
@dp.message_handler( commands=['id'], is_reply=True)
async def reply_filter(msg: types.Message):
    await msg.answer(msg.reply_to_message.from_user.id)


# isSenderContact
@dp.message_handler(filters.IsSenderContact(True), content_types=['contact'])
# @dp.message_handler(content_types=['contact'], is_sender_contact=True)
async def contact_filter(msg: types.Message):
    await msg.answer('Thank you for your contact!')


# ForwardedMessageFilter
@dp.message_handler(filters.ForwardedMessageFilter(True))
async def forwarded_message_filter(msg: types.Message):
    await msg.answer('You have forwarded a message!')


# ChatTypeFilter
@dp.message_handler(filters.ChatTypeFilter(types.ChatType.PRIVATE), commands=['lich'])    # PRIVATE is changable
# @dp.message_handler(content_types=['is_pm'], chat_type='private')
async def contact_filter(msg: types.Message):
    await msg.answer('You are in private mode!')