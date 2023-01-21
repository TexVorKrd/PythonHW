command_list=[(1,'*показать все'),
              (2,'*загрузить'),
              (3,'сохранить'),
              (4,'*добавить'),
              (5,'*изменить'),
              (6,'*удалить'),
              (7,'*найти'),
              (8,'*выйти')]

def cls(): print('\n'*50)

def show_menu():
    for i in command_list:
        print(i)

def show_pb(pb:list,title:str='ТЕКУЩАЯ ТЕЛЕФОННАЯ КНИГА'):

    if len(pb)!=0:
        print(f'\n{title}\n')
        for x in enumerate(pb): print (f'{x[0]} - {x[1]}')
        print()
    else:
        print ('\nТЕЛЕФОННАЯ КНИГА ПУСТАЯ\n')

def show_deldate(date:list):
    
    if len(date)==0:
        print ('\nНИЧЕГО НЕ УДАЛЕНО\n')
    else:
        print ('\nУСПЕШНО УДАЛЕНА ЗАПИСЬ\n')
        print (date)
        print ()

def show_del_date_menu(pb:list):
    show_pb(pb,'ВЫБЕРИТЕ ЗАПИСЬ ДЛЯ УДАЛЕНИЯ')
    return(int(input('\n№ для удаления - ')))

def load_sucsess():
    print ('\nЗАГРУЗКА ВЫПОЛНЕНИЕ УСПЕШНО\n')

def load_fail():
    print ('\nЗАГРУЗКА НЕ ВЫПОЛНЕНА\n')

def stop_work():
    print ('\nРАБОТА ПРОГРАММЫ ЗАКОНЧЕНА\n')

def search_str():
    print ('\nВВЕДИТЕ ТЕКСТ ДЛЯ ПОИСКА ',end='- ')
    return input()

def add_line_ask():
    print ('\nДОБАВЛЕНИЕ ЗАПИСИ\n')
    name =input('введите Имя - ')
    tel =input('введите телефон - ')
    rem =input('введите Комментарий - ')
    return([name,tel,rem])

def add_line_resaullt(line:list=[]):
    if len(line)==0:
        print ('\nНИЧЕГО НЕ ДОБАВЛЕНО\n')
    else:
        print ('ЗАПИСЬ')
        print (line)
        print ('УСПЕШНО ДОБАВЛЕНА\n')

def update_viewer(pb:list):
    show_pb(pb)
    line=input ('ВЫБЕРИТЕ ЗАПИСЬ ДЛЯ РЕДАКТИРОВАНИЯ\nЕСЛИ ТАКОЙ ЗАПИСИ НЕТ РЕДАКТИРОВАНИЕ БУДЕТ ОСТАНОВЛЕНО\n - ?')
    if not line.isdigit(): 
        return (-1,[])
    if int(line)<0 or int(line)>len(pb)-1: 
        return (-1,[])
    line_date=pb[int(line)].copy()
    modifite_line=int(line)
    k=0
    while k==0:
        print ('Выберите поле для редактирования\n')
        for fild in enumerate(line_date):
            print (fild)
        print ()
        print (('\'exit\' - ЗАКОНЧИТЬ'))
        ask=input('? - ')

        if ask.isdigit():
            index=int(ask)
            if not (index>len(fild) or index<-1):                
                print (f'РЕДАКТИРУЕМ ЗНАЧЕНИЕ {index}  {line_date[index]}')
                new_fild =input ('ВВЕДИТЕ НОВОЕ ЗНАЧЕНИЕ - ')
                if new_fild!='':line_date[index]=new_fild            
            else:
                print ('ВЫБОР НЕДОПУСТИМ')        
        
        elif ask.lower()=='exit':
            k=1
        else:
            print ('ВЫБОР НЕДОПУСТИМ')

 
    return ((modifite_line,line_date))

def update_msg(flag:bool):
  
    if flag:
        print ('ДАННЫЕ УСПЕШНО ИЗМЕНЕНЫ')
    else:
        print ('ИЗМЕНЕИЕ НЕ ВНЕСЕНЫ')
                
def save_msg():
        print ('ДАННЫЕ УСПЕШНО СОХРАНЕНЫ')



    



  
