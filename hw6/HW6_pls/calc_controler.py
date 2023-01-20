import string_input as data_input
import view_string_calc as viewer
import module_calc as calc

operators={'+':(calc.sum,1),
           '-':(calc.sub,1),
           '*':(calc.mult,0),
           '/':(calc.div,0)}

my_data=str(data_input.input_console('Введите строку для обработки')).replace(' ','')
viewer.to_console(my_data)

list_date=my_data.replace('+',' + ').replace('-',' - ').replace('*',' * ').replace('/',' / ').split()
if list_date[0]=='-':
    list_date[1]='-'+list_date[1]
    list_date.pop(0)

list_date= list(map(lambda a:int(a) if str(a).isdigit() else a,list_date))    

pririty_operation=sorted(list(set([x[1] for x in operators.values()])))

for pri in sorted(list(set([x[1] for x in operators.values()]))):
    i=0
    while i < len(list_date):
        if list_date[i] in operators.keys() and operators.get(list_date[i])[1]==pri:
            # делаем вычисления
            list_date[i-1]=operators.get(list_date[i])[0](list_date[i-1],list_date[i+1])
            for q in range(2): list_date.pop(i)
        else:
            i+=1     
print (list_date)