from sorting import selection_sort, insertion_sort, mergesort, quicksort
from Selects import ReadList, SelectMethod

if __name__ == "__main__":

    lista = ReadList()  
    choice = SelectMethod() 

    print("\n*******************************\n")
    for dados in lista:
        print(dados)
    print("*******************************")
    
    #ordenando dados:
    if ( (choice) == 0):
        insertion_sort(lista)
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

