from aiogram import Dispatcher

from loader import dp
from .admins import AdminFilter
from .groupFilter import IsGroup
from .privetChat import IsPrivet


if __name__ == "filters":
    dp.filters_factory.bind(AdminFilter)
    dp.filters_factory.bind(IsGroup)
    dp.filters_factory.bind(IsPrivet)
