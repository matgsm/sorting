import timeit
from menu import Menu
from monitor  import Monitor
from search import linear_search, binary_search
from sorting import merge_sort
from use_list import print_list


def select_search():     #Menu de buscas

    alternatives =  [ ["Linear Search"], ["Binary Search"] ]
    f1 = "\nSelecione um método de busca: "
    f2 = "\nNúmero do método desejado: "
    f3 = "Metodo de busca escolhido: "
    frases = [f1, f2, f3]

    search_method = Menu (alternatives, frases)
    search_method.print_choice()
    return (search_method)

#************************************************************************#

def search_list (list,method):    #busca elemento na lista

    again = 1
    while (again == 1):

        name = str( input("\nNome para pesquisar na lista: ") )

        relatorio = search (list, name, method)
        print_search (list,relatorio)

        again = more_search()

#************************************************************************#

def search (list, name, method):
    time1 = timeit.default_timer()
    if (method == 0):                   #linear_search
        relatorio = linear_search (list,name)

    else:                               #binary_search
        relatorio = binary_search (list, name)
    time2 = timeit.default_timer()

    relatorio.time = time2 - time1
    relatorio.text = "Tempo para buscar dado: "
    return (relatorio)

#************************************************************************#

def print_search(list, relatorio):

    indice = relatorio.ind
    if ( indice is not None ):
        print("\n")
        print("**********"*10)
        print ("\nIndice encontrado: ", indice)
        print (list[indice])
        relatorio.status()
    else:
        print("\n")
        print("**********"*10)
        print("\nElemento nao encontrado.")
        relatorio.status()

#************************************************************************#

def more_search():           #Menu: nova busca?

    alternatives = ["Encerrar busca", "Nova busca"]     #again
    f1 = "\nOpções disponíveis: "
    f2 = "\nOpção desejada: "
    f3 = "Opção escolhida: "
    frases = [f1, f2, f3]

    again = Menu(alternatives, frases)
    again.print_choice()
    return (again.choice)
