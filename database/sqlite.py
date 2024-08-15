import sqlite3 as sq
from aiogram.fsm.context import FSMContext
from aiogram.types import  Message



async def db_start():
    global db, cur

db = sq.connect('users_db')
cur = db.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS users(user_id TEXT PRIMARY KEY, name VARCHAR(64), age VARCHAR(64))')
db.commit()

async def create_user(user_id):
    user = cur.execute("SELECT 1 FROM users WHERE user_id == '{key}'".format(key = user_id)).fetchone()
    if not user:
        cur.execute("INSERT INTO users VALUES(?, ?, ?)", (user_id, '', ''))
        db.commit()


async def edit_user(state: FSMContext, user_id):
    data = await state.get_data()
    user_name = data['name']
    user_age = data['age']
    cur.execute("UPDATE users SET name = '{1}', age = '{2}' WHERE user_id == '{0}'".format(user_id, user_name, user_age ))
    db.commit()
 

    


