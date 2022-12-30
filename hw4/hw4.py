# A. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) 
# многочлена и записать в файл многочлен степени k.
# Пример:
# если k = 2, то многочлены могут быть => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

# B. Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

# НЕОБЯЗАТЕЛЬНОЕ, ДОПОЛНИТЕЛЬНОЕ ЗАДАНИЕ:
# Расширить значение коэффициентов до [-100..100]
import random as rnd
import math

def multy_assembler(count):
    i=0
    k=count
    koef={}
    multi_string=''
    while i<=k:
        koef[i]=rnd.randint(-100,100)
        
        # Первый коэффициент не равен 0
        
        if i==2:
            koef[i]=1
        if i==3:
            koef[i]=-1
        if i==4:
            koef[i]=0
                


        print (f'i={i} k={koef[i]} ',end=' ')
        if koef[i]==0:            
            if i==0:
                continue
            else:
                i+=1
                continue
        # Формируем x со степенью, учитываем степени 0 и 1
        if i==0:
            temp_pref=''
        elif i==1:
            temp_pref='x'
        else:
            temp_pref='x'+str(i)
    

        if koef[i]>1:
            temp_pref='+'+str(koef[i])+'*'+temp_pref
        elif koef[i]<-1:
            temp_pref=str(koef[i])+'*'+temp_pref
        elif koef[i]==-1:
            temp_pref='-'+temp_pref
        elif koef[i]==1:
            temp_pref='+'+temp_pref
        if i==0:
            if koef[i]==0:
                temp_pref=''
            elif koef[i]>0:
                temp_pref='+'+str(koef[i])
            else:
                temp_pref=str(koef[i])
        i+=1
        print (temp_pref)
        multi_string=temp_pref+multi_string
    print(multi_string)
    return  multi_string[1:]

k=int(input('Введите степень многочлена '))
print (multy_assembler(k))