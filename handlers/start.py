from aiogram import Router, types, F
from aiogram.filters import Command
from keyboards.for_start import builder

router = Router()

@router.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Добро пожаловать в наш бот!", reply_markup=builder.as_markup())

@router.callback_query(F.data == "choice_one")
async def choice_one_button(callback: types.CallbackQuery):
    await callback.message.answer("Вы выбрали Выбор 1")

@router.callback_query(F.data == "choice_two")
async def choice_two_button(callback: types.CallbackQuery):
    await callback.message.answer("Вы выбрали Выбор 2")