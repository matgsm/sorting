import timeit
from menu import menu
from Monitor  import Monitor
from search import linear_search, binary_search
from sorting import mergesort
from UseList import PrintList


def SelectSearch():     #Menu de buscas

    alternatives =  [ ["Linear Search"], ["Binary Search"] ]
    f1 = "\nSelecione um método de busca: "
    f2 = "\nNúmero do método desejado: "
    f3 = "Metodo de busca escolhido: "
    frases = [f1, f2, f3]

    search_method = menu (alternatives, frases)
    search_method.PrintChoice()
    return (search_method)

#************************************************************************#

def SearchList (list,method):    #busca elemento na lista

    again = 1
    while (again == 1):

        name = str( input("\nNome para pesquisar na lista: ") )

        relatorio = Search (list, name, method)
        indice = relatorio.ind
        PrintSearch (list,relatorio, indice)

        again = MoreSearch()

#************************************************************************#

def Search (list, name, method):
    time1 = timeit.default_timer()
    if (method == 0):                   #linear_search
        relatorio = linear_search (list,name)

    else:                               #binary_search
        relatorio = binary_search (list, name)
    time2 = timeit.default_timer()

    relatorio.time = time2 - time1
    relatorio.text = "\nTempo para buscar dado: "
    return (relatorio)

#************************************************************************#

def PrintSearch(list, relatorio, indice):
        if ( indice is not None ):
            print ("\nIndice encontrado: ", indice)
            print (list[indice])
            relatorio.status()
        else:
            print("\nElemento nao encontrado.")
            relatorio.status()

#************************************************************************#

def ListInformation(list, sorted):

            #Menu: lista está ordenada? levanta mais dados sobre a lista
            alternatives = [ ["Sim, lista esta ordenada."],
                             ["Não, lista não está ordenada."],
                             ["Não sei se a lista está ordenada"]   ]

            f1 = "\nA lista está ordenada? "
            f2 = "\nResposta: "
            f3 = ""
            frases = [f1,f2,f3]

            info_list = menu(alternatives, frases)
            info_list.PrintChoice()

            if(info_list.choice == 0):    #lista ordenada
                sorted = True
                return (sorted) #lista original está ordenada

            else:
                mergesort (list)
                PrintList (list,"Lista ordenada")
                print("\nLista ordenada automaticamente para a busca binária")
                #Apenas a lista copiada para a busca binaria está Ordenada
                #A lista original continua desordenada
                sorted = False
                return (sorted)

#************************************************************************#

def MoreSearch():           #Menu: nova busca?

        alternatives = ["Encerrar busca", "Nova busca"]     #again
        f1 = "\nOpções disponíveis: "
        f2 = "\nOpção desejada: "
        f3 = "Opção escolhida: "
        frases = [f1, f2, f3]

        again = menu(alternatives, frases)
        again.PrintChoice()
        return (again.choice)
