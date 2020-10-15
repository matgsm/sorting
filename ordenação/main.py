from Selects import ( SelectList, ReadList, SelectSort, BestSorting, SortList,
                      SelectSearch, SearchList, Interface, PrintList, print_status  )

from menu import menu
import timeit
import sys

sys.setrecursionlimit(10**4)
#quantidade de recursão padrao do python estava sendo excedida, portanto foi aumentada de 10^3 para 10^4


if __name__ == "__main__":
    CompMovTime = []

    list_name = SelectList()
    list = ReadList (list_name.path)   #caminho completo de list_name
    PrintList(list,"Original List")
    sorted = False  #Lista não ordenada

    option = Interface(1)

    while (option > 0):
        if (option == 1):           #sorting
            sort_name = SelectSort()
            if(sort_name.choice == sort_name.Last() ):
                sort_name.choice = BestSorting(list, sort_name)   #método mais rápido

            CompMovTime = SortList(sort_name, list) #ordenando
            PrintList (list,"Lista ordenada")
            print_status (list_name, sort_name, CompMovTime)
            sorted = True   #Lista Ordenada

        elif (option == 2):         #searching
            search_name = SelectSearch()
            SearchList (list.copy(), search_name.choice, sorted)

        elif (option == 3):         #switch list
            list_name = SelectList()
            list = ReadList(list_name.path )
            PrintList(list,"Lista original")
            sorted = False  #Lista não ordenada

        option = Interface()
