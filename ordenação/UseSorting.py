import timeit
from menu import menu
from Monitor  import Monitor
from sorting import insertion_sort, selection_sort, mergesort, quicksort

def SelectSort():

    alternatives =  [ ["insertion_sort"], ["selection_sort"],
                    ["mergesort"], ["quicksort"],
                    #["bubble_sort"],
                    ["Fastest_Method"]     ]

    f1 = "\nSelecione um método de ordenação: "
    f2 = "\nNúmero do método desejado: "
    f3 = "Metodo de ordenação escolhido: "
    frases = [f1, f2, f3]

    method = menu (alternatives, frases)
    method.PrintChoice()
    return (method)


def BestSorting(list, method):
    Best = monitor()
    BestChoice = 0

    time1 = timeit.default_timer()
    for i in range ( 0 , len(method.alternatives)-1 ):
        if (i==0):
            Best = SortList ( 0 , list.copy() )
            BestChoice = 0
        else:
            T = SortList ( i , list.copy() )
            if( T.time < Best.time ):		#compara apenas o tempo
                Best = T
                BestChoice = i
    time2 = timeit.default_timer()

    Best.sec_time = (time2 - time1)
    Best.text = "\nTempo para ordenar dados por esse metodo:"
    Best.ind = BestChoice

    Best.status()
    return (Best)


#****************************************#

def SortList (choice,lista):

    #classe Monitor gera objetos relatorio
    time1 = timeit.default_timer()
    if ( (choice) == 0):
        relatorio = insertion_sort(lista)
    elif( (choice) == 1):
        relatorio = selection_sort(lista)
    elif( (choice) == 2):
        relatorio = mergesort (lista)
    elif( (choice) == 3):
        relatorio = quicksort(lista)
#    else:
#        CompMov = bubble_sort(lista)
    time2 = timeit.default_timer()      #(time2)-(time1)

    relatorio.time = (time2 - time1)
    relatorio.text = "\nTempo para ordenar dados: "
    return(relatorio )
