from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton        


builder = InlineKeyboardBuilder()

builder.add(InlineKeyboardButton(
text="Выбор 1",
callback_data="choice_one"))

builder.add(InlineKeyboardButton(
text="Выбор 2",
callback_data="choice_two"))