import asyncio
import logging
import sys
from os import getenv
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from aiogram.client.bot import DefaultBotProperties
from database.sqlite import db_start
from handlers import start, help, echo, register, task, users, weather, photo
from middleware.scheduler import SchedulerMiddleware



async def on_startup(_):
    await db_start()
    


async def main() -> None:

    load_dotenv()
    TOKEN = getenv('BOT_TOKEN')
    bot = Bot(TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp = Dispatcher()

    dp.include_routers(start.router, 
                       help.router,
                       echo.router, 
                       register.router, 
                       task.router,
                       users.router,
                       weather.router,
                       photo.router)
    
    # And the run events dispatching
    scheduler = AsyncIOScheduler()
    timezone="Asia/Irkutsk"

    dp.update.middleware(
        SchedulerMiddleware(scheduler=scheduler),
    )

    scheduler.start()
    await dp.start_polling(bot, on_startup=on_startup)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
