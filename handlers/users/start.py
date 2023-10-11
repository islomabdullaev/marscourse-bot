from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.start_keyboards import get_start_keyboards

from loader import dp
admin_id = 1928655714


@dp.message_handler(CommandStart(), chat_id=1928655714)
async def bot_start(message: types.Message):
    photo = "https://avatars.mds.yandex.net/get-altay/998620/2a00000185bedb0cfe606686bf9d0f3c6bac/L_height"
    await message.answer_photo(
        photo=photo, caption="Welcome to Mars IT School!",
        reply_markup=get_start_keyboards())


@dp.message_handler(text="Back⬅️")
async def bot_start(message: types.Message):
    photo = "https://avatars.mds.yandex.net/get-altay/998620/2a00000185bedb0cfe606686bf9d0f3c6bac/L_height"
    await message.answer_photo(
        photo=photo, caption="Welcome to Mars IT School!",
        reply_markup=get_start_keyboards())