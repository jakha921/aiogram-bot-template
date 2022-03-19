import email
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from loader import dp
from states.personalData import PersonalData


@dp.message_handler(commands='anketa', state=None)
async def bot_start(message: types.Message):
    await message.answer(f"Enter your full name:")
    await PersonalData.fullname.set()


@dp.message_handler(state=PersonalData.fullname)
async def get_fullname(message: types.Message, state: FSMContext):
    fullname = message.text
    # await state.update_data(fullname=fullname)
    await state.update_data(
        {'fullname': fullname}
    )

    await message.answer(f"Enter your age:")
    await PersonalData.next()


@dp.message_handler(state=PersonalData.age)
async def get_email(message: types.Message, state: FSMContext):
    age = message.text
    # await state.update_data(age=age)
    await state.update_data(
        {'age': age}
    )

    await message.answer(f"Enter your phone:")
    await PersonalData.next()


@dp.message_handler(state=PersonalData.phone)
async def get_email(message: types.Message, state: FSMContext):
    phone = message.text
    # await state.update_data(phone=phone)
    await state.update_data(
        {'phone': phone}
    )

    data = await state.get_data()
    fullname = data['fullname']
    age = data['age']
    phone = data['phone']

    msg = "Your data:\n"
    msg += f"Fullname: {fullname}\n"
    msg += f"Age: {age}\n"
    msg += f"Phone: {phone}\n"
    await message.answer(msg)

    await state.finish()        # end of the state machine
    # await state.reset_state(with_data=False)    # if you want to save data
