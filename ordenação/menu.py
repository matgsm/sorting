class Menu:
    #atributes
    alternatives = []
    frases = ["\nEscolha: ", "\nResposta: ", ""]    #padrao
    path = ""
    choice = None

    #construtor
    def __init__(self, lista = [], textos=[], caminho=None):
        self.alternatives = lista
        self.path = caminho
        self.frases = textos
        if ( len(self.alternatives) > 0 ):
            self.choice = self.select_menu()
        else:
            print("\nNenhuma alternativa")
        if (caminho is not None):
            self.path = self.path + self.alternatives[self.choice]

    #Method 1
    def select_menu(self):
        print ( self.frases[0] )                #permite personalização de texto
        for index,choices in enumerate (self.alternatives):
            print ("%d) %s" %(index,choices) )  #Enumera as alternativas

        choice = int ( input(self.frases[1]) )  #permite personalização de texto

        #valida a escolha antes de retornar
        if ( (choice < len(self.alternatives) )  and (choice >= 0) ):
            return (choice)
        else:
            print("\n%d não é uma opção. Tente novamente:" %choice) #impede o usuario de escolher fora do intervalo
            return ( self.select_menu() )

    #Method 2
    def print_choice(self):
        print ( self.frases[2], self.alternatives [self.choice] )
        #permite personalização da mensagem padrao



    #Method 3
    def last(self):
        return ( len(self.alternatives) - 1 )

    #fim da classe

#************************************************************************#

def interface( first=False ):       #Menu controle

    if (first is True):     #primeira execução

        alternatives =[ ["Encerrar o programa"],
                        ["Escolher metodo para ordenação"],
                        ["Escolher metodo de busca"],
                        ["Imprimir a lista"]    ]

        f1 = "\nOpções disponíveis: \n"
        f2 = "\nOpção desejada: "
        f3 = "Opção escolhida: "
        frases = [f1, f2, f3]           #frases personalizadas

        option = Menu (alternatives, frases)        #cria o Menu
        option.print_choice()
        return (option.choice)

    else:   #demais execuções

        alternatives =[ ["Encerrar o programa"],
                        ["Escolher metodo para ordenação"],
                        ["Escolher metodo de busca"],
                        ["Imprimir a lista"],
                        ["Escolher outra lista"]    ]

        #Novo menu
        f1 = "\nOpções disponíveis: "
        f2 = "\nOpção desejada: "
        f3 = "Opção escolhida: "
        frases = [f1, f2, f3]           #frases personalizadas

        option = Menu (alternatives, frases)
        option.print_choice()
        return (option.choice)
