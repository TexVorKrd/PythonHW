from loader import dp
from aiogram.types import Message
from loader import gl as game_list
@dp.message_handler(commands=['play'])
async def mes_start(message: Message):
    if game_list.get_game(message.from_user.id)[0] == -1:
        game_list.add_game(message.from_user.id, message.from_user.first_name + message.from_user.last_name)
    game = game_list.get_game(message.from_user.id)[1]
    if not game.is_game():
        await message.answer('Для начала новой игры наберите /restart')
        return
    max_candy = min(game.get_candy_count(), game.get_candy_max())

    if game.get_beginer() % 2:
        bot_step = game.bot_AI()
        await message.answer('Продолжаем игру')
        await message.answer(f'Бот взял  - {bot_step} конфет.')
        game.make_step(bot_step)
        await message.answer(f'На столе   {game.get_candy_count()} конфет')
        max_candy = min(game.get_candy_count(), game.get_candy_max())
        await message.answer(f'Возьмите от 1 до  {max_candy}')
    else:
        await message.answer(f'Всего конфет на столе - {game.get_candy_count()} конфет')
        max_candy = min(game.get_candy_count(), game.get_candy_max())
        await message.answer(f'За раз можно взять от 1 до {max_candy} конфет')
        await message.answer('Ваш ход')

