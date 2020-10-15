from sorting import selection_sort, insertion_sort, mergesort, quicksort, bubble_sort
from menu import menu
from search import binary_search, linear_search
import csv
from os import listdir
from os.path import isfile, join
import timeit

TFastest = 0

def SelectList():

    path = './logs/'
    alternatives = [f for f in listdir(path) if isfile(join(path, f))]
                    #armazena nome dos arquivos presentes em ./logs

    f1 = "\nEscolha a lista de logs desejada: "
    f2 = "\nNumero da lista: "
    f3 = "Lista de logs selecionada: "
    frases = [f1, f2, f3]

    list_name = menu (alternatives, frases, path)
    list_name.PrintChoice()
    return (list_name)
#************************************************************************#

def ReadList(list_name):
    with open(list_name) as csv_file:   #percorre a lista segundo o formato .csv
        list_person = []  #lista lida
        csv_reader = csv.reader(csv_file, delimiter=',')
        csv_reader.__next__()           #desconsiderar os cabeçalhos
        for row in csv_reader:
            person = row                #cada linha tem os dados de uma pessoa
            list_person.append(person)
        return(list_person)                   #retorna a lista de pessoas

#************************************************************************#

def PrintList (list, legend=""):
    print ("\n\n\t%s\n\n" %(legend) )
    print("**********" * 10)
    for dados in list:
        print(dados)        #imprime a lista original
    print("**********" * 10)

#************************************************************************#

def Interface(begin=None):
    if (begin is not None):
        alternatives =[ ["Encerrar o programa"],
                        ["Escolher metodo para ordenação"],
                        ["Escolher metodo de busca"]        ]

        f1 = "\nOpções disponíveis: \n"
        f2 = "\nOpção desejada: "
        f3 = "Opção escolhida: "
        frases = [f1, f2, f3]

        option = menu (alternatives, frases)
        option.PrintChoice()
        return (option.choice)

    else:
        alternatives =[ ["Encerrar o programa"],
                        ["Escolher metodo para ordenação"],
                        ["Escolher metodo de busca"],
                        ["Escolher outra lista"]            ]   #new list?

        f1 = "\nOpções disponíveis: "
        f2 = "\nOpção desejada: "
        f3 = "Opção escolhida: "
        frases = [f1, f2, f3]

        option = menu (alternatives, frases)
        option.PrintChoice()
        return (option.choice)

#************************************************************************#

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

#************************************************************************#

def BestSorting(list, method):
    global TFastest
    Best = []
    BestChoice = 0

    time1 = timeit.default_timer()
    for i in range ( 0 , len(method.alternatives)-1 ):
        if (i==0):
            Best = SortList ( 0 , list.copy() )
            BestChoice = 0
        else:
            T = SortList ( i , list.copy() )
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
    CompMov = []
    time1 = timeit.default_timer()
    if ( (choice) == 0):
        CompMov = insertion_sort(lista)
    elif( (choice) == 1):
        CompMov = selection_sort(lista)
    elif( (choice) == 2):
        CompMov = mergesort (lista)
    elif( (choice) == 3):
        CompMov = quicksort(lista)
#    else:
#        CompMov = bubble_sort(lista)
    time2 = timeit.default_timer()      #(time2)-(time1) determina o tempo de ordenação independente do metodo

    return(CompMov[0], CompMov[1],(time2 - time1) )

#************************************************************************#

def SelectSearch():

    alternatives =  [ ["Linear Search"], ["Binary Search"] ]


    f1 = "\nSelecione um método de busca: "
    f2 = "\nNúmero do método desejado: "
    f3 = "Metodo de busca escolhido: "
    frases = [f1, f2, f3]

    search_method = menu (alternatives, frases)
    search_method.PrintChoice()
    return (search_method)

#************************************************************************#

def SearchList (list,method,sorted):
    if ( (sorted == False) and (method == 1) ):
        SortList(2, list)
        PrintList (list,"Lista ordenada")
        print("\nLista ordenada automaticamente para a busca binária")

    again = 1
    while (again == 1):
        name = str( input("\nNome para pesquisar na lista: ") )

        i = Search (list, name, method)

        if ( i is not None ):
            print ("\nIndice encontrado: ", i)
            print (list[i])
        else:
            print("\nElemento nao encontrado.")

        alternatives = ["Encerrar busca", "Nova busca"]     #again
        f1 = "\nOpções disponíveis: "
        f2 = "\nOpção desejada: "
        f3 = "Opção escolhida: "
        frases = [f1, f2, f3]

        again = menu(alternatives, frases)
        again.PrintChoice()
        again = again.choice
        #again = input("Repetir (S/N): ").lower()

#************************************************************************#

def Search (list, name, method):
    if (method == 0):                   #linear_search
        i = linear_search (list,name)

    elif(method == 1):                  #binary_search
        i = binary_search (list, name)

    return (i)

#************************************************************************#

def print_status(list_name, method, CompMovTime):
    print("\ntempo para ordenar: ",CompMovTime[2])                #imprime o tempo para ordenação
    list_name.PrintChoice()                                   #imprime o nome da lista
    method.PrintChoice()                               #imprime o metodo de ordenação
    print("\nComparações: ",CompMovTime[0])                 #imprime qtd de comparações
    print("Movimentações: ",CompMovTime[1])                 #imprime qtd de movimentações
    TBest_Method()
