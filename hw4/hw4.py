# A. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) 
# многочлена и записать в файл многочлен степени k.
# Пример:
# если k = 2, то многочлены могут быть => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

# B. Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

# НЕОБЯЗАТЕЛЬНОЕ, ДОПОЛНИТЕЛЬНОЕ ЗАДАНИЕ:
# Расширить значение коэффициентов до [-100..100]

import random as rnd

# Создаем коэффицинты многочлена
def create_dic(count):
    if count <0:
        return -1
    i=0
    k=count
    koef={}
    for i in range(count+1):
        koef[i]=koef[i]=rnd.randint(-100,100)
    
    # Добавлены специально 0,1 и -1 для чистоты экспремента
    koef[2]=0
    koef[3]=1
    koef[4]=-1
    
    return koef    

# Принимаем строку и возвращаем словарь
def multy_desassembler(multy_str):
    d_koef = {}
    temp_list = str(multy_str).replace('-', '+-').replace('*', '').split('+')
    max = 0
    for i in range(len(temp_list)):
        temp_list[i] = temp_list[i].split('x')

        if (len(temp_list[i]) == 1):
            my_key = 0
            my_value = int(temp_list[i][0])
        else:
            if temp_list[i][0] == '':
                temp_list[i][0] = '1'
            if temp_list[i][1] == '':
                temp_list[i][1] = '1'
            if temp_list[i][0] == '-':
                temp_list[i][0] = '-1'
            my_key = int(temp_list[i][1])
            my_value = int(temp_list[i][0])
        d_koef[int(my_key)] = int(my_value)
        if my_key > max:
            max = my_key
    if (len(d_koef) < max+1):

        # Заполняем пустые ключи нулями
        for i in range(max+1):
            # print(d_koef.get(i))
            if (d_koef.get(i) == None):
                d_koef[i] = 0

    return d_koef

#Отправляем словарь с коэффицинтами, где:
# ключ - чтепень при х
# значение - коэффициент
def multy_assembler(koefs):
    i = 0
    k = len(koefs)
    koef = koefs
    multi_string = ''
    while i < k:

        # Первый коэффициент не равен 0
        if koef[i] == 0:
            if i == 0:
                continue
            else:
                i += 1
                continue

        # Формируем x со степенью, учитываем степени 0 и 1
        if i == 0:
            temp_pref = ''
        elif i == 1:
            temp_pref = 'x'
        else:
            temp_pref = 'x'+str(i)

        # Формируем коэффициенты при x учитывая знак и значения 1,-1 и 0
        if koef[i] > 1:
            temp_pref = '+'+str(koef[i])+'*'+temp_pref
        elif koef[i] < -1:
            temp_pref = str(koef[i])+'*'+temp_pref
        elif koef[i] == -1:
            temp_pref = '-'+temp_pref
        elif koef[i] == 1:
            temp_pref = '+'+temp_pref

        # Отдельно проверяем свободный член
        if i == 0:
            if koef[i] == 0:
                temp_pref = ''
            elif koef[i] > 0:
                temp_pref = '+'+str(koef[i])
            else:
                temp_pref = str(koef[i])
        i += 1
        multi_string = temp_pref+multi_string

    return multi_string[1:]

#Принимаем две строки с многочленами и возвращам их сумму
def sum(multy1, multy2):

    koef1 = multy_desassembler(multy1)
    koef2 = multy_desassembler(multy2)

    if (len(koef1) > len(koef2)):
        max_len = len(koef1)
    else:
        max_len = len(koef2)
    koef3 = {}
    for i in range(max_len):
        koef3[i] = koef1.get(i, 0)+koef2.get(i, 0)

    return multy_assembler(koef3)

# Создаем два многочлена и сохраняем их в разные файлы (по условию)

str1 = multy_assembler(create_dic(int(input ('Введите степень первого многочлна '))))

my_file = open('file1.txt','w')
my_file.writelines(str1)
my_file.close

str1 = multy_assembler(create_dic(int(input ('Введите степень второго многочлна '))))

my_file = open('file2.txt','w')
my_file.writelines(str1)
my_file.close

# читываем многочлены из файлов в разные строки (по условию задачи)
my_file = open('file1.txt','r')
str1=my_file.readline()
my_file.close
print ('Многочлен 1')
print(str1)

my_file = open('file2.txt','r')
str2=my_file.readline()
my_file.close
print ('Многочлен 2')
print(str2)
print ('Сумма многочленов')
str3=sum(str1, str2)
print(str3)

my_file = open('file3.txt','w')
my_file.writelines(str3)
my_file.close




