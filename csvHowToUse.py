import csv

with open('trades.csv') as csvFile:
    readCsv = csv.reader(csvFile, delimiter = ',')

    names = []
    ages = []
    expertise = []
    for row in readCsv:
        first = row[0]
        second = row[1]
        third = row[2]
        names.append(first)
        ages.append(second)
        expertise.append(third)
print(names)
print(ages)
print(expertise)
try:
    question = input('say the name : ')
    if question in names:
        print()
        print('mr', question, 'is', ages[names.index(question.lower())],
              'years old, and he is', expertise[names.index(question.lower())])
    else:
        print(question,'is not in the names or you wrote ir wrong')
except Exception as e:
    print(e)
