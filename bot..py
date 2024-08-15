import asyncio
import logging
import sys
from os import getenv
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from typing import Any, Awaitable, Callable, Dict
from aiogram import BaseMiddleware
from aiogram.types import TelegramObject
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from aiogram.client.bot import DefaultBotProperties
from db import db_start
from handlers import start, help, echo, register, task, users, weather, photo
from dotenv import load_dotenv



async def on_startup(_):
    await db_start()
    

#Add middleware Scheduler
class SchedulerMiddleware(BaseMiddleware):
    def __init__(self, scheduler: AsyncIOScheduler):
        self.scheduler = scheduler

    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any],
    ) -> Any:
        # add apscheduler to data
        data["apscheduler"] = self.scheduler
        return await handler(event, data)  


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
