matrix_aux = ([4,6,2,9],[5,8,6,1],[7,2,5,10],[27,12,25,15])
            
print(matrix_aux[2][1])

print(matrix_aux[1][0])

print(matrix_aux)

# Calcular la suma de los elementos de la matrix
sumEleMat=0
for c in range(4):
    for f in range (4):
        sumEleMat=sumEleMat+matrix_aux[c][f]
        print("la suma es : ",sumEleMat)
    print("la suma ciclo externo es:", sumEleMat)
    
import numpy as np 

n = 4
A = np.array ([[4,6,2,9],[5,8,6,1],[7,2,5,10],[27,12,25,15]])
print(A)

sum_first_diagonal = sum(A[i][i] for i in range(n))
sum_second_diagonal = sum(A[i][n-i-1] for i in range(n))
print(str(sum_first_diagonal))
print(str(sum_second_diagonal))
