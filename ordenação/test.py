import random
import csv
from sorting import selection_sort, bubble_sort, insertion_sort
from sorting import mergesort, quicksort

#fname
list_name = "decrescente-1000.csv"
with open(list_name) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    csv_reader.__next__()
    fname = []
    i=0
    for row in csv_reader:
        x = [ [row[0] ], [row[1] ], [row[2] ], [row[3] ], [row[4] ] ]
        fname.append(x)

any_numbers = random.sample(range(1, 1000), 42)

already_sorted = [1, 2, 3, 4, 5, 6, 9, 20, 22, 23, 28, 
                    32, 34, 39, 40, 42, 76, 87, 99, 112]

inversed = [117, 90, 88, 83, 81, 77, 74, 69, 64, 63, 51,
            50, 49, 42, 41, 34, 32, 29, 28, 22, 16, 8, 6, 5, 3, 1]

repeated = [7, 7, 7, 7, 7, 1, 1, 9, 9, 0, 4, 4, 4, 5, 4, 5, 7, 1,]

names = ["zeze", "joao", "zeca", "maria" , "pedro", "joana", "pablo", "matheus", "ana", "amanda"] 

if __name__ == "__main__":

    lista = fname  #select list to sort (any_numbers, already_sorted, inversed, repeated, names)
    print("\n*******************************\n")
    print(lista)

    insertion_sort(lista)       #select sorting method
#    selection_sort(lista)
#    mergesort (lista)
#    quicksort(lista)
    
    print("\n\n Ordenado:\n")
    print(lista)
    print("*******************************")
    print("\nlista ordenada: ", list_name)
