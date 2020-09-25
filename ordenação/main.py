from sorting import selection_sort, insertion_sort, mergesort, quicksort
from Selects import ReadList, Print_ListName, SelectMethod, Print_Method
import timeit
import sys

sys.setrecursionlimit(10**4)
#quantidade de recursão padrao do python estava sendo excedida, portanto foi aumentada de 10^3 para 10^4

if __name__ == "__main__":

    lista = ReadList()          #retorna a lista escolhida entre as presentes em ./logs 
    choice = SelectMethod()     #recebe o indice do metodo de ordenação desejado
    time=0.0

    print ("\n\n\tOriginal:\n\n")
    print("\n*********************************************************************************************")
    for dados in lista:
        print(dados)        #imprime a lista original
    print("*********************************************************************************************")
    
    #ordenando dados:
    
    time1 = timeit.default_timer()
    if ( (choice) == 0):
        CompMov = insertion_sort(lista)
    elif( (choice) == 1):
        CompMov = selection_sort(lista)
    elif( (choice) == 2):
        CompMov = mergesort (lista)
    else:
        CompMov = quicksort(lista)
    time2 = timeit.default_timer()      #(time2)-(time1) determina o tempo de ordenação independente do metodo

    print("\n\n\tOrdenado:\n\n")
    print("*********************************************************************************************")
    for dados in lista:
        print(dados)        #imprime a lista ordenada
    print("*********************************************************************************************")
    
    print("\ntempo para ordenar: ",(time2 - time1))     #imprime o tempo para ordenação
    Print_ListName()                                    #imprime o nome da lista
    Print_Method(choice)                                #imprime o metodo de ordenação
    print("\nComparações: ",CompMov[0])                 #imprime qtd de comparações
    print("Movimentações: ",CompMov[1])                 #imprime qtd de movimentações
