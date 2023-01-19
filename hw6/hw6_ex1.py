
import random as rnd

# Напишите программу, которая по заданному номеру четверти, показывает диапазон
# возможных координат точек в этой четверти (x и y).
# q = int(input("введите четверть декартовой системы координат 1-4  "))
# if (q > 4 or q <= 0):
#     print('некорректные данные')
# else:
#     if (q == 1):
#         print(f'X=(0,+бесконечность)  Y=(0,+бесконечность)')
#     elif (q == 2):
#         print(f'X=(0,-бесконечность,0)  Y=(0,+бесконечность)')
#     elif (q == 3):
#         print(f'X=(0,-бесконечность,0)  Y=(0,-бесконечность,0)')
#     else:
#         print(f'X=(0,+бесконечность)  Y=(0,-бесконечность,0)')

# anyKey = input("\n през ани кей ту континиус")
# for i in range(50):
#     print('\n')

# q = int(input("введите четверть декартовой системы координат 1-4  "))

msg={1:'(0,-бесконечность,0)',2:'(0,+бесконечность)'}
text=dict(zip(('1','2','3','4'),((2,2),(1,2),(1,1),(2,1))))
print ((lambda a=input('Введите номер четверти от 1 до 4 '): 'Ввели некоректне данные' if text.get(a,'5')=='5' else 'X='+msg.get(text.get(a)[0]) + ' Y='+msg.get(text.get(a)[1]))())



# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

# myString=input('введите вещественное число или просто  строку где есть разные цифры  ')
# sum=0
# digs={}
# for  i in (range(10)):
#     digs[str(i)]=i

# for char in myString:
#     type(digs.get(char))
#     if type(digs.get(char))==int:
#             sum+=digs.get(char)
# print(f'{myString} -> {sum}')

print(sum([int(a) for a in input('Введите строку с цифрами') if a.isdigit()]))

# Реализуйте алгоритм перемешивания списка. НЕ ИСПОЛЬЗОВАТЬ ВСТРОЕННЫЕ БИБЛИОТЕКИ SHUFFLE, максимум использование библиотеки Random для и получения случайного int

# import random as rnd
# myList=[]
# for i in range(rnd.randint(10,20)):
#     myList.append(rnd.randint(1,100))
# print('До')
# print(myList)    
# print('После')
# for i in range(rnd.randint(100,1000)):
#     index1=rnd.randint(0,len(myList)-1)
#     index2=rnd.randint(0,len(myList)-1)
#     temp=myList[index1]
#     myList[index1]=myList[index2]
#     myList[index2]=temp
# print(myList)

def shuffl(lst):
    f_rnd = lambda q:rnd.randint(0,len(q)-1)   
    for i in range(500):
        a=f_rnd(lst)
        b=f_rnd(lst)
        t=lst[a]
        lst[a]=lst[b]
        lst[b]=t
    return lst    

myList= [rnd.randint(1,100) for _ in range(10,20)]
print (myList)
print (shuffl(myList))



# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# Создает Список случайных целых чисел
# def createRandomeIntList(n=20,min=1,max=200):
#     tList=[]
#     for i in range(n):
#         tList.append(rnd.randint(min,max))
#     return tList

# myList=createRandomeIntList(rnd.randint(5,30))
# sum=0
# print (myList,end=" -> на нечётных позициях элементы ")
# myStr=''
# if len(myList)>1:
#     for i in range(1,len(myList),2):
#             sum+=myList[i]
#             myStr=myStr+str(myList[i])+', '
# print (f'{myStr[0:-2]} ответ: {sum}')

lst =  [rnd.randint(10,100) for _ in range(rnd.randint(10,20))]
print (f'{lst} -> на нечётных позициях элементы {str(list(map(lambda b:b[1],filter(lambda a:a[0]%2, enumerate(lst)))))[1:-1]}, ответ {sum(list(map(lambda b:b[1],filter(lambda a:a[0]%2, enumerate(lst)))))} ')
print (sum([x[1] for x in enumerate(lst) if x[0]%2==1]))


