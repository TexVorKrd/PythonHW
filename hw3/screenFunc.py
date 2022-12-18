# очищаем экран
def cls():
    for i in range(50):
        print()
# пауза
def goNext(msg='\n\nНажмите что нить для продолжения'):
    input(msg)

# Содержание ДЗ
with open ('hwText.txt','r',encoding='utf-8') as hwText:
    allLines=hwText.readlines()

# Печатает указанное задание или не печатаем ничего
def exes(n):
    with open ('hwText.txt','r',encoding='utf-8') as hwText:
            allLines=hwText.readlines()
    startFrom='ex'+str(n)+'\n'
    startTo='ex'+str(int(n)+1)+'\n'
    isPrint=False
    
    print('-'*50)  
    for myLine in allLines:

        # print (f'{myLine==startFrom}{myLine==startTo}{isPrint}')
        if myLine==startFrom :
            isPrint=True
        if myLine==startTo :
            isPrint=False        
        if (isPrint):
            print (myLine[0:-1])
    print('-'*50)                            

