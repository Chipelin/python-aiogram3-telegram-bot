from aiogram import Router, types
from aiogram.filters import Command

router = Router()

@router.message(Command("echo")) 
async def cmd_echo(message: types.Message):
    try:
        await message.answer(message.text.replace('/echo ', ''))
    except TypeError:
        await message.answer("Некоректный тип данных сообщения")