import model 
import view


def start (journal:model.My_journal):
    my_str=''
    view.ask_class(journal.get_class())

    journal.print_data()


