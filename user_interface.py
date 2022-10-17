import user_interface as user
from import_data import input_people as write
from export_data import output_people as exphum
from export_data import output_job as expjob
from export_data import output_salary as expsal
from change_data import change_elem as chel
from delete_data import delete_people as delhum

print()
while True:
    print("Вас приветствует справочник компании!")
    print\
    (f'Меню:\n'
       '1 - добавить сотрудника;\n'
       '2 - поиск сотрудника;\n'
       '3 - поиск сотрудника по должности;\n'
       '4 - поиск сотрудника по зарплате;\n'
       '5 - изменить данные сотрудника;\n'
       '6 - удалить сотрудника;\n'
       '7 - выход.\n'
    )
    ch = input("Введите команду: ")
   
    if ch == '1':
        user.write()
    elif ch == '2':
        user.exphum()
    elif ch == '3':
        user.expjob()
    elif ch == '4':
        user.expsal()
    elif ch == '5':
        user.chel()
    elif ch == '6':
        user.delhum()
    elif ch == '7':
        print("Сеанс окончен, до свидания!")
        exit()
    else:
        print("Введите корректную цифру!")
  
    
    




