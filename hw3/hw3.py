import screenFunc as scr
import random as rnd

# Создает Список случайных целых чисел
def createRandomeIntList(n=20,min=1,max=200):
    tList=[]
    for i in range(n):
        tList.append(rnd.randint(min,max))
    return tList

scr.cls()
# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
scr.exes(1)

myList=createRandomeIntList(rnd.randint(5,30))
sum=0
print (myList,end=" -> на нечётных позициях элементы ")
myStr=''
if len(myList)>1:
    for i in range(1,len(myList),2):
            sum+=myList[i]
            myStr=myStr+str(myList[i])+', '
print (f'{myStr[0:-2]} ответ: {sum}')

scr.goNext()
# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]
scr.exes(2)

myList=createRandomeIntList(rnd.randint(5,30))
print (myList,end=' => [')
myStr=''
for i in range(0,len(myList)):
            if (i>=len(myList)/2):
                break
            myStr=myStr+str(myList[i]*myList[len(myList)-1-i])+', '
print (f'{myStr[:-2]}]')

scr.goNext()
# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19
scr.exes(3)

myListFloat=[]
for i in range(rnd.randint(5,20)):    
    rndCount=round(rnd.random(),2)
    afterDot= int(str(rndCount).split('.')[1])
    myListFloat.append(rndCount)
    if i==0:
        min=afterDot
        max=afterDot
    if afterDot > max:
        max=afterDot
    if afterDot < min:
        min=afterDot    
print (f'\n{myListFloat} => 0.{max-min}\n')

scr.goNext()
# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10
scr.exes(4)

myStr=''
myCount=rnd.randint(1,1023)
print(f'- {myCount} ->',end='')
while myCount>0:
    myStr=str(myCount%2)+myStr
    myCount=myCount//2
print(f' {myStr}')

scr.goNext()
# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
scr.exes(5)

fib={0:0,1:1,2:1}

def fibWitnMemory (n):
    if (fib.get(n)!=None):
        return fib.get(n)
    if (n<0):
        return ((-1)**(n*-1+1))*fibWitnMemory(n*-1)
    fibItem=fibWitnMemory(n-1)+fibWitnMemory(n-2)    
    fib[n]=fibItem    
    return fibItem

count=rnd.randint(1,50)
print (f'- для k = {count} список будет выглядеть так:',end=' ')
fibList=[]
for i in range(count*-1,count+1):
    fibList.append(fibWitnMemory(i))
print (fibList)


