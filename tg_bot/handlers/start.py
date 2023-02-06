from loader import dp
from aiogram.types import Message
from loader import gl as game_list


@dp.message_handler(commands=['start'])
async def mes_start(message: Message):
    game = game_list.get_game(message.from_user.id)
    if game[0] == -1:
        await message.answer('Добро пожаловать новый игрок. Для начала введите команду /play')
    elif game[0] == 1:
        await message.answer(f'С возвращением {message.from_user.first_name}  {message.from_user.last_name}')
        await message.answer(f'Вы уже сыграли {game[1].game_done} игр')
        if game[1].is_game:
            await message.answer(f'У Вас незаконченая игра. для продолжения введите  /play')
        else:
            await message.answer(f'У Вас все игры закончены. Для новой игры введите  /restart')

