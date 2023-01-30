import model 
import view


def start (journal:model.My_journal):
    
    is_end=0
    
    # Выбор класса
    class_number =view.ask_class_list(journal.get_class_number())
    
    # Выбор предмета
    classes=view.ask_classes(journal.get_classes())
    
    # Опрос
    while True:       
        
        # Выбор ученика
        id_puple=view.show_class_list(journal,class_number,classes)
        if id_puple==-1:
            # Сохранение данных
            journal.save_date()
            break        
        # Выбор оценки
        ask_number=view.show_ask_resault(journal,class_number,classes,id_puple)

        # Добавление оценки
        journal.add_ask(classes,id_puple,ask_number)



