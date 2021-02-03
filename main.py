import re
import csv
from pymongo import MongoClient
from datetime import datetime


client = MongoClient()
db = client.tickets_db
ticket_db = db.ticket




def read_file(csv_file, db):
    with open(csv_file, encoding='UTF-8') as csv_file:
        rows_list = list()
        reader = csv.DictReader(csv_file)
        for row in reader:
            row = dict(row)
            row['Цена'] = int(row['Цена'])
            row['Дата'] += '.2022'
            row['Дата'] = datetime.strptime(row['Дата'], '%d.%m.%Y')
            rows_list.append(row)
        db.insert_many(rows_list)

def find_cheapest(db):
    sorted_list = list(database.find().sort('Цена', 1))
    for item in sorted_list:
        print(f'{item["Исполнитель"]}, {item["Цена"]} рублей,'
              f' {item["Место"]}, {item["Дата"]}')

def find_by_name(name, db):
    name = re.escape(name)
    regex = re.compile(name)
    sorted_list = list(database.find({'Исполнитель': regex}).sort('Цена', 1))
    print(f'Найдено мероприятий: {len(sorted_list)}')
    for item in sorted_list:
        print(f'{item["Исполнитель"]}, {item["Цена"]} рублей,'
              f' {item["Место"]}, {item["Дата"]}')


if __name__ == '__main__':

    read_file('artists.csv', ticket_db)
    find_cheapest(ticket_db)
    find_by_name('t', ticket_db)
