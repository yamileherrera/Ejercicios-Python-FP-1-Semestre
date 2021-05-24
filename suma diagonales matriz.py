matrizNumeros=[[7,8,3],[1,9,2],[4,6,5]]

print(matrizNumeros)

# Suma de todos los elementos de la matriz
sumEleMat=0
for f in range(3):
    for c in range(3):
        sumEleMat=sumEleMat+matrizNumeros[f][c]
print("la suma de los elementos es: ",sumEleMat)        

# Imprimir la matriz
for f in range(3):
    for c in range(3):
        print("Dato:",matrizNumeros[f][c])
        
        
# sumar la diagonal principal 
sumDiaPri=0
for pos in range(3):
    sumDiaPri=sumDiaPri+matrizNumeros[pos][pos]
    print("Diagonal:",sumDiaPri)
    
    sumDiaPri1=0
for fil in range(3):
    for col in range(3):
        if(fil==col):
            sumDiaPri1=sumDiaPri1+matrizNumeros[fil][col]
    print("Diagonal:",sumDiaPri1)
    
