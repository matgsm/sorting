from sorting import selection_sort, insertion_sort, mergesort, quicksort, bubble_sort
from menu import menu
import csv
from os import listdir
from os.path import isfile, join
import timeit

TFastest = 0

def SelectList():

    path = './logs/'
    lists = [f for f in listdir(path) if isfile(join(path, f))]

    f1 = "\nEscolha a lista de logs desejada: "
    f2 = "\nNumero da lista: "
    f3 = "Lista de logs selecionada: "
    frases = [f1, f2, f3]

    list_name = menu(lists, frases, path)   #Recebe como retorno a lista escolhida pelo usuario
    list_name.PrintChoice()
    return (list_name)
#************************************************************************#

def ReadList(list_name):
    with open(list_name) as csv_file:   #percorre a lista segundo o formato .csv
        fname = []  #lista lida
        csv_reader = csv.reader(csv_file, delimiter=',')
        csv_reader.__next__()           #avança uma linha para desconsiderar os cabeçalhos ex:first_name)
        for row in csv_reader:
            person = row                #cada linha tem os dados de uma pessoa, independe da qtd de linhas ou colunas
            fname.append(person)
        return(fname)                   #retorna uma lista segundo o formato .csv independente do numero de colunas

#************************************************************************#

def SelectMethod():     #imprime metodos de ordenação para o usuario e retorna o indice do metodo escolhido
    global method

    methods = [ ["insertion_sort"], ["selection_sort"],
                ["mergesort"], ["quicksort"],
                ["bubble_sort"], ["Fastest_Method"]     ]

    f1 = "\nSelecione um método de ordenação: "
    f2 = "\nNúmero do método desejado: "
    f3 = "Metodo de ordenação escolhido: "
    frases = [f1, f2, f3]

    method = menu(methods, frases)
    method.PrintChoice()
    return (method)

#************************************************************************#

def BestSorting(CopList):
    global TFastest
    Best = []
    BestChoice = 0

    time1 = timeit.default_timer()
    for i in range ( 0 , len(method.alternatives)-1 ):
        if (i==0):
            Best = SortList ( 0 , CopList.copy() )
            BestChoice = 0
        else:
            T = SortList ( i , CopList.copy() )
            if( T[2] < Best[2] ):		#compara apenas o tempo
                Best = T
                BestChoice = i
    time2 = timeit.default_timer()
    TFastest = (time2 - time1)

    print("\n\nMelhor metodo para ordenação: ", method.alternatives[BestChoice]  )
    print("Tempo gasto para ordenar por esse metodo: ", Best[2] )
    print("Comparações: ", Best[0])                 #imprime qtd de comparações
    print("Movimentações: ", Best[1])                 #imprime qtd de movimentações
    print("Tempo para escolher melhor metodo: ", TFastest )
    return (BestChoice)

def TBest_Method():
    global TFastest
    if (TFastest != 0):
        print("Tempo para escolher melhor metodo: ", TFastest )


#************************************************************************#

def SortList (choice,lista):
    time1 = timeit.default_timer()
    if ( (choice) == 0):
        CompMov = insertion_sort(lista)
    elif( (choice) == 1):
        CompMov = selection_sort(lista)
    elif( (choice) == 2):
        CompMov = mergesort (lista)
    elif( (choice) == 3):
        CompMov = quicksort(lista)
    else:
        CompMov = bubble_sort(lista)
    time2 = timeit.default_timer()      #(time2)-(time1) determina o tempo de ordenação independente do metodo
    return(CompMov[0], CompMov[1],(time2 - time1) )

#coment adding in atom
