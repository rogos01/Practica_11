#estrategia divide y venceras
"""
21 10 12 0 34 15
p   i          d

15 10 12 0 34 21
p   i       d

15 10 12 0 34 21
p      i d

0 10 12 15 34 21
p

0 10 12             15 34 21
p  i  d             p   i  d

"""   
def quicksort(lista):
    quicksort2(lista, 0, len(lista)-1)


def quicksort2(lista, inicio, fin):
    if inicio <fin:
        pivote = particion(lista, inicio, fin)
        quicksort2(lista, inicio, pivote-1)
        quicksort2(lista, pivote+1, fin)

def particion(lista, inicio, fin):
    pivote = lista[inicio]
    print("valor de pivote {}".format(pivote))
    izquierda = inicio+1
    derecha = fin
    print("indice izquierdo {} e indice derecho {}".format(izquierda, derecha))
    bandera = False
    while not bandera:
        while izquierda <= derecha and lista[izquierda] <= pivote:
            izquierda = izquierda + 1
        while derecha >= izquierda and lista[derecha] >= pivote:
            derecha = derecha-1
        if derecha < izquierda:
            bandera = True
        else:
            temp = lista[izquierda]
            lista[izquierda] = lista[derecha]
            lista[derecha] = temp

    print(lista)
    temp = lista[inicio]
    lista[inicio] = lista[derecha]
    lista[derecha] = temp 
    return derecha

lista=[21, 10, 12, 0, 34, 15]
print(lista)
quicksort(lista)
print(lista)