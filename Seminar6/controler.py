
import view as viewer
import model


def start ():
    my_pb = model.PhoneBook('my_pb.css')
    ask=''
    the_end=0    
    while the_end ==0:
        viewer.show_menu()
        ask=input('\nВыберите действие? ')
        match ask:
            case '1': #ПОКАЗАТЬ ТК

                # Показываем Телефонную книгу
                viewer.show_pb(my_pb.get_data())
                
            case '2': #ЗАГРУЗИТЬ ТК ИЗ ФАЙЛА

                # Загрузаем загружаем базу из файла
                # Показываем сообщение о результате загрузки
                my_pb.load()
                viewer.load_sucsess()

            case '3': #ЗАПИСАТЬ ТК ИЗ ФАЙЛА
                
                my_pb.save_to_file()
                viewer.save_msg
            case '4':#ДОБАВИТЬ ЗАПИСЬ В ТК

                # Запрвшиваем данные для добавления                
                # Добавляем данные
                # Выводим результат добавления                
                viewer.add_line_resaullt(my_pb.add_line(viewer.add_line_ask()))

            case '5': #ИЗМЕНИТЬ ДАННЫЕ
                # Выбрать запись/(и) для изменения, измения и передать ее для изменения                 
                # Подтвердить результат                
                # Вывеси результат изменения
                
                viewer.update_msg(my_pb.update_line(viewer.update_viewer(my_pb.get_data())))

            case '6': #УДАЛИТЬ ЗАПИСЬ ИЗ ТК

                # Выдаем список из чего удалять
                # Запрашиваем что удалять
                # Удаляем
                # Выдаем результат удаления
               viewer.show_deldate(my_pb.del_from_pb(viewer.show_del_date_menu(my_pb.get_data())))

            case '7':#НАЙТИ ЗАПИСИ В ТК ПО ЗАПРОШЕННОМУ ТЕКСТУ
                
                # Запрашиваем что искать
                # Выдаем результат
                search_str=viewer.search_str()                
                viewer.show_pb(my_pb.search(search_str),f'CОВПАДЕНИЯ ПО \'{search_str}\'')

            case '8': #ЗАВЕРШИТЬ ВЫПОЛНЕНИЕ

                # Выдаем сообщение о завершении выполнения
                # Прекращаем работу
                viewer.stop_work()
                the_end=1





