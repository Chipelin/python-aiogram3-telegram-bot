from aiogram import Router, F
from aiogram.filters import Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from database.sqlite import create_user, edit_user
import re

router = Router()

def extract_number(text):
    match = re.search(r'\b(\d+)\b', text)
    if match:
        return int(match.group(1))
    else:
        return None

class Form(StatesGroup):
    name = State()
    age = State()

@router.message(Command('register'))
async def start_questionnaire_process(message: Message, state: FSMContext):
        await message.answer('Здравствуйте. Как вас зовут?')
        await create_user(user_id=message.from_user.id)
        
        await state.set_state(Form.name)
    

    
@router.message(F.text, Form.name)
async def capture_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer('Ваш возраст?')
        
    await state.set_state(Form.age)



@router.message(F.text, Form.age)
async def capture_age(message: Message, state: FSMContext):
    check_age = extract_number(message.text)

    if not check_age or not (1 <= check_age <= 100):
        await message.reply('Пожалуйста, введите корректный возраст (число от 1 до 100).')
        return
    await state.update_data(age=check_age)
    data = await state.get_data()    
    msg_text = (f'Вас зовут {data.get("name")} и вам {data.get("age")}')
    await message.answer(msg_text)
    await edit_user(state, message.from_user.id)
    await state.clear()