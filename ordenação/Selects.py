from sorting import selection_sort, insertion_sort, mergesort, quicksort, bubble_sort
import csv
from os import listdir
from os.path import isfile, join
import timeit

list_name = ""
methods = [ ["insertion_sort"], ["selection_sort"],["mergesort"], ["quicksort"], ["bubble_sort"], ["Fastest_Method"] ]
TFastest = 0

def SelectList():       #imprime listas disponiveis para o usuario e retorna a lista escolhida
    global list_name
    path = './logs/'
    files = [f for f in listdir(path) if isfile(join(path, f))]     #armazena em "files" o nome das listas em ./logs
    print("\nEscolha a lista de logs desejada: ")
    for index,item in enumerate (files):
        print("%d) %s" %(index,item) )              #imprime indices associados a listas ex: 2) random-5000.csv
    N_lista =  int( input ("\nNumero da lista: ") )
    if ( (N_lista < len(files) )  and (N_lista >= 0) ):
        list_name = path + files[N_lista]           # concatena o caminho (path) com o nome da lista (files[N_lista])
        return (list_name)
    else:
        print("\n%d não é uma opção. Tente novamente:" %N_lista)    #impede o usuario de escolher fora do intervalo
        return ( SelectList() )

def Print_ListName():
    global list_name
    print ("\nLista de logs selecionada: ",list_name)

#************************************************************************#

def ReadList():
    global list_name
    list_name = SelectList()   #Recebe como retorno a lista escolhida pelo usuario
    Print_ListName()

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
    global methods
    print ("\nSelecione um método de ordenação: ")
    for index,sort in enumerate (methods):          #imprime indices associados a metodos de ordenação (ex: "2) mergesort" )
        print ("%d) %s" %(index,sort) )
    choice = int(input("\nNúmero do método desejado: ") )

    if ( (choice < len(methods) )  and (choice >= 0) ):
        Print_Method(choice)
        return (choice)
    else:
        print("\n%d não é uma opção. Tente novamente:" %choice) #impede o usuario de escolher fora do intervalo
        return ( SelectMethod() )

def Print_Method(choice):
    global methods
    print("\nMetodo de ordenação escolhido: ", methods[choice])

def Return_Method(choice):
    global methods
    return (methods[choice])

def Last_Method():
    global methods
    return (len(methods)-1)
#obs: para a interação com o usuario, o programa aceita numeros, mas apresenta erros se forem recebidos letras ou carac. esp.

#************************************************************************#

def BestSorting(CopList):
    global TFastest
    Best = []
    BestChoice = 0

    time1 = timeit.default_timer()
    for i in range ( 0 , Last_Method() ):
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

    print("\n\nMelhor metodo para ordenação: ", Return_Method(BestChoice)  )
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
