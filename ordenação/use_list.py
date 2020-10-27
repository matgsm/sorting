from os import listdir
from os.path import isfile, join
import csv
from menu import Menu

def select_list():       #Menu seleção de listas

    path = './logs/'
    alternatives =  [f for f in listdir(path) if isfile(join(path, f))]
                    #armazena nome dos arquivos presentes em ./logs

    f1 = "\nEscolha a lista de logs desejada: "
    f2 = "\nNumero da lista: "
    f3 = "Lista de logs selecionada: "
    frases = [f1, f2, f3]               #frases personalizadas

    list_name = Menu (alternatives, frases, path)   #cria o Menu
    list_name.print_choice()
    return (list_name)

#************************************************************************#

def read_list(list_name):

    with open(list_name) as csv_file:   #percorre a lista segundo o formato .csv
        list_person = []  #lista lida
        csv_reader = csv.reader(csv_file, delimiter=',')
        csv_reader.__next__()           #desconsiderar os cabeçalhos
        for row in csv_reader:
            person = row                #cada linha tem os dados de uma pessoa
            list_person.append(person)
        return(list_person)                   #retorna a lista de pessoas

#************************************************************************#

def print_list (list, legend=""):
    print ("\n\n\t%s\n\n" %(legend) )
    print("**********" * 10)
    for dados in list:
        print(dados)        #imprime a lista
    print("**********" * 10,"\n")

#************************************************************************#

def list_information(list):

        #Menu: lista está ordenada? levanta mais dados sobre a lista
        alternatives = [ ["Não, não sei ou lista não está ordenada."],
                         ["Sim, lista está ordenada."]   ]

        f1 = "\nA lista está ordenada? "
        f2 = "\nResposta: "
        f3 = ""
        frases = [f1,f2,f3]

        info_list = Menu(alternatives, frases)
        info_list.print_choice()

        if(info_list.choice == 1):    #lista ordenada
            sorted = True
            return (sorted) #lista original está ordenada

        else:
            sorted = False
            return (sorted)
