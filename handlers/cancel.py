
from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from apscheduler.schedulers.asyncio import AsyncIOScheduler

router = Router()

@router.message(Command("cancel"))
async def echo_handler_cancel(message: Message, apscheduler: AsyncIOScheduler) -> None:
    apscheduler.remove_all_jobs()
    await message.answer("Задача отменена!")