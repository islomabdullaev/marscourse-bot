from aiogram.dispatcher.filters.state import StatesGroup, State


class ContactState(StatesGroup):
    phone = State()