from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp, bot, db
from data.config import ADMINS

# email input state
@dp.message_handler(commands="email")
async def bot_start(message:types.Message, state:FSMContext):
    await message.answer("Send your email address")
    await state.set_state("email")
    

# start email state (input) 
@dp.message_handler(state="email")
async def enter_email(message:types.Message, state:FSMContext):
    email = message.text
    db.update_user_email(email=email, id=message.from_user.id)
    user=db.select_user(id=message.from_user.id)
    await message.answer("Your email was updated!")
    await bot.send_message(chat_id=ADMINS, text=f"The base has been updated:{user}")
    await state.finish()