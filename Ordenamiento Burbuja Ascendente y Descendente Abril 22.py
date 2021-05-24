# Ordenamiento por burbuja Ascendente y Descendente

def ordenamientoBurbuja(unaLista,tipo):
    
    if(tipo=="Ascendente"):
        for numPasada in range(len(unaLista)-1,0,-1):
           for i in range(numPasada):
              if unaLista[i]>unaLista[i+1]:
                 temp = unaLista[i]
                 unaLista[i] = unaLista[i+1]
                 unaLista[i+1] = temp
                 
    if(tipo=="Descendente"):
        for numPasada in range(len(unaLista)-1,0,-1):
          for i in range(numPasada):
                  if unaLista[i]<unaLista[i+1]:
                    temp = unaLista[i]
                    unaLista[i] = unaLista[i+1]
                    unaLista[i+1] = temp             
                 
      
# Fin del desarrollo de la funcion 

unaLista = [2,14,93,17,23,31,15,55,4]
tipo="Descendente"
ordenamientoBurbuja(unaLista,tipo)
print("Lista Ordenada de acuerdo a su gusto:", unaLista)
    
