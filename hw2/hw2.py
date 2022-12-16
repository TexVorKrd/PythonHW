def goNext():
    input ('\nGo to next? ')
    cls()

def cls():
    for i in range(50):
        print('\n')




cls()
# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

myString=input('введите вещественное число или просто  строку где есть разные цифры  ')

sum=0

digs={}
for  i in (range(10)):
    digs[str(i)]=i

for char in myString:
    type(digs.get(char))
    if type(digs.get(char))==int:
            sum+=digs.get(char)
print(f'{myString} -> {sum}')


goNext()
# Задайте список из n чисел последовательности (1 + 1/n)^n, выведеите его на экран, а так же сумму элементов списка.
# Пример:
# Для n=4 -> [2, 2.25, 2.37, 2.44]
# Сумма 9.06

def noFactorial(n):
    if n!=0:
        return (1+1/n)**n 

myList=[]
sum=0
n=int(input('Введите N '))
for i in range(1,n+1):    
    myList.append(round(noFactorial(i),2))
    sum+=myList[i-1]

print (f'Для n={n} ->',end=' ' )
print (myList)
print (f'Сумма {round(sum,2)}')


goNext()
# Реализуйте алгоритм перемешивания списка. НЕ ИСПОЛЬЗОВАТЬ ВСТРОЕННЫЕ БИБЛИОТЕКИ SHUFFLE, максимум использование библиотеки Random для и получения случайного int

import random as rnd
myList=[]
for i in range(rnd.randint(10,20)):
    myList.append(rnd.randint(1,100))
print('До')
print(myList)    
print('После')
for i in range(rnd.randint(100,1000)):
    index1=rnd.randint(0,len(myList)-1)
    index2=rnd.randint(0,len(myList)-1)
    temp=myList[index1]
    myList[index1]=myList[index2]
    myList[index2]=temp
print(myList)



