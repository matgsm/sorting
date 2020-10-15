from Selects import SelectList, ReadList, SelectMethod, BestSorting, SortList, TBest_Method
from menu import menu
from search import binary_search
import timeit
import sys

sys.setrecursionlimit(10**4)
#quantidade de recursão padrao do python estava sendo excedida, portanto foi aumentada de 10^3 para 10^4


if __name__ == "__main__":

    list_name = SelectList()          #retorna a lista escolhida entre as presentes em ./logs

    lista = ReadList(list_name.choice)

    method = SelectMethod()     #recebe o indice do metodo de ordenação desejado

    if(method.choice == len(method.alternatives)-1 ):     #ultima alternativa
        method.choice = BestSorting(lista)
    CompMov = []

    #lista original
    print ("\n\n\tOriginal:\n\n")
    print("**********")
    for dados in lista:
        print(dados)        #imprime a lista original
    print("**********")

    #ordenando dados:
    CompMovTime = []
    CompMovTime = SortList(method.choice, lista)

    #lista ordenada
    print("\n\n\tOrdenado:\n\n")
    print("**********")
    for dados in lista:
        print(dados)        #imprime a lista ordenada
    print("**********")

    print("\ntempo para ordenar: ",CompMovTime[2])                #imprime o tempo para ordenação
    list_name.PrintChoice()                                   #imprime o nome da lista
    method.PrintChoice()                               #imprime o metodo de ordenação
    print("\nComparações: ",CompMovTime[0])                 #imprime qtd de comparações
    print("Movimentações: ",CompMovTime[1])                 #imprime qtd de movimentações
    TBest_Method()

    again = 's'
    while (again == 's'):
        name = str( input("\nNome para pesquisar na lista ordenada: ") )
        i = binary_search(lista, name)
        if ( i is not None ):
            print ("\nindice encontrado: ", i)
            print (lista[i])
            again = input("Repetir (S/N): ").lower()
