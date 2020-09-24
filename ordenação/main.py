from sorting import selection_sort, insertion_sort, mergesort, quicksort
from Selects import ReadList, SelectMethod
import timeit

if __name__ == "__main__":

    lista = ReadList()  
    choice = SelectMethod() 
    time=0.0

    print("\n*******************************\n")
    for dados in lista:
        print(dados)
    print("*******************************")
    
    #ordenando dados:
    if ( (choice) == 0):
      time1 = timeit.default_timer()
      insertion_sort(lista)
      time2 = timeit.default_timer()
    elif( (choice) == 1):
        selection_sort(lista)
    elif( (choice) == 2):
        mergesort (lista)
    else:
        quicksort(lista)

    print("\n\n Ordenado:\n")
    for dados in lista:
        print(dados)
    print("*******************************")
    print(time2 - time1)

