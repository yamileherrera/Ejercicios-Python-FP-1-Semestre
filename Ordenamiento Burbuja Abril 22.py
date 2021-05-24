# Ordenamiento por burbuja Ascendente

def ordenamientoBurbujaAscendente(unaLista):
    for numPasada in range(len(unaLista)-1,0,-1):
        for i in range(numPasada):
            if unaLista[i]>unaLista[i+1]:
                temp = unaLista[i]
                unaLista[i] = unaLista[i+1]
                unaLista[i+1] = temp

unaLista = [54,26,93,17,77,31,44,55,20]
print("Lista Original",unaLista)

ordenamientoBurbujaAscendente(unaLista)
print("Lista Ordenada Ascendente:", unaLista)

# Ordenamiento por burbuja descendente

def ordenamientoBurbujaDescendente(unaLista):
    for numPasada in range(len(unaLista)-1,0,-1):
        for i in range(numPasada):
            if unaLista[i]<unaLista[i+1]:
                temp = unaLista[i]
                unaLista[i] = unaLista[i+1]
                unaLista[i+1] = temp

unaLista = [2,14,93,17,23,31,15,55,4]
print("Lista Original",unaLista)

ordenamientoBurbujaDescendente(unaLista)
print("Lista Ordenada Descendente:", unaLista)




