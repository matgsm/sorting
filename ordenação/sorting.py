comp = 0    #quantidade de comparações
movim = 0   #quantidade de movimentações entre registros

#****************************************#

def insertion_sort(lista):
    global comp, movim
    n = len(lista)
    for i in range(1, n):       #for
        chave = lista[i]
        j = i - 1
        while j >= 0 and lista[j][0] > chave[0]:   #compara apenas first_name
            lista[j+1] = lista[j]
            movim = movim +1                    #movim
            j = j - 1
            comp = comp + 1
        comp = comp + 1
        lista[j+1] = chave
    
    CompMov = [ [comp],[movim] ]
    return (CompMov)

# Complexidade de tempo O(nˆ2)
# Complexidade de espaço O(n)

#****************************************#

def selection_sort(lista):
    global comp, movim
    n = len(lista)
    for j in range(n-1):
        min_index = j
        for i in range(j, n):
            if lista[i][0] < lista[min_index][0]:                       #compara apenas first_name
                min_index = i
            comp = comp + 1
        if lista[j][0] > lista[min_index][0]:                           #compara apenas first_name
            lista[j], lista[min_index] = lista[min_index], lista[j]
            movim = movim + 1                                           #movim
        comp = comp + 1
    CompMov = [ [comp],[movim] ]
    return (CompMov)

# 1 + (n-1)*[5 + X] = 1 + 5*(n-1) + X*(n-1)
# Complexidade de tempo O(nˆ2)
# Complexidade de espaço O(n)

#****************************************#

def mergesort(lista, inicio=0, fim=None):
    global comp, movim
    if fim is None:
        fim = len(lista)
    if(fim - inicio > 1):
        meio = (fim + inicio) // 2    # '//' retorna a parte inteira da divisao
        mergesort(lista, inicio, meio)
        mergesort(lista, meio, fim)
        merge(lista, inicio, meio, fim)
    
    CompMov = [ [comp],[movim] ]
    return (CompMov)

def merge(lista, inicio, meio, fim):
    global comp, movim
    left = lista[inicio:meio]
    right = lista[meio:fim]
    top_left, top_right = 0, 0
    for k in range(inicio, fim):
        if top_left >= len(left):
            lista[k] = right[top_right]
            movim = movim + 1                           #movim
            top_right = top_right + 1
        elif top_right >= len(right):
            lista[k] = left[top_left]
            movim = movim + 1                           #movim
            top_left = top_left + 1
        elif left[top_left][0] < right[top_right][0]:   #compara apenas first_name
            lista[k] = left[top_left]
            movim = movim + 1                           #movim
            top_left = top_left + 1
            comp = comp + 1
        else:
            lista[k] = right[top_right]
            movim = movim + 1                           #movim
            top_right = top_right + 1
            comp = comp + 1

#****************************************#

def quicksort(lista, inicio=0, fim=None):
    global comp, movim
    if fim is None:
        fim = len(lista)
    if inicio < fim:
        p = partition(lista, inicio, fim)
        # recursivamente na sublista à esquerda (menores)
        quicksort(lista, inicio, p)
        # recursivamente na sublista à direita (maiores)
        quicksort(lista, p+1, fim)

    CompMov = [ [comp],[movim] ]
    return (CompMov)
    
def partition(lista, inicio, fim):
    global comp,movim
    pivot = lista[inicio][0]            #armazena para comparação apenas first_name
    i = inicio + 1                      #i:na esquerda de i tem elementos menores que o pivo     
    for j in range( (inicio+1), fim ):  #j:entre i e j tem  maiores que o pivo
                                        # j sempre avança, pois representa o elementa em análise
                                        # j delimita os elementos maiores que o pivô
        
        if lista[j][0] <= pivot:        #compara apenas first_name       
            lista[j], lista[i] = lista[i], lista[j]
            movim = movim + 1           #movim
            i = i + 1                   # incrementa-se o limite dos elementos menores que o pivô 
        comp = comp+1   #comp
    
    if (i > (inicio + 1) ):             #Verifica se i foi incrementado, evita movimentações desnecessarias
        lista[i-1], lista[inicio] = lista[inicio], lista[i-1]   
        movim = movim + 1                   #movimentação do pivô

#    lista[i-1], lista[inicio] = lista[inicio], lista[i-1]   
#    movim = movim + 1                   #movimentação do pivô

    return (i-1)

#****************************************#
