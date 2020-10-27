import timeit
import sys
from use_list import select_list, read_list, print_list, list_information
from use_sorting import select_sort, best_sorting, sort_list
from use_search import select_search, search_list
from menu import Menu, interface
from monitor import Monitor
sys.setrecursionlimit(10**4)

ALWAYS_ORDERED = False

if __name__ == "__main__":

    #Constantes para sort_name:
    INSERTION_SORT = 0
    SELECTION_SORT = 1
    MERGE_SORT = 2
    QUICK_SORT = 3
    FASTEST_METHOD = 4  #last

    #Constantes para search_name:
    LINEAR = 0
    BINARIA = 1

    list_name = select_list()            #Menu de seleção de listas
    list = read_list (list_name.path)
    print_list(list,"Original List")

    #buscar mais dados sobre a lista
    if (ALWAYS_ORDERED is True):
        sorted = ALWAYS_ORDERED
    else:
        sorted = list_information(list)



    first = True    #primeira execução
    option = interface(first)
    #option: [0]Sair; [1]ordenar; [2]Buscar; [3]imprimir lista



    while (option > 0):
        if (option == 1):#sorting
            relatorio = Monitor()
            best = None

            sort_name = select_sort()



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
            search_name = select_search()

            if ( (search_name.choice == BINARIA) and (sorted == False) ):
                cp_list = list.copy()
                relatorio = sort_list(MERGE_SORT, cp_list) #ordenando
                print_list (cp_list,"Lista ordenada")
                print("Lista ordenada automaticamente apenas para a busca binária.\n")
                relatorio.status()
                search_list (cp_list, search_name.choice)
                del cp_list
            else:
                search_list (list, search_name.choice)

        elif (option == 3):
             print_list(list,"Lista salva em memoria: ")

        elif (option == 4):         #switch list
            del list
            list_name = select_list()
            list = read_list(list_name.path )
            print_list(list,"Lista original")
            if (ALWAYS_ORDERED is True):    #buscar mais dados sobre a lista
                sorted = ALWAYS_ORDERED
            else:
                sorted = list_information(list)

        first = False       #demais execuções do menu
        option = interface(first)
        #option: [0]Sair; [1]ordenar; [2]Buscar; [3]imprimir lista; [4]Nova lista
