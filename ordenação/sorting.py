from monitor import Monitor
import timeit

#****************************************#

def insertion_sort(lista):
    n = len(lista)
    comp = movim = 0

    for i in range(1, n):       #for
        chave = lista[i]
        j = i - 1

        while j >= 0 and lista[j][0] > chave[0]:   #compara apenas first_name
            comp += 1
            lista[j+1] = lista[j]
            movim += 1                    #movim
            j -= 1

        comp += 1         #1 comparação é feita quando nao entra no laço
        lista[j+1] = chave

    relatorio = Monitor (comp, movim)
    return (relatorio)

# Complexidade de tempo O(nˆ2)
# Complexidade de espaço O(n)

#****************************************#

def selection_sort(lista):
    n = len(lista)
    comp = movim = 0

    for j in range(n-1):
        min_index = j

        for i in range(j, n):
            if lista[i][0] < lista[min_index][0]:                       #compara apenas first_name
                min_index = i
            comp += 1

        if lista[j][0] > lista[min_index][0]:                           #compara apenas first_name
            lista[j], lista[min_index] = lista[min_index], lista[j]
            movim += 1                                           #movim
        comp += 1
    relatorio = Monitor (comp, movim)
    return (relatorio)

# 1 + (n-1)*[5 + X] = 1 + 5*(n-1) + X*(n-1)
# Complexidade de tempo O(nˆ2)
# Complexidade de espaço O(n)

#****************************************#

def merge_sort(lista, inicio=0, fim=None, relatorio=None):
    if fim is None:
        fim = len(lista)
        relatorio = Monitor()
        R1 = None
    if(fim - inicio > 1):
        meio = (fim + inicio) // 2    # '//' retorna a parte inteira da divisao
        relatorio = merge_sort(lista, inicio, meio, relatorio)
        relatorio = merge_sort(lista, meio, fim, relatorio)
        relatorio = merge(lista, inicio, meio, fim, relatorio)

#        relatorio.comp += R1.comp + R2.comp + R3.comp
#        relatorio.movim = R1.movim + R2.movim + R3.movim
    return (relatorio)

def merge(lista, inicio, meio, fim, relatorio):
    left = lista[inicio:meio]
    right = lista[meio:fim]
    top_left, top_right = 0, 0
    for k in range(inicio, fim):
        if top_left >= len(left):
            lista[k] = right[top_right]
            relatorio.movim += 1                           #movim
            top_right = top_right + 1
        elif top_right >= len(right):
            lista[k] = left[top_left]
            relatorio.movim += 1                           #movim
            top_left = top_left + 1
        elif left[top_left][0] < right[top_right][0]:   #compara apenas first_name
            lista[k] = left[top_left]
            relatorio.movim += 1                             #movim
            top_left = top_left + 1
            relatorio.comp += 1
        else:
            lista[k] = right[top_right]
            relatorio.movim += 1                            #movim
            top_right = top_right + 1
            relatorio.comp += 1

    return (relatorio)

#****************************************#

def quick_sort(lista, inicio=0, fim=None, relatorio=None):
    if fim is None:
        fim = len(lista)
        relatorio = Monitor()

    if inicio < fim:
        relatorio = partition(lista, inicio, fim, relatorio)
        i = relatorio.ind   #indice
        # recursivamente na sublista à esquerda (menores)
        relatorio = quick_sort(lista, inicio, i, relatorio)
        # recursivamente na sublista à direita (maiores)
        relatorio = quick_sort(lista, i+1, fim, relatorio)

    return (relatorio)  #relatorio

def partition(lista, inicio, fim, relatorio):
    pivot = lista[inicio][0]            #armazena para comparação apenas first_name
    i = inicio + 1                      #i:na esquerda de i tem elementos menores que o pivo
    for j in range( (inicio+1), fim ):  #j:entre i e j tem  maiores que o pivo
                                        # j sempre avança, pois representa o elementa em análise
                                        # j delimita os elementos maiores que o pivô

        if lista[j][0] <= pivot:        #compara apenas first_name
            lista[j], lista[i] = lista[i], lista[j]
            relatorio.movim += 1           #movim
            i = i + 1                   # incrementa-se o limite dos elementos menores que o pivô
        relatorio.comp += 1   #comp

    if (i > (inicio + 1) ):             #Verifica se i foi incrementado, evita movimentações desnecessarias
        lista[i-1], lista[inicio] = lista[inicio], lista[i-1]
        relatorio.movim += 1                 #movimentação do pivô

    relatorio.ind = (i-1)
    return (relatorio)

#****************************************#

def bubble_sort(lista):
    n = len(lista)
    for j in range(n-1):
        for i in range(n-1):
            if lista[i] > lista[i+1]:
                # troca de elementos nas posições i e i+1
                lista[i], lista[i+1] = lista[i+1], lista[i]
                movim = movim + 1
            comp = comp + 1
    relatorio = Monitor (comp, movim)
    return (relatorio)
# Complexidade de tempo O(nˆ2)
# Complexidade de espaço O(n)
