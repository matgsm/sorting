from Selects import ReadList, Print_ListName, SelectMethod, Print_Method, Return_Method, BestSorting, SortList, Last_Method
import timeit
import sys

sys.setrecursionlimit(10**4)
#quantidade de recursão padrao do python estava sendo excedida, portanto foi aumentada de 10^3 para 10^4



if __name__ == "__main__":

    lista = ReadList()          #retorna a lista escolhida entre as presentes em ./logs 
#    listaCopy = lista.copy()
    choice = SelectMethod()     #recebe o indice do metodo de ordenação desejado
    if(choice == Last_Method() ):
        choice = BestSorting(lista)
#    time=0.0
    CompMov = []

    print ("\n\n\tOriginal:\n\n")
    print("\n*********************************************************************************************")
    for dados in lista:
        print(dados)        #imprime a lista original
    print("*********************************************************************************************")
    
    #ordenando dados:
        

    
    print("\n\n\tOrdenado:\n\n")
    CompMovTime = []
    CompMovTime = SortList(choice,lista)
    print("*********************************************************************************************")
    for dados in lista:
        print(dados)        #imprime a lista ordenada
    print("*********************************************************************************************")
    
    print("\ntempo para ordenar: ",CompMovTime[2])                #imprime o tempo para ordenação
    Print_ListName()                                    #imprime o nome da lista
    Print_Method(choice)                                #imprime o metodo de ordenação
    print("\nComparações: ",CompMovTime[0])                 #imprime qtd de comparações
    print("Movimentações: ",CompMovTime[1])                 #imprime qtd de movimentações

#    print("\n\nAnalisando melhor metodo de ordenação: ...")
#    BestSorting(listaCopy)
