comp = 0    #quantidade de comparações
movim = 0   #quantidade de movimentações entre registros

#****************************************#

def insertion_sort(lista):
    global comp, movim
    n = len(lista)
    for i in range(1, n):       #for
        comp = comp + 1         #comp do laço for
        chave = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > chave:      #while
            comp = comp + 2                     # 2 comparações no laço while
            lista[j+1] = lista[j]
            movim = movim +1                    #movimentação
            j = j - 1
        lista[j+1] = chave
        movim = movim + 1                       #movimentação
    
    CompMov = [ [comp],[movim] ]
    return (CompMov)

# Complexidade de tempo O(nˆ2)
# Complexidade de espaço O(n)

#****************************************#

def selection_sort(lista):
    global comp, movim
    n = len(lista)
    for j in range(n-1):        #for-1
        comp = comp + 1         #comp do laço for-1
        min_index = j
        for i in range(j, n):   #for-2
            comp = comp + 1     #comp do laço for-2
            if lista[i] < lista[min_index]:     #if-1
                comp = comp + 1                 #comp da condição if-1
                min_index = i
        if lista[j] > lista[min_index]:         #if-2
            comp = comp + 1                     #comp da condição if-2
            lista[j], lista[min_index] = lista[min_index], lista[j]
            movim = movim +1                    #movimentação

    CompMov = [ [comp],[movim] ]
    return (CompMov)

# 1 + (n-1)*[5 + X] = 1 + 5*(n-1) + X*(n-1)
# Complexidade de tempo O(nˆ2)
# Complexidade de espaço O(n)

#****************************************#

def mergesort(lista, inicio=0, fim=None):
    global comp, movim
    if fim is None:         #if-1
        fim = len(lista)
    comp = comp + 1         #comp condição if-1
    if(fim - inicio > 1):   #if-2
        meio = (fim + inicio) // 2    # '//' retorna a parte inteira da divisao
        mergesort(lista, inicio, meio)
        mergesort(lista, meio, fim)
        merge(lista, inicio, meio, fim)
    comp = comp + 1         #comp condição if-2
    
    CompMov = [ [comp],[movim] ]
    return (CompMov)

def merge(lista, inicio, meio, fim):
    global comp, movim
    left = lista[inicio:meio]
    right = lista[meio:fim]
    top_left, top_right = 0, 0
    for k in range(inicio, fim):                    #for
        comp = comp + 1                             #comp laço for
        if top_left >= len(left):                   #if-3
            lista[k] = right[top_right]
            movim = movim + 1                       #movim
            top_right = top_right + 1
            comp = comp + 1                         #comp condição if-3
        elif top_right >= len(right):               #elif-4
            lista[k] = left[top_left]
            movim = movim + 1                       #movim
            top_left = top_left + 1
            comp = comp + 2                         #(if-3) + (elif-4) = 2 comparações
        elif left[top_left] < right[top_right]:     #(elif-5)
            lista[k] = left[top_left]
            movim = movim + 1                       #movim
            top_left = top_left + 1
            comp = comp + 3                         #(if-3) + (elif-4) + (elif-5) = 3 comparações
        else:                                       #else-6
            lista[k] = right[top_right]
            movim = movim + 1                       #movim
            top_right = top_right + 1
            comp = comp + 3                         #(if-3) + (elif-4) + (elif-5) = 3 comparações
                                                    #obs: else nao conta como comparação. Se comparações sao falsas, executa else


#****************************************#

def quicksort(lista, inicio=0, fim=None):
    global comp, movim
    if fim is None:     #if-1
        fim = len(lista)
    comp = comp+1       #comp condição if-1
    if inicio < fim:    #if-2
        p = partition(lista, inicio, fim)
        # recursivamente na sublista à esquerda (menores)
        quicksort(lista, inicio, p)
        # recursivamente na sublista à direita (maiores)
        quicksort(lista, p+1, fim)
    comp = comp+1       #comp condição if-2

    CompMov = [ [comp],[movim] ]
    return (CompMov)
    
def partition(lista, inicio, fim):
    global comp,movim
    pivot = lista[inicio]
    i = inicio + 1      #i:na esquerda tem menores que pivo; j:entre i e j tem  maiores que o pivo(direita do pivo)
    for j in range( (inicio+1), fim ):  #for-1
        comp = comp+1                   #comp laço for-1
        # j sempre avança, pois representa o elementa em análise
        # e delimita os elementos maiores que o pivô
        if lista[j] <= pivot:           #if-3
            lista[j], lista[i] = lista[i], lista[j]
            movim = movim + 1           #movimentação de registros
            # incrementa-se o limite dos elementos menores que o pivô
            i = i + 1
        comp = comp+1   #comp condição if-3
    lista[i-1], lista[inicio] = lista[inicio], lista[i-1]   
    movim = movim + 1                   #movimentação do pivô

    return (i-1)

#****************************************#
