# Посчитать строковое выражение
# Доступны "+-*/().1234567890"


# Проверяем условия:
def str_cheker(my_str):

    digs='1234567890'
    my_str=str(my_str).replace(' ','').replace(',','.').replace(')(',')*(')

    # 1) входят только указаные символы    
    if len([1 for x in my_str if x not in '+-*/().1234567890'])>0:
         return (0,'недопустимые символы')

    # 2) между точкой могут быть только цифры
    for x in enumerate(my_str[1:-1]):
        if x[1] == '.' and not (my_str[x[0]] in digs and my_str[x[0]+2] in digs):            
            return(0,'между . и , могут быть только цифры')
            
   # 3) перед операцией может быть только цифра или закрывающаяся скобка исключение -
    for x in enumerate(my_str[1:-1]):
        if x[1] in '+*/' and not (my_str[x[0]] in digs+')' and my_str[x[0]+2] in digs+'(-'):            
            return(0,'перед операцией может быть только цифра или закрывающаяся скобка а после закрывающаяся')

    # 4) перед "-" может быть только цифра  скобка после только цифра или открывающаяся скобка
    for x in enumerate(my_str[1:-1]):
        if x[1] =='-' and not (my_str[x[0]] in digs+')(*/+' and my_str[x[0]+2] in digs+'('):            
            return(0,'перед "-" может быть только цифра скобка или операция */')

    # 4) перед "-" может быть только цифра  скобка после только цифра или открывающаяся скобка
    for x in enumerate(my_str[1:-1]):
        if x[1] =='-' and not (my_str[x[0]] in digs+')(*/+' and my_str[x[0]+2] in digs+'('):            
            return(0,'перед "-" может быть только цифра скобка или операция */')
   
   # 6)  перед цифрой может быть только цифра 
    for x in enumerate(my_str[1:-1]):

        if x[1] in digs and (my_str[x[0]] ==')' or my_str[x[0]+2]=='('):
            return(0,'нарушение правила знаков и скобок')
        
    my_str=str(my_str).replace('+-','-')

    # Порядок скобок
    count=0
    for x in my_str:
        if x=='(':count+=1
        if x==')':count-=1
        if count<0: return (0,'Не соблюден порядок скобок') 
    
    if (my_str[0] in digs and my_str[1]=='(') or (my_str[-1]in digs and my_str[-2]==')') :
        return (0,'Не соблюдено сочетание скобок и цифр')

    if my_str[-1] in '+-*/.(':
        return (0,'недопустимое значение в конце')


    return(1,my_str)     
def my_calk (my_string, cheker):

    if cheker==1:
        
        (is_pass,my_string)=str_cheker(my_string)
        if is_pass!=1:
            print (my_string)
            return
    print (my_string)        

my_str='(12.1)+1,5+8*-(9)(8+8)'
my_calk('1234+12j3+1234-24',1)        




