import csv

with open('crescente.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    fname = []
    i=0
    for row in csv_reader:
        x = row[0]
        fname.append(x)
    
    print (fname)

        
