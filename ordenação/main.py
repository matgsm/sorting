from sorting import selection_sort, insertion_sort, mergesort, quicksort
from Selects import ReadList, Print_ListName, SelectMethod, Print_Method, Return_Method
import timeit
import sys

sys.setrecursionlimit(10**4)
#quantidade de recursão padrao do python estava sendo excedida, portanto foi aumentada de 10^3 para 10^4



if __name__ == "__main__":

    lista = ReadList()          #retorna a lista escolhida entre as presentes em ./logs 
    CopList = lista.copy()
    choice = SelectMethod()     #recebe o indice do metodo de ordenação desejado
    time=0.0
    CompMov = []

    print ("\n\n\tOriginal:\n\n")
    print("\n*********************************************************************************************")
    for dados in lista:
        print(dados)        #imprime a lista original
    print("*********************************************************************************************")
    
    #ordenando dados:
        
    def SortList (choice, lista):
        global CompMov
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
        return(time2 - time1)
    
    print("\n\n\tOrdenado:\n\n")
    time = SortList(choice,lista)
    print("*********************************************************************************************")
    for dados in lista:
        print(dados)        #imprime a lista ordenada
    print("*********************************************************************************************")
    
    print("\ntempo para ordenar: ",time)                #imprime o tempo para ordenação
    Print_ListName()                                    #imprime o nome da lista
    Print_Method(choice)                                #imprime o metodo de ordenação
    print("\nComparações: ",CompMov[0])                 #imprime qtd de comparações
    print("Movimentações: ",CompMov[1])                 #imprime qtd de movimentações
    print("\nAnalizando metodo de ordenação mais rápido: ...")
    def BestSorting():
        global CopList    
        BestTime = 0.0 
        BestChoice = 0

        for i in range (0,4):
            CopList2 = CopList.copy()
            if (i==0):
                BestTime = SortList(0,CopList2)
                BestChoice = 0
            else:
                T = float( SortList(i,CopList2) )
                if(T < BestTime):
                    BestTime = T
                    BestChoice = i        
        print("\n\nMelhor metodo para ordenação: ",Return_Method(BestChoice)  )
        print("Tempo gasto para ordenar por esse metodo: ",BestTime )
    
    Best = BestSorting()
