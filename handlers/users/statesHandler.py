from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp


@dp.message_handler(commands='buy')
async def set_state_command(msg: types.Message, state: FSMContext):
    await state.set_state(f"buy_state")
    await msg.answer(f"Choose product!")


@dp.message_handler(state='buy_state')
async def out_state(msg: types.Message, state: FSMContext):
    await msg.answer(f"Product added to cart!")
    await state.finish()
