from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def get_starter_keyboards():
    starter = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="Starter(8-12)", callback_data="starter_old"),
                InlineKeyboardButton(text="Starter(12-16)", callback_data="starter_young"),
            ],
            [
                InlineKeyboardButton(text="Intensive", callback_data="intensive_course"),
            ]
        ]
    )

    return starter