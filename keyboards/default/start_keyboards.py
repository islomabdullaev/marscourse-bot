from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def get_start_keyboards():
    start_keyboard = ReplyKeyboardMarkup(
        [
            [
                KeyboardButton(text="Contact☎️"),
                KeyboardButton(text="Courses📒")
            ],
            [
                KeyboardButton(text="About Usℹ️")
            ]
        ],
        resize_keyboard=True
    )
    return start_keyboard
