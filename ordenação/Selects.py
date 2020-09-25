import csv
from os import listdir
from os.path import isfile, join

list_name = ""
methods = [ ["insertion_sort"], ["selection_sort"],["mergesort"], ["quicksort"] ]

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
        return(fname)                   #retorna uma lista ordenada segundo o formato .csv independente do numero de colunas


#************************************************************************#


def Print_Method(choice):
    global methods
    print("\nMetodo de ordenação escolhido: ", methods[choice])

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

#obs: para a interação com o usuario, o programa aceita numeros, mas apresenta erros se forem recebidos letras ou carac. esp.
