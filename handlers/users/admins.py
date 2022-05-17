from aiogram import types
import time

from data.config import ADMINS
from loader import dp, db, bot


@dp.message_handler(text='/allusers', user_id=ADMINS)
async def get_all_users(msg: types.Message):
    users = db.select_all_users()
    await msg.answer(f'{len(users)} users found')
    

@dp.message_handler (text="/ads", user_id=ADMINS)
async def send_ad_to_all(msg: types.Message):
    users=db.select_all_users()
    for user in users:
            user_id=user[0]
            photo_link = 'https://www.nandikannadakoota.org/wp-content/uploads/2016/01/yourad-1024x1024.png'
            await bot.send_photo(chat_id=user_id, photo=photo_link, caption="your ad can be here")
            time.sleep(1)   # cause TG have limit for send messages per second

@dp.message_handler(text="/clean_db", user_id=ADMINS)
async def delete_all_users(msg: types. Message):
    db.delete_users()
    await msg.answer("The was cleaned!")

if __name__ == '__main__':
    pass