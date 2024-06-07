from aiogram.filters.command import Command
from aiogram import types, Router
from aiogram import F
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types.web_app_info import WebAppInfo
from aiogram.types.callback_query import CallbackQuery
from aiogram.filters.callback_data import CallbackData



router = Router()

class MyCallback(CallbackData, prefix="my"):
    full_name: str

    
@router.message(Command("start"))
async def cmd_start(message: types.Message):
    builder = InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(
        text="MeetUp", web_app=WebAppInfo(url='https://f1e3-83-142-11-113.ngrok-free.app'))
    )
    builder.row(types.InlineKeyboardButton(
        text="Ответы на вопросы", 
        callback_data= MyCallback(full_name=f'{message.from_user.full_name}').pack()
        )
    )


    await message.answer(f'Привет,{message.from_user.full_name}, ты MeetUp`er, не правда ли? Если ты хочешь новых знакомств то быстрее переходи в приложение и ищи друзей!', reply_markup=builder.as_markup(),
    )

@router.callback_query(MyCallback.filter())
async def my_callback(query: CallbackQuery, callback_data: MyCallback):
    full_name = callback_data.full_name
    await query.message.answer(f'{full_name} это приложение для знакомств! Чтобы начать знакомиться, перейдите в MeetUp через /start или через меню!')

    
@router.message(Command("q"))
async def cmd_q(message: types.Message):
    await message.answer(f"Привет, {message.from_user.full_name}, чтобы начать искать знакомых введите /start!")


