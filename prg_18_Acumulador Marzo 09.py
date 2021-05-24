# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 18:42:55 2021

@author: yamile
"""
# Librerias usadas en el programa
import random

# Leer N, general aleatorios y calcular suma y promedio

# Area de definicion de variables 

cantidadNumeros = 0
contadorRepeticionesWhile = 0
numero = 0
acumuladorSuma = 0
promedioNumeroAleatorios = 0.0

# Segunda parte del ejercicio

acumuladorPositivos = 0
acumuladorNegativos = 0
contadorPositivos = 0
contadorNegativos= 0
promedioPositivos = 0.0
promedioNegativos = 0.0

# Tercera parte del ejercicio

mayorPositivo = 0
mayorNegativo = 0
menorPositivo = 1000
menorNegativo = -1000

# Entradas

cantidadNumeros =int (input("Cantidad de numeros :"))

# Procesos
# Ciclo While

while contadorRepeticionesWhile<cantidadNumeros:
    numero = random.randint(-10000, 10000)
    acumuladorSuma=acumuladorSuma+numero
    
    # Segunda parte del ejercicio
    if numero>0: # calculo de numero positivos
        print(" Número Positivo:" , numero)
        acumuladorPositivos=acumuladorPositivos+numero
        contadorPositivos=contadorPositivos+1
        
        # Tercera parte del ejercicio
        # Identificar el mayor de los positivos
        if numero>mayorPositivo:
            mayorPositivo=numero
            
        # Identificar el menor de los positivos
        if numero<menorPositivo:
            menorPositivo=numero 
        # Fin tercera parte del ejercico
        
    else:# calculo para numeros negativos
     print("Número negativo: ", numero)
     acumuladorNegativos=acumuladorNegativos+numero
     acumuladorNegativos=acumuladorNegativos+1
     contadorRepeticionesWhile=contadorRepeticionesWhile+1
     
     # Identificar el mayor de los negativos
    
     if numero>mayorNegativo:
            mayorNegativo=numero
            
     # Identificar el menor de los negativos
     if numero<menorNegativo:
            menorNegativo=numero
            
        # Fin tercera parte del ejercico
        # fin de la segunda parte del ejercicio
        
    contadorRepeticionesWhile=contadorRepeticionesWhile+1
# Fin del ciclo
# Calculo de promedios

promedioNumeroAleatorios = acumuladorSuma/contadorRepeticionesWhile
promedioPositivos=acumuladorPositivos/contadorPositivos
promedioNegativos=acumuladorNegativos/contadorNegativos

# Salidas de todos los numeros 
print("Suma de numeros aleatorios", acumuladorSuma)
print("promedio de numeros aleatorios", promedioNumeroAleatorios)

# Salida de todos los numeros positivos
print("cantidad numeros positivos:", contadorPositivos)
print("suma de numeros positivos:", acumuladorPositivos)
print("promedio de los numeros positivos:", promedioPositivos)

# Salida de todos los numeros negativos
print("cantidad numeros negativos:", contadorNegativos)
print("suma de numeros negativos:", acumuladorNegativos)
print("promedio de los numeros negativos:", promedioNegativos)

# Salida mayor de los positivos y menor de los positivos
print("Mayor de los positivos:",mayorPositivo)
print("Menor de los positivos: ",menorPositivo)

# Salida mayor de los negativos y menor de los negativos
print("Mayor de los negativos:",mayorNegativo)
print("Menor de los negativos: ",menorNegativo)
