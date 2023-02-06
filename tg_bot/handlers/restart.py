from loader import dp
from aiogram.types import Message
from loader import gl as game_list
@dp.message_handler(commands=['restart'])
async def mes_start(message: Message):
    game=game_list.get_game(message.from_user.id)
    if game[0] == -1:
        await message.answer('Для начала игры введите /start')
        return
    game[1].restart()
    await message.answer('Игра перезапущена. Для начала выполните /play')
