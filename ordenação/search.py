from monitor import Monitor

def linear_search (list, item):
    end = len(list)
    comp = 0
    relatorio = Monitor()
    for i in range (0 , end ):
        comp +=1
        if (list[i][0].lower() == item.lower() ):
            relatorio.comp = comp
            relatorio.ind = i
            return (relatorio)

    relatorio.comp = comp
    return (relatorio)   #Não esta na lista

#************************************************************************#

def binary_search (list, item, begin=0, end=None, relatorio=None):
    if (end is None):
        end = len(list)-1
        relatorio = Monitor()
        relatorio.ind = None

    if (begin <= end):
        m = (begin + end)//2

        relatorio.comp +=1
        if ( list[m][0].lower() == item.lower() ):
            relatorio.ind = m
            return (relatorio)

        relatorio.comp +=1
        if (item.lower() < list[m][0].lower() ):
            return (binary_search(list, item, begin, m-1, relatorio) )
        else:
            return (binary_search(list, item, m+1, end, relatorio) )
    return (relatorio)
