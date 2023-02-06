from loader import dp
from aiogram import types
from aiogram.types import Message
from loader import gl as game_list


@dp.message_handler(commands=['start'])
async def mes_start(message: Message):
    await message.answer('Игра перезапущена. Для начала выполните /start_game')


@dp.message_handler(commands=['restart'])
async def mes_start(message: types.Message):
    global list_games
    if list_games.get(message.from_user.id) is None:
        list_games[message.from_user.id] = candy.Candy()
        list_games.get(message.from_user.id).set_player(message.from_user.id)
    print(message.from_user.id)
    list_games.get(message.from_user.id).restart()
    await message.answer('Игра перезапущена. Для начала выполните /start_game')


@dp.message_handler(commands=['help'])
async def mes_start(message: types.Message):
    await message.answer('Hi')


@dp.message_handler(commands=['start_game'])
async def mes_start(message: types.Message):
    global candy_game
    global list_games
    print(message)
    if list_games.get(message.from_user.id) == None:
        list_games[message.from_user.id] = candy.Candy()
        list_games.get(message.from_user.id).set_player(message.from_user.id)
        print(f'Добавлен игрок, всего играков {len(list_games)}')
    await message.answer(f'Добро пожаловать {list_games.get(message.from_user.id).get_player()} Вы уже сыграли {list_games.get(message.from_user.id).get_player_game_done()}')
    await message.answer('Начнем игру')
    await message.answer(f'Всего конфет - {list_games.get(message.from_user.id).get_candy_count()}')
    await message.answer(f'За раз можно взять - {list_games.get(message.from_user.id).get_candy_max()}')
    if list_games.get(message.from_user.id).beginer % 2:
        bot_step = list_games.get(message.from_user.id).bot_AI()
        list_games.get(message.from_user.id).make_step(bot_step)
        await message.answer(f'Бот взял  - {bot_step} конфет. Осталось {list_games.get(message.from_user.id).get_candy_count()} конфет')
    else:
        await message.answer(
            f'Ваш ход. Возьмите не больше  {min(list_games.get(message.from_user.id).get_candy_max(), list_games.get(message.from_user.id).get_candy_count())}')


@dp.message_handler()
async def mes_start(message: types.Message):
    if list_games.get(message.from_user.id).get_candy_count() == 0:
        await message.answer('GAME OVER')
        await message.answer('Для начала новой, наберите /restart')
        return
    if message.text.isdigit():
        if int(message.text) > min(list_games.get(message.from_user.id).get_candy_max(), list_games.get(message.from_user.id).get_candy_count()):
            await message.answer(
                f'Ваш ход. Вы можете взять не больше {min(list_games.get(message.from_user.id).get_candy_max(), list_games.get(message.from_user.id).get_candy_count())} конфет')
            return
        list_games.get(message.from_user.id).make_step(int(message.text))
        await message.answer(f'Вы взяли {message.text} осталось {list_games.get(message.from_user.id).get_candy_count()} конфет')
        if list_games.get(message.from_user.id).get_candy_count() == 0:
            await message.answer('Вы ВЫИГРАЛИ')
            return
        bot_step = list_games.get(message.from_user.id).bot_AI()
        list_games.get(message.from_user.id).make_step(bot_step)
        if list_games.get(message.from_user.id).get_candy_count() == 0:
            await message.answer('БОТ ВЫИГРАЛ')
            return

        await message.answer(f'Бот взял  - {bot_step} конфет. Осталось {list_games.get(message.from_user.id).get_candy_count()} конфет')

    else:
        await message.answer('Нужно ввести число')
