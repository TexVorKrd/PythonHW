import model

def ask_class(scool:dict):
    print('Выберите класс из списка')
    for (key,value) in scool:
        print (f'{key} {value}')
