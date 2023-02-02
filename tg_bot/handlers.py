from loader import dp
from aiogram import types
import candy
import random as rnd

candy_game = candy.Candy()
beginer = 0


@dp.message_handler(commands=['start'])
async def mes_start(message: types.Message):
    await message.answer('Игра перезапущена. Для начала выполните /start_game')


@dp.message_handler(commands=['restart'])
async def mes_start(message: types.Message):
    global candy_game
    candy_game.restart()
    await message.answer('Игра перезапущена. Для начала выполните /start_game')


@dp.message_handler(commands=['help'])
async def mes_start(message: types.Message):
    await message.answer('Hi')


@dp.message_handler(commands=['start_game'])
async def mes_start(message: types.Message):
    global candy_game
    beginer = rnd.randint(0, 1)
    await message.answer('Начнем игру')
    await message.answer(f'Всего конфет - {candy_game.get_candy_count()}')
    await message.answer(f'За раз можно взять - {candy_game.get_candy_max()}')
    if candy_game.beginer % 2:
        bot_step = candy_game.bot_AI()
        candy_game.make_step(bot_step)
        await message.answer(f'Бот взял  - {bot_step} конфет. Осталось {candy_game.get_candy_count()} конфет')
    else:
        await message.answer(
            f'Ваш ход. Возьмите не больше  {min(candy_game.get_candy_max(), candy_game.get_candy_count())}')


@dp.message_handler()
async def mes_start(message: types.Message):
    if candy_game.get_candy_count() == 0:
        await message.answer('GAME OVER')
        await message.answer('Для начала новой, наберите /restart')
        return
    if message.text.isdigit():
        if int(message.text) > min(candy_game.get_candy_max(), candy_game.get_candy_count()):
            await message.answer(
                f'Ваш ход. Вы можете взять не больше {min(candy_game.get_candy_max(), candy_game.get_candy_count())} конфет')
            return
        candy_game.make_step(int(message.text))
        await message.answer(f'Вы взяли {message.text} осталось {candy_game.get_candy_count()} конфет')
        if candy_game.get_candy_count() == 0:
            await message.answer('Вы ВЫИГРАЛИ')
            return
        bot_step = candy_game.bot_AI()
        candy_game.make_step(bot_step)
        if candy_game.get_candy_count() == 0:
            await message.answer('БОТ ВЫИГРАЛ')
            return

        await message.answer(f'Бот взял  - {bot_step} конфет. Осталось {candy_game.get_candy_count()} конфет')

    else:
        await message.answer('Нужно ввести число')
