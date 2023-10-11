from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def get_programming_keyboards():
    programming = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="Front End", callback_data="front_course"),
                InlineKeyboardButton(text="Back End", callback_data="back_end"),
            ]
        ]
    )

    return programming