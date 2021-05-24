# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 18:38:21 2021

@author: Yamile
"""

# Programa que calcula el cuadro de los primeros 100 numeros

# Area declaracion de variables

cuadradoNumero = 0
acumuladorSuma = 0
num = 1

# Entradas
cantidadNumeros = int (input("cantidad de numeros: "))
# Procesos

for num in range(1,cantidadNumeros+1,1):
    cuadradoNumero=num*num
    acumuladorSuma=acumuladorSuma+cuadradoNumero
    print("El cuadrado de : ", num, " es : " ,cuadradoNumero)
    print("La suma acumulada es : ", acumuladorSuma)
    
# Fin del ciclo

print("la suma de los cuadrados es : ", acumuladorSuma)