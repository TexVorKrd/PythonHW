# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# aaaaabbbcccc -> 5a3b4c
# 5a3b4c -> aaaaabbbcccc

# Реализация для любой строки при условии что в раскодированной строке нет цифр
# В закодированой не содержатся 1 

def new_coder(de_str):

    if de_str=='':
        return ''

    code_list = [1, de_str[0]]
    for q in de_str[1:]:
        if code_list[-1] == q:

            code_list[-2] +=1
        else:
            code_list.append(1)
            code_list.append(q)

    return ''.join(str(x) for x in code_list).replace('1', '')

def new_decoder(code_str):

    # если строка пустая ее и возвращаем
    if code_str == '':
        return ''

    # Если первый символ не цифра приводим к нужному формату
    code_str = code_str if code_str[0].isdigit() else '1'+code_str

    # Собираем в кучу отдельно символы и отдельно цифры и формируем список
    # Последний элемент если он не символ не добавится
    code_list = []
    sub_str = ''
    for x in code_str:

        if x.isdigit():
            sub_str += x
        else:
            sub_str = '1' if sub_str == '' else sub_str
            code_list.append(sub_str)
            code_list.append(x)
            sub_str = ''

    # Декодируем строку

    count = list([x[1] for x in enumerate(code_list) if not x[0] % 2])
    value = list([x[1] for x in enumerate(code_list) if x[0] % 2])
    vc = list(zip(count, value))
    vc = [x[1]*int(x[0]) for x in vc]
    vc = ''.join(x for x in vc)

    # а теперь все то же самое в одну строку, так что фиг кто поймет
    vc = ''.join(x for x in [x[1]*int(x[0]) for x in list(zip(list([x[1] for x in enumerate(
        code_list) if not x[0] % 2]), list([x[1] for x in enumerate(code_list) if x[0] % 2])))])

    return vc

my_str = 'aaaawraabbbcwcccert'

print(my_str)
print(new_coder(my_str))
print(new_decoder(my_str))
