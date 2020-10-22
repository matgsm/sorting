import timeit
from menu import Menu
from monitor  import Monitor
from sorting import insertion_sort, selection_sort, merge_sort, quick_sort

def select_sort():

    alternatives =  [ ["insertion_sort"], ["selection_sort"],
                    ["mergesort"], ["quicksort"],
                    #["bubble_sort"],
                    ["Fastest_Method"]     ]

    f1 = "\nSelecione um método de ordenação: "
    f2 = "\nNúmero do método desejado: "
    f3 = "Metodo de ordenação escolhido: "
    frases = [f1, f2, f3]

    method = Menu (alternatives, frases)
    method.print_choice()
    return (method)


def best_sorting(list, method):
    best = Monitor()
    best_choice = 0

    time1 = timeit.default_timer()
    for i in range ( 0 , len(method.alternatives)-1 ):
        if (i==0):
            best = sort_list ( 0 , list.copy() )
            best_choice = 0
        else:
            aux = sort_list ( i , list.copy() )
            if( aux.time < best.time ):		#compara apenas o tempo
                best = aux
                best_choice = i
    time2 = timeit.default_timer()

    best.sec_time = (time2 - time1)
    best.text = "\nTempo para ordenar dados por esse metodo:"
    best.ind = best_choice

    best.status()
    return (best)


#****************************************#

def sort_list (choice,lista):

    #classe Monitor gera objetos relatorio
    time1 = timeit.default_timer()
    if ( (choice) == 0):
        relatorio = insertion_sort(lista)
    elif( (choice) == 1):
        relatorio = selection_sort(lista)
    elif( (choice) == 2):
        relatorio = merge_sort (lista)
    elif( (choice) == 3):
        relatorio = quick_sort(lista)
#    else:
#        CompMov = bubble_sort(lista)
    time2 = timeit.default_timer()      #(time2)-(time1)

    relatorio.time = (time2 - time1)
    relatorio.text = "\nTempo para ordenar dados: "
    return(relatorio )
