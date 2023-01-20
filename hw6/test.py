import random as rnd

lst =  [rnd.randint(10,100) for _ in range(rnd.randint(10,20))]
print (f'{lst} -> на нечётных позициях элементы {str(list(map(lambda b:b[1],filter(lambda a:a[0]%2, enumerate(lst)))))[1:-1]}, ответ {sum(list(map(lambda b:b[1],filter(lambda a:a[0]%2, enumerate(lst)))))} ')
print (sum([x[1] for x in enumerate(lst) if x[0]%2==1]))
