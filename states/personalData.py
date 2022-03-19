from aiogram.dispatcher.filters.state import StatesGroup, State

from loader import dp


class PersonalData(StatesGroup):
    fullname = State()
    age = State()
    phone = State()
    