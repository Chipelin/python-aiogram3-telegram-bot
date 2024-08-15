from os import getenv
from dotenv import load_dotenv
import requests
from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

router = Router()


@router.message(Command('weather'))
async def get_weather(message: Message):
    load_dotenv()
    TOKEN = getenv('WEATHER_TOKEN')
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&lang=ru&appid='+ TOKEN
    text = message.text
    city = text.replace('/weather ', '')
    city_weather = requests.get(url.format(city)).json()
    try: 
        weather = {
                'city' : city,
                'temperature' : city_weather['main']['temp'],
                'description' : city_weather['weather'][0]['description'],
                }
        await message.answer(f'{str(weather['temperature'])} °C {weather["description"]}')

    except KeyError:
        await message.answer('Нет такого города!')
