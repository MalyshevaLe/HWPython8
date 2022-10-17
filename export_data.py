import csv

list_data = ['id', 'surname', 'name', 'job', 'phone_number', 'salary']

def output_people():
    surname = (input("Введите фамилию, которую необходимо найти: "))
    with open("company_directory.csv", 'r', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter=',')
        for line in reader:
            if surname in line:
                description = dict(zip(list_data, line))
                for key, value in description.items():
                    print(f'{key}: {value}')
    
    return surname

def output_job():
    job = (input("Введите должность, которую необходимо найти: "))
    with open("company_directory.csv", 'r', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter=',')
        for line in reader:
            if job in line:
                description = dict(zip(list_data, line))
                for key, value in description.items():
                    print(f'{key}: {value}')
    return job

def output_salary():
    salary = (input("Введите размер зарплаты, которую необходимо найти: "))
    with open("company_directory.csv", 'r', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter=',')
        for line in reader:
            if salary in line:
                description = dict(zip(list_data, line))
                for key, value in description.items():
                    print(f'{key}: {value}')
    
    return salary