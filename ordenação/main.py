import timeit
import sys

from UseList import SelectList, ReadList, PrintList
from UseSorting import SelectSort, BestSorting, SortList
from UseSearch import SelectSearch, ListInformation, SearchList
from menu import menu, Interface
from Monitor import Monitor

sys.setrecursionlimit(10**4)
#quantidade de recursão padrao do python estava sendo excedida, portanto foi aumentada de 10^3 para 10^4


if __name__ == "__main__":

    list_name = SelectList()            #Cria o Menu de seleção de listas
    list = ReadList (list_name.path)   #Caminho completo de list_name
    PrintList(list,"Original List")
    sorted = False  #Lista não ordenada pelo programa
    #obs: lista pode estar ordenada previamente mas o programa nao sabe.

    first = True    #primeira execução
    option = Interface(first)   #cria o Menu

    #option: [0]Sair; [1]ordenar; [2]Buscar; [3]imprimir lista; [4]Nova lista
    while (option > 0):
        if (option == 1):           #sorting
            Best = None
            sort_name = SelectSort()    #Cria Menu com os metodos de ordenação
            if(sort_name.choice == sort_name.Last() ):  #Metodo mais rapido
                Best = BestSorting(list, sort_name)
                sort_name.choice = Best.ind

            relatorio = SortList(sort_name.choice, list) #ordenando
            PrintList (list,"Lista ordenada")
            sorted = True   #Lista Ordenada

            sort_name.PrintChoice()
            list_name.PrintChoice()
            relatorio.status()
            if (Best is not None):
                Best.time_best()

        elif (option == 2):         #searching
            cp_list = list.copy()   # NÃO modifica a lista original
            search_name = SelectSearch()    #search_name: [0]Linear; [1]binaria

            if ( (search_name.choice == 1) and (sorted == False) ):
                sorted = ListInformation(cp_list, sorted)
                #busca mais dados sobre a lista

            SearchList (cp_list, search_name.choice)
            #faz a busca

        elif (option == 3):
             PrintList(list,"Lista salva em memoria: ")

        elif (option == 4):         #switch list
            list_name = SelectList()
            list = ReadList(list_name.path )
            PrintList(list,"Lista original")
            sorted = False  #Lista não ordenada



        first = False       #demais execuções do menu
        option = Interface(first)   #cria o Menu
