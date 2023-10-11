from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.start_keyboards import get_start_keyboards

from loader import dp


@dp.message_handler(text="About Usℹ️")
async def about(message: types.Message):
    photo = "https://avatars.mds.yandex.net/get-altay/927916/2a00000185bedb2a15156f16141730efa685/orig"
    msg = """
        <a href='https://marsit.uz'>Mars IT School</a>, O'zbekistondagi bolalar ta'lim muassasalari orasida yetakchi <b>o’quv markazi</b>.  
        """
    await message.answer_photo(photo=photo)
    await message.answer(text=msg)