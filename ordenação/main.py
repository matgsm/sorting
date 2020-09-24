from sorting import selection_sort, insertion_sort, mergesort, quicksort
from Selects import ReadList, SelectMethod
import timeit

import sys
sys.setrecursionlimit(10**4)
#quantidade de recursão padrao do python estava sendo excedida, portanto foi aumentada

if __name__ == "__main__":

    lista = ReadList()  
    choice = SelectMethod() 
    time=0.0

    print("\n*********************************************************************************************")
    for dados in lista:
        print(dados)
    print("*********************************************************************************************")
    
    #ordenando dados:
    
    time1 = timeit.default_timer()
    if ( (choice) == 0):
      insertion_sort(lista)
    elif( (choice) == 1):
        selection_sort(lista)
    elif( (choice) == 2):
        mergesort (lista)
    else:
        quicksort(lista)
    time2 = timeit.default_timer()
    print("\n\n\tOrdenado:\n\n")
    print("*********************************************************************************************")
    for dados in lista:
        print(dados)
    print("*********************************************************************************************")
    print("\ntempo para ordenar: ",(time2 - time1))

