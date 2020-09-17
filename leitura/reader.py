import csv

with open('crescente.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    len (csv_file)
    for row in csv_reader:
        print (row[0], row[1], row[2], row[3], row[4])

