class Monitor:
    #atributes
    time = None
    sec_time = None
    comp = None     #comparisons
    movim = None    #movimentations
    ind = None      #indice
    text = None

    #constructor
    def __init__(self, comparisons=0, movimentations=0, indice=None):
        self.comp = comparisons
        self.movim  = movimentations
        self.ind = indice

    #methods
    def status (self):
        if (self.text is None):
            self.text = "processar"
        print("\nTempo para %s: " %(self.text) ,self.time)
        print("\nComparações: ",self.comp)
        if (self.movim is not None):
            print("Movimentações: ", self.movim)
        self.time_best()

    def time_best(self):
        if (self.sec_time is not None):
            print("Tempo para escolher melhor metodo: ",self.sec_time)
