import csv
from csv import writer


def delete_people():
    request = input("Введите данные для удаления: ")
    
    with open('company_directory.csv', 'r', encoding = 'utf_8') as inp:
        newrows = []
        data = csv.reader(inp)
        for row in data:
            if request not in row:
                newrows.append(row)
    with open('company_directory.csv', 'w', encoding = 'utf_8') as out:
        csv_writer = writer(out)
        for row in newrows:
            csv_writer.writerow(row)
        print(f' Строка со значением {request} удалена')


    return request