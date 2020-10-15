class menu:
    #atributes
    alternatives = []
    frases = []
    path = ""
    choice = None

    #construtor
    def __init__(self, lista = [], textos=[], caminho=None):
        self.alternatives = lista
        self.frases = textos
        self.path = caminho

        if ( len(self.alternatives) > 0 ):
            self.choice = self.SelectMenu()
        else:
            print("\nNenhuma alternativa")

        if (caminho is not None):
            self.path = self.path + self.alternatives[self.choice]

    #Methods
    def SelectMenu(self):
        print ( self.personal_text(0) )
        for index,choices in enumerate (self.alternatives):
            print ("%d) %s" %(index,choices) )          #Enumera as alternativas

        choice = int ( input(self.personal_text(1)) )

        #valida a escolha antes de retornar
        if ( (choice < len(self.alternatives) )  and (choice >= 0) ):
            return (choice)
        else:
            print("\n%d não é uma opção. Tente novamente:" %choice) #impede o usuario de escolher fora do intervalo
            return ( self.SelectMenu() )


    def PrintChoice(self):
        print ( self.personal_text(2), self.alternatives [self.choice] )


    def Last(self):
        return ( len(self.alternatives) - 1 )


    def personal_text(self, i ):
        if ( len(self.frases) > i ):
            return (self.frases[i]) #saida personalizada
        elif (i==0):
            return ("\nEscolha: ")  #saida predefinida
        elif (i==1):
            return ("\nNumero: ")   #saida predefinida
