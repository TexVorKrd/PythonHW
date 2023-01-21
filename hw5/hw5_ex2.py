# Создайте программу для игры в 'Крестики-нолики'
# НЕОБЯЗАТЕЛЬНО Добавить игру против бота с интеллектом

# 0 - пусто 1 - крестик 2 - нолик.
import random as rnd
cls=lambda :print ('\n'*50)

print_fild = lambda fld:[print(list(map(lambda a:str(a).replace('0',' ').replace('1','X').replace('2','O') , x)),sep="\n") for x in fld]

# Ход Вручную
def manual_step(fild):
    steps=[row.copy() for row in fild]
    rows={0:'A',1:'B',2:'C'}
    cols={0:'1',1:'2',2:'3'}

    for row in range(3):
        for col in range(3):
            
            if (steps[row][col]==0):
                steps[row][col]=rows[row]+cols[col]
            else:
                steps[row][col]='  '




    print('\nДоступные ходы')
    [print (row) for row in steps]
    print()
    
    pos_step=[]
    for row in steps:
        for x in row:
            if x!="  ":
                pos_step.append(x)

    
    str_step =''

    while not str_step in pos_step:
        print('Выберите ход из  ', end=' ')
        print (*pos_step,end='  ')
        str_step= input().upper()
        
    
    return (int(str_step[0].replace('A','0').replace('B','1').replace('C','2')),int(str_step[1])-1)    

# RND BOT
def rnd_bot(fld):
    my_fld=[(x[0]//3,x[0]%3) for x in filter(lambda x: x[1]==0, enumerate(fld[0]+fld[1]+fld[2]))]
    
    return(my_fld[rnd.randint(0,len(my_fld)-1)])

def win_cheker(fild):
    chek_list=[]
    
    # все строки
    rows=fild
    # все столбцы
    cols=list(map(list,list(zip(fild[0],fild[1],fild[2]))))

    # диагональ слева на прпаво
    diag1 =[fild[point][point] for point in [0,1,2]]
    
    # диагональ справа налево
    diag2=[row[1][[2,1,0][row[0]]] for row in enumerate(fild) ]
    
    chek_list=rows+cols
    chek_list.append(diag1)
    chek_list.append(diag2)
    # print (chek_list)
    
    
    # проверяем кажды элемент списка что в нем все элементы равны    
    tester = list(map (lambda lst:lst[1]==lst[0] and lst[1]==lst[2] and lst[1]!=0 ,chek_list))
    
    # фильтруем только по условию что значение True
    tester = list(filter(lambda a:a,tester))
    if len(tester)>0:
        return True
    return False    

def game_starter(players):
    start_fild = [[0,0,0],[0,0,0],[0,0,0]]
    
    # Жеребьевка 
    beginer = rnd.randint(0,1)
    print (f'\n Результат жеребьевки \n Начинает {players[beginer][0]} Играет "X" {players[(beginer+1)%2][0]} Играет "O" \n')
    players[beginer].append(1)
    players[(beginer+1)%2].append(2)

    steps=1
    while not win_cheker(start_fild) and not steps ==10:
        print ('Текущее поле')
        print_fild(start_fild)
        print (f'\n Ходит {players[beginer%2][0]} - {str(players[beginer%2][2]).replace("1","X").replace("2","O")}')
        step=players[beginer%2][1](start_fild)
        start_fild[step[0]][step[1]]=players[beginer%2][2]
        beginer+=1
        steps+=1

    print_fild(start_fild)
    if steps!=10 or win_cheker(start_fild):
        print (f'---{players[(beginer-1)%2][0]} ВЫИГРАЛ!!!!---')    
    else:
        print ('---НИЧЬЯ---')    


cls()

player_list=[['Игрок 1',manual_step],['Игрок 2 - БОТ',rnd_bot]]

game_starter(player_list)




# print(manual_step(start_fild))

