import timeit
import sys
from use_list import select_list, read_list, print_list
from use_sorting import select_sort, best_sorting, sort_list
from use_search import select_search, list_information, search_list
from menu import Menu, interface
from monitor import Monitor
sys.setrecursionlimit(10**4)

ALWAYS_ORDERED = False

if __name__ == "__main__":

    list_name = select_list()            #Cria o Menu de seleção de listas
    list = read_list (list_name.path)
    print_list(list,"Original List")
    sorted = ALWAYS_ORDERED

    first = True    #primeira execução
    option = interface(first)
    #option: [0]Sair; [1]ordenar; [2]Buscar; [3]imprimir lista

    while (option > 0):
        if (option == 1):#sorting
            relatorio = Monitor()
            best = None

            sort_name = select_sort()
            #sort_name: [0]insertion_sort; [1]selection_sort; [2]mergesort
            #           [3]quicksort; [4]Fastest_Method
            if(sort_name.choice == sort_name.last() ):  #if Fastest_Method
                best = best_sorting(list, sort_name)
                sort_name.choice = best.ind

            relatorio = sort_list(sort_name.choice, list) #ordenando
            print_list (list,"Lista ordenada")
            sorted = True   #Lista Ordenada

            list_name.print_choice()
            sort_name.print_choice()
            relatorio.status()
            if (best is not None):
                best.time_best()

        elif (option == 2):#searching
            cp_list = list.copy()   # NÃO modifica a lista original
            search_name = select_search()    #search_name: [0]Linear; [1]binaria

            if ( (search_name.choice == 1) and (sorted == False) ):
                sorted = list_information(cp_list, sorted)
                #busca mais dados sobre a lista

            search_list (cp_list, search_name.choice)
            #faz a busca

        elif (option == 3):
             print_list(list,"Lista salva em memoria: ")

        elif (option == 4):         #switch list
            list_name = select_list()
            list = read_list(list_name.path )
            print_list(list,"Lista original")
            sorted = ALWAYS_ORDERED

        first = False       #demais execuções do menu
        option = interface(first)
        #option: [0]Sair; [1]ordenar; [2]Buscar; [3]imprimir lista; [4]Nova lista
