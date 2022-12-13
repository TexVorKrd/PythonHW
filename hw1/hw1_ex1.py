# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

dayNumber = int(input('Введите день недели'))
if 0<dayNumber<=5:
    print ('рабочий')
elif 5<dayNumber<8:
    print ('выходной')
else:
    print ('нет такого дня')

anyKey = input("\n през ани кей ту континиус")
for i in range(50):
    print ('\n')

# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.  


for xPred in [True,False]:
    for yPred in [True,False]:
        for zPred in [True,False]:
            print (f'X={xPred} Y={yPred} Z={zPred} значение ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z = {(not (xPred or yPred or zPred)) == (not (xPred) and not (yPred) and not (zPred))}')


anyKey = input("\n през ани кей ту континиус")
for i in range(50):
    print ('\n')

# Напишите программу, которая принимает на вход координаты точки (X и Y), 
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится 
# эта точка (или на какой оси она находится).

x=int(input("введите координату X отличное от 0  "))
y=int(input("введите координату Y отличное от 0  "))
if (x==0 or y==0):
    print ('некорректные данные')
else:
    if (x>0 and y>0):
        print (f'X={x} Y={y} 1 четверть')
    elif(x<0 and y>0):
        print (f'X={x} Y={y} 2 четверть')
    elif(x<0 and y<0):
        print (f'X={x} Y={y} 3 четверть')
    else:
        print (f'X={x} Y={y} 4 четверть')

anyKey = input("\n през ани кей ту континиус")
for i in range(50):
    print ('\n')

# Напишите программу, которая по заданному номеру четверти, показывает диапазон 
# возможных координат точек в этой четверти (x и y).
q=int(input("введите четверть декартовой системы координат 1-4  "))
if (q>4 or q<=0):
    print ('некорректные данные')
else:
    if (q==1):
        print (f'X=(0,+бесконечность)  Y=(0,+бесконечность)')
    elif(q==2):
        print (f'X=(0,-бесконечность,0)  Y=(0,+бесконечность)')
    elif(q==3):
        print (f'X=(0,-бесконечность,0)  Y=(0,-бесконечность,0)')
    else:
        print (f'X=(0,+бесконечность)  Y=(0,-бесконечность,0)')

anyKey = input("\n през ани кей ту континиус")
for i in range(50):
    print ('\n')

# Напишите программу, которая принимает на вход координаты двух 
# точек и находит расстояние между ними в 2D пространстве.

import math
coordInfo =[]
coordInfo.append(int(input("точку X точки А")))
coordInfo.append(int(input("точку Y точки А")))
coordInfo.append(int(input("точку X точки B")))
coordInfo.append(int(input("точку Y точки B")))

for i in coordInfo:
    print ((coordInfo[0]-coordInfo[3]))


print (f'Растояние между точками А({coordInfo[0]},{coordInfo[1]}) и А({coordInfo[2]},{coordInfo[3]}) равно {round(math.sqrt((coordInfo[0]-coordInfo[2])**2+(coordInfo[1]-coordInfo[3])**2),2)} ')












