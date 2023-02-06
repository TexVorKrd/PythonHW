from loader import dp
from aiogram.types import Message
from loader import gl as game_list
@dp.message_handler()
async def mes_start(message: Message):
    pass

    game=game_list.get_game(message.from_user.id)
    if game[0] == -1:
        await message.answer('Для начала игры наберите /start')
        return
    else:
        game = game[1]

    if not game.is_game():
        await message.answer('Игра завершена. Для новой игры введите  /restart')
        return

    max_candy = min(game.get_candy_count(), game.get_candy_max())
    if not message.text.isdigit():
        await message.answer(f'Введите число от 1 до  {max_candy}')
        return

    take_candy = int(message.text)
    if take_candy < 1 or take_candy > max_candy:
        await message.answer(f'Число должно быть от 1 до  {max_candy}')
        return

    game.make_step(take_candy)

    if not game.is_game():
        await message.answer('ВЫ ВЫИГРАЛИ')
        return
    else:
        bot_step = game.bot_AI()
        await message.answer(f'Бот взял  - {bot_step} конфет.')
        game.make_step(bot_step)
        if not game.is_game():
            await message.answer('БОТ ВЫИГРАЛИ')
            return

    await message.answer(f'На столе   {game.get_candy_count()} конфет')
    max_candy = min(game.get_candy_count(), game.get_candy_max())
    await message.answer(f'Возьмите от 1 до  {max_candy}')
