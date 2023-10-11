from aiogram.dispatcher.filters.state import StatesGroup, State


class CourseBuyState(StatesGroup):
    course = State()
    item = State()
    clients = State()