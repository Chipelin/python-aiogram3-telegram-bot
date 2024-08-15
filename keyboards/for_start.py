from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup        

def get_choices_kb() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()

    builder.add(InlineKeyboardButton(
    text="Выбор 1",
    callback_data="choice_one"))

    builder.add(InlineKeyboardButton(
    text="Выбор 2",
    callback_data="choice_two"))
    return builder.as_markup(resize_keyboard=True)