from aiogram import Bot, Router
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from aiogram.filters import Command
from aiogram.types import Message
from datetime import datetime, timedelta

router = Router()
  
async def send_message_scheduler(bot: Bot, message: str, user_id: int):
    await bot.send_message(chat_id=int(user_id), text="Не забудьте проверить уведомления!!!!!!")

@router.message(Command("task"))
async def echo_handler(
    message: Message, bot: Bot, apscheduler: AsyncIOScheduler
) -> None:
    """
    Handler will forward receive a message back to the sender

    By default, message handler will handle all message types (like a text, photo, sticker etc.)
    """
    try:
        # Send a copy of the received message
        dt = datetime.now() + timedelta(seconds=1)
        print(dt, bot, message.chat.id, message.text)
        apscheduler.add_job(
            send_message_scheduler,
            trigger="interval",
            start_date = datetime.now(),
            seconds = 3,
            id= 'my_task',
            kwargs={
                "bot": bot,
                "message": message.text,
                "user_id": message.chat.id,
            },
        )
    except TypeError:
        # But not all the types is supported to be copied so need to handle it
        await message.answer("Nice try!")
