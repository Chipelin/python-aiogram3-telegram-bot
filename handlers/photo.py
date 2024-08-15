from aiogram import Router, F
from aiogram.types import Message

router = Router()

@router.message(F.photo)
async def photo_upload(message: Message):
    photo_data = message.photo[-1]    
    await message.answer(f'Размеры фото : {photo_data.width} X {photo_data.height}') 