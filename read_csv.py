import csv

with open("birthdays.csv", "r") as f:
    for row in csv.reader(f):
        print(row)

with open("birthdays.csv", "r") as f:
    for row in csv.DictReader(f):
        print(row['name'], row['age'])

