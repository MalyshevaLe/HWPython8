import csv

list_data = ['id', 'surname', 'name', 'job', 'phone_number', 'salary']

def input_people():
    record = [input(f'{i} :') for i in list_data]
    with open('company_directory.csv', 'a', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(record)

    print("Данные успешно записаны")
    return record