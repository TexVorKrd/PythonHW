import  model
import controler

# Реализация журнала через имитацию базы данных - каждая строка - отдельная таблица

my_scool=model.My_journal()
controler.start(my_scool)
