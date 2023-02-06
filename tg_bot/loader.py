from aiogram import Bot, Dispatcher
import os
import gamelist

# Список Игр
gl = gamelist.Game_list()

bot = Bot(os.getenv('TOKEN'))
dp = Dispatcher(bot)
