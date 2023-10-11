from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.courses import get_course_keyboards
from keyboards.inline.programming import get_programming_keyboards
from keyboards.inline.design import get_design_keyboards
from keyboards.inline.starter import get_starter_keyboards
from states.courses import CourseBuyState
from aiogram.dispatcher import FSMContext
from datetime import datetime

from loader import dp, bot


@dp.message_handler(text="Courses📒")
async def course_list(message: types.Message):
    await message.answer(text="Choose course !", reply_markup=get_course_keyboards())
    await CourseBuyState.course.set()


@dp.message_handler(state=CourseBuyState.course)
async def get_course(message: types.Message, state: FSMContext):
    course = message.text
    await state.update_data({
        "course": course
    })
    if course == "Programming💻":
        repl_mark = get_programming_keyboards()
    elif course == "Design🖌️":
        repl_mark = get_design_keyboards()
    elif course == "Starter📒":
        repl_mark = get_starter_keyboards()

    await message.answer("Choose course item !", reply_markup=repl_mark)
    await CourseBuyState.item.set()


@dp.callback_query_handler(state=CourseBuyState.item)
async def get_course_item(call: types.CallbackQuery, state: FSMContext):
    item = call.data
    await state.update_data({
        "item": item
    })
    await call.message.answer("Enter a number of children !")
    await CourseBuyState.clients.set()

@dp.message_handler(state=CourseBuyState.clients)
async def get_clients_number(message: types.Message, state: FSMContext):
    group_chat_id = -4058229527
    now = datetime.now()
    clients = message.text
    course_price = 1090000
    await state.update_data({
        "clients": clients
    })
    data = await state.get_data()
    total_price = int(data['clients']) * course_price
    formatted_price = format(total_price, ",")
    msg_to_admins = f"""
        🗓️ {now.date()} - {now.time()}
        👤 @{message.from_user.username}
        📔 {data['course']}
        💻 {data['item'].split("_")[0]}
        🔢 {data['clients']}
        💵 {formatted_price}
    """
    await message.answer("Thanks, admins will contact you !")
    await bot.send_message(chat_id=group_chat_id, text=msg_to_admins)
    await state.finish()
    await state.reset_data()


# @dp.message_handler(text="Programming💻")
# async def programming_course_list(message: types.Message):
#     await message.answer(text="Programming", reply_markup=get_programming_keyboards())


# @dp.message_handler(text="Design🖌️")
# async def design_course_list(message: types.Message):
#     await message.answer(text="Design", reply_markup=get_design_keyboards())


# @dp.message_handler(text="Starter📒")
# async def starter_course_list(message: types.Message):
#     await message.answer(text="Starter", reply_markup=get_starter_keyboards())
