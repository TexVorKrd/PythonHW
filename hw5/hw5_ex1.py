# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит заданное количество конфет. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход.
# a) Добавьте игру против бота
# b) Подумайте как наделить бота 'интеллектом'

# Логика:
# 1) Случайно генерится число конфет больше 28
# 2) Проводится жеребьевка
# 3) Цель привести количество конфет поле своего хода к колличеству кратному 28+1

import random as rnd 

# очистка консоли
cls=lambda :print ('\n'*50)

# Ручной ввод. Игрок Человек
def manual_step(count, max):

    max = min([count, max])
    candy_taked = 0

    while (not 0 < candy_taked <= max):
        candy_taked = int(input(f'Сколько конфет взять [1-{max}] ? '))
    return candy_taked


# Логика бота
def bot_step(count, max):

    if count % (max+1) == 0:
        return 1
    else:
        return count % (max+1)

# Лямбдабот
bot_AI=lambda a,b: rnd.randint(1,min(a,28)) if a%(b+1)==0 else a%(b+1)

# Лямбда рандом бот
bot_rnd = lambda a,b: rnd.randint(1,min([a,b]))

# Запуск игры
# players - список картежей ('Ирок',Логика)
# candy_c - количество конфет
# max_c - сколько можно взять максимум за раз
def game_starter (players,candy_c, max_c):
    
    cls()

    beginer = rnd.randint(0,1)
    print (f'\n Результат жеребьевки \n Начинает { players[beginer][0]} \n Число конфет - {candy_c}\n')
    
    # Тграем пока не забраны последнии конфеты.
    while(candy_c>0):
        candy_taken=players[beginer%2][1](candy_c, max_c)
        candy_c=candy_c-candy_taken
        print (f'ход - {beginer}  {players[beginer%2][0]} взял {candy_taken} конфет. Осталось {candy_c} конфет ')
        beginer+=1
    print (f'Выиграл {players[(beginer-1)%2][0]}')  


# Участники с логикой
player_list = [('Бот AI',bot_AI),(
'Миша',manual_step)]

max_candy_by_step=28
candy_count = rnd.randint(100,400)

game_starter(player_list, candy_count , max_candy_by_step)
