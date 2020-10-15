class menu:

    def __init__(self, lista = [], textos=[], caminho=None):
        self.alternatives = lista
        self.frases = textos
        self.path = caminho
        if ( len(self.alternatives) ):
            self.choice = self.SelectMenu()
        if (caminho is not None):
            self.path = self.path + self.alternatives[self.choice]
        else:
            print("\nNenhuma alternativa")


    def SelectMenu(self):

        print ( self.personal_text(0) )
        for index,choices in enumerate (self.alternatives):          #imprime indices 
            print ("%d) %s" %(index,choices) )
        choice = int ( input(self.personal_text(1)) )

        if ( (choice < len(self.alternatives) )  and (choice >= 0) ):
            return (choice)
        else:
            print("\n%d não é uma opção. Tente novamente:" %choice) #impede o usuario de escolher fora do intervalo
            return ( self.SelectMenu() )


    def PrintChoice(self):
        print ( self.personal_text(2), self.alternatives [self.choice] )


    def personal_text(self, i ):
        if ( len(self.frases) > i ):
            return (self.frases[i]) #saida personalizada
        elif (i==0):
            return ("\nEscolha: ")  #saida predefinida
        elif (i==1):
            return ("\nNumero: ")   #saida predefinida
