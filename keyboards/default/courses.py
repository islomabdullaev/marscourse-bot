from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def get_course_keyboards():
    courses = ReplyKeyboardMarkup(
        [
            [
                KeyboardButton(text="Design🖌️"),
                KeyboardButton(text="Programming💻")
            ],
            [
                KeyboardButton(text="Starter📒")
            ],
            [
                KeyboardButton(text="Back⬅️")
            ]
        ],
        resize_keyboard=True
    )

    return courses