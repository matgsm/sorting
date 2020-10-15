# Busca binária
def binary_search (list, item, begin=0, end=None):
    if (end is None):
        end = len(list)-1
    if (begin <= end):
        m = (begin + end)//2
        if ( list[m][0].lower() == item.lower() ):
            return (m)
        if (item.lower() < list[m][0].lower() ):
            return (binary_search(list, item, begin, m-1) )
        else:
            return (binary_search(list, item, m+1, end) )
    return (None)


def linear_search (list, item):
    end = len(list)
    for i in range (0 , end ):
        if (list[i][0].lower() == item.lower() ):
            return (i)

    return (None)   #Não esta na lista
