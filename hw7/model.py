class My_journal:
    
    def __init__(self,path:str='my_scool.txt'):
        self.path=path
        self.data=[]
        with open(self.path,encoding='UTF-8',mode='r') as file:
            self.data=file.readlines()
        
        # Словарь Классов
        self.numer_of_class={int(a.split(',')[0]):a.split(',')[1] for a in self.data[0].replace('\n','').split(';')}
        print(self.numer_of_class)

        # Словарь Предметов
        self.clasees={int(a.split(',')[0]):a.split(',')[1] for a in self.data[1].replace('\n','').split(';')}
        print(self.clasees)
        
        # Словарь Учеников
        self.names={int(a.split(',')[0]):a.split(',')[1] for a in self.data[2].replace('\n','').split(';')}
        print(self.names)

        # Список Учеников в классе
        self.classes_list={int(a.split(',')[0]):list(map(lambda a:int(a),a.split(',')[1:])) for a in self.data[3].replace('\n','').split(';')}
        print(self.classes_list)

        # Предмет/Ученик/Список оценка
        self.matches_by_classes={int(a.split(';')[0]): {int(b.split(',')[0]):[int(c) for c in b.split(',')[1]] for b in  a.split(';')[1:]} for a in self.data[4].replace('\n','').split('|')}
        print(self.matches_by_classes)        



    def get_class(self):
        return(self.classes_list)        

    def print_data(self):
        pass        

    def print_data(self):
        pass        



    def print_data(self):
        pass        
            



