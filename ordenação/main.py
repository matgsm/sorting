from Selects import ( SelectList, ReadList, SelectSort, BestSorting, SortList,
                      SelectSearch, SearchList, Interface, PrintList  )

from menu import menu
from Monitor import Monitor
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
            Best = None
            sort_name = SelectSort()
            if(sort_name.choice == sort_name.Last() ):
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
            search_name = SelectSearch()
            SearchList (list.copy(), search_name.choice, sorted)

        elif (option == 3):         #switch list
            list_name = SelectList()
            list = ReadList(list_name.path )
            PrintList(list,"Lista original")
            sorted = False  #Lista não ordenada

        option = Interface()
