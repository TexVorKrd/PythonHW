class PhoneBook:
    
    def __init__(self,path:str='my_pb.css'):
        self.path=path
        self.phone_book=[]
    
    def get_data(self):
        return self.phone_book

    def load(self):
        with open(self.path,encoding='UTF-8',mode='r') as file:
            data=file.readlines()
            data=[x.replace('\n','') for x in data]
            self.phone_book.clear()
            for line in data:
                self.phone_book.append(line.split(';'))

    def del_from_pb(self,position:int=-1):
        if position==-1:
            return []
        if  len(self.phone_book)-1<position or position<0:
            print ('-----------')
            return []

        del_date=self.phone_book[position]        
        self.phone_book.pop(position)
        return del_date 

    def search(self,search_str:str=''):
        
        if search_str=='':return []
        search_res=[]
        for line in self.phone_book:
            for field in line:
                if search_str in field:
                    search_res.append(line)
                    break
        return(search_res)

    def add_line(self,line:list=[] ):
        if len(line)<3: return[]
        if line[0]=='' or line[1]=='':return[]
        
        self.phone_book.append(line)
        return(line)

    def update_line(self,line:tuple):
        if line[0]<0 or line[0]>len(self.get_data()) or len(line[1])!=3:
            return 0
        else:
            for fild in range(3):
                self.phone_book[line[0]][fild]=line[1][fild]
            return 1

    def save_to_file(self):
        #  with open(self.path,encoding='UTF-8',mode='w') as file:
            pb_str=[]
            for line in self.phone_book:
                pb_str.append(';'.join(line))
            with open (self.path,'w',encoding='UTF-8') as file:
                pb_str=file.write('\n'.join(pb_str))







