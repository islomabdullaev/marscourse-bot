from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def get_design_keyboards():
    design = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="Motion Graphic", callback_data="motion_grapic_course"),
                InlineKeyboardButton(text="Graphic Design", callback_data="graphic_design_course"),
            ],
            [
                InlineKeyboardButton(text="3D", callback_data="3d_course"),
            ]
        ]
    )

    return design