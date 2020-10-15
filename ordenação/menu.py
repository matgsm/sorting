class menu:

    def __init__(self, lista = [], textos=[], caminho=[]):
        self.alternatives = lista
        self.frases = textos
        if ( len(self.alternatives) ):
            self.choice = caminho + self.alternatives[ self.SelectMenu() ]
        else:
            print("\nNenhuma alternativa")

    def SelectMenu(self):     #imprime metodos de ordenação para o usuario e retorna o indice do metodo escolhido

        print ( self.personal_text(0) )
        for index,sort in enumerate (self.alternatives):          #imprime indices associados a metodos de ordenação (ex: "2) mergesort" )
            print ("%d) %s" %(index,sort) )
        choice = int ( input(self.personal_text(1)) )

        if ( (choice < len(self.alternatives) )  and (choice >= 0) ):
            #Print_Method(choice)
            return (choice)
        else:
            print("\n%d não é uma opção. Tente novamente:" %choice) #impede o usuario de escolher fora do intervalo
            return ( self.SelectMenu() )

    def PrintChoice(self):
        print ( self.personal_text(2), self.choice )

    def personal_text(self, i ):
        if ( len(self.frases) > i ):
            return (self.frases[i])
        elif (i==0):
            return ("\nEscolha: ")
        elif (i==1):
            return ("\nNumero: ")
