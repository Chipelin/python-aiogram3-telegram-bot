from aiogram import Router, types, F
from aiogram.filters import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder

router = Router()

@router.message(Command("start"))
async def cmd_start(message: types.Message):
        builder = InlineKeyboardBuilder()
        builder.add(types.InlineKeyboardButton(
        text="Выбор 1",
        callback_data="choice_one"))
        builder.add(types.InlineKeyboardButton(
        text="Выбор 2",
        callback_data="choice_two"))
        await message.answer("Добро пожаловать в наш бот!", reply_markup=builder.as_markup())

@router.callback_query(F.data == "choice_one")
async def choice_one_button(callback: types.CallbackQuery):
    await callback.message.answer("Вы выбрали Выбор 1")

@router.callback_query(F.data == "choice_two")
async def choice_two_button(callback: types.CallbackQuery):
    await callback.message.answer("Вы выбрали Выбор 2")