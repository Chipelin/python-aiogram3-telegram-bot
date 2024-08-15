import sqlite3
from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

router = Router()

@router.message(Command('users'))
async def get_users(message: Message):
    db = sqlite3.connect('users_db')
    cur = db.cursor()
    cur.execute("SELECT name, age FROM users")
    users = cur.fetchall()
    for user in users:
        await message.answer(f'{user[0]} {user[1]}')
    db.close()

  

  