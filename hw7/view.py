import model

def ask_class_list(scool:dict):
    print('Выберите класс из списка указав порядковый номер')
    for (key,value) in scool.items():
        print (f'{key} - {value}')
    return int(input('? - '))

def ask_classes(scool:dict):
    print('Выберите предмет из списка указав порядковый номер')
    for (key,value) in scool.items():
        print (f'{key} - {value}')
    return int(input('? - '))

def show_class_list(my_jornal:model.My_journal, class_number:int, classes:int):
    print (f'Предмет {my_jornal.get_classes().get(classes)} ')
    print (f'Список {my_jornal.get_class_number().get(class_number)} ')
    print ('-'*10)
    for a in my_jornal.get_class_list().get(class_number):
        print (f'{a} - {my_jornal.get_names().get(a)}') 
    print ('-'*10)
    print ('Выберите ученика для ответа или наберите \'exit\' для выхода')
    ask=input('? -')
    if ask.lower()=='exit':
        return -1
    return int(ask)    

def show_ask_resault(my_jornal:model.My_journal, class_number:int, classes:int,id_name:int):
    print (f'Предмет {my_jornal.get_classes().get(classes)} ')
    print (f'Класс {my_jornal.get_class_number().get(class_number)} ')
    print (f'Ученик {my_jornal.get_names().get(id_name)}',end=' оценки - ')
    print (f'{my_jornal.get_matches_by_classes().get(classes).get(id_name)}')

    return (int(input('На какую оценку ответ? -')))
