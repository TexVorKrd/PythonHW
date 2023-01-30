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



    def get_class_number(self):
        return(self.numer_of_class)
    
    def get_classes(self):
        return(self.clasees)

    def get_class_list(self):
        return(self.classes_list)

    def get_names(self):
        return(self.names)

    def get_matches_by_classes(self):
        return(self.matches_by_classes)        

    def add_ask(self,classes:int,id_puple:int,ask_number:int):
        self.matches_by_classes.get(classes).get(id_puple).append(ask_number)

    def save_date(self):
        total_str=''
        for (key,value) in self.get_matches_by_classes().items():
            tmp_str=''
            for (k,v) in value.items():
                my_str=str(k)+','+''.join([str(a) for a in v])
                tmp_str=tmp_str+my_str+';'
            total_str=total_str+str(key)+';'+tmp_str[0:-1]+'|'
        # print (total_str)
        self.data[4]=total_str[0:-1]
        with open(self.path,encoding='UTF-8',mode='w') as file:
            file.writelines(self.data)    
 
    def print_data(self):
        pass        

     
            



