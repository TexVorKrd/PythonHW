from loader import dp
from aiogram import types
from aiogram.types import Message

@dp.message_handler(commands=['help'])
async def mes_start(message: types.Message):
    pass
    # await message.answer('Hi')

