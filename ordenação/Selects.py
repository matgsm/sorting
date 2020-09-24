import csv
from os import listdir
from os.path import isfile, join


def SelectList():
    path = './logs/'
    files = [f for f in listdir(path) if isfile(join(path, f))]
    print("\nEscolha a lista de logs desejada: ")
    for index,item in enumerate (files):
        print("%d) %s" %(index,item) )
    N_lista =  int( input ("\nNumero da lista: ") )
    if ( (N_lista < len(files) )  and (N_lista >= 0) ):
        list_name = path + files[N_lista]
        return (list_name)
    else:
        print("\n%d não é uma opção. Tente novamente:" %N_lista)
        return ( SelectList() )


def ReadList():
    list_name = SelectList()
    print ("\nLista de logs selecionada: ",list_name)
    with open(list_name) as csv_file:
        fname = []  #lista lida
        csv_reader = csv.reader(csv_file, delimiter=',')
        csv_reader.__next__()
        for row in csv_reader:
            x = [ [row[0] ], [row[1] ], [row[2] ], [row[3] ], [row[4] ] ]
            fname.append(x)
        return(fname)

def SelectMethod():
    methods = [ ["insertion_sort"], ["selection_sort"],["mergesort"], ["quicksort"] ]
    print ("\nSelecione um método de ordenação: ")
    for index,sort in enumerate (methods):
        print ("%d) %s" %(index,sort) )
    choice = int(input("\nNúmero do método desejado: ") )

    if ( (choice < len(methods) )  and (choice >= 0) ):
        print("\nMetodo de ordenação escolhido: ", methods[choice])
        return (choice)
    else:
        print("\n%d não é uma opção. Tente novamente:" %choice)
        return ( SelectMethod() )

