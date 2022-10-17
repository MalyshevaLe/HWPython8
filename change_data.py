import csv
from dataclasses import replace

list_data = ['id', 'surname', 'name', 'job', 'phone_number', 'salary']

def change_elem():
    with open("company_directory.csv", "r", encoding='utf-8', newline='') as file:
        surname = input("Введите фамилию сотрудника, которого необходимо изменить: ")
        # with open("company_directory.csv", 'r', encoding='utf-8', newline='') as file:
        replacetext = ''
        # reader = csv.reader(file, delimiter=',')
        for line in file:
            # description = dict(zip(list_data, line))
            if surname in line:
                print\
                (f'что хотите изменить?:\n'
                'Если должность, введите 1:\n'
                'Если номер телефона, введите 2:\n'
                'Если размер зарплаты, введите 3:\n'
                )
                ask = (input())
                if ask == '1':
                    new_job = input('введите новую должность: ')
                    old_job = line.split(',')[3]
                    line = line.replace(old_job,new_job)
                elif ask == '2':
                    new_phone_number = input('введите новый номер телефона (пример 89111111111): ')
                    old_phone_number = line.split(',')[4]
                    line = line.replace(old_phone_number,new_phone_number)
                elif ask == '3':
                    new_salary = input('введите новый размер зарплаты: ')
                    old_salary = line.split(',')[5]
                    line = line.replace(old_salary,new_salary) + '\n'
            replacetext = replacetext + line
           
    with open('company_directory.csv', 'w', encoding='UTF8', newline='') as file:
        file.writelines(replacetext)
print("Данные успешно перезаписаны")
                
                    
                    
   