# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 19:30:12 2021

@author: yamile
"""

# Programa que lee  N numeros enteros y calcula su promedio sale con
# un numero menor a cero

# Declarar variables

num = 0 # Variable que almacena los numeros que digita el usuario
suma = 0 # Variable que almacena la suma de los numeros positivos
med = 0.0 # Variable que almacena la media
canEle = 0 # Variable que almacena la cantidad de numeros digitados

num = int(input("Número : ")) # Lectura del primer numero

while (num > 0): # Inicio del ciclo
    suma = suma + num
    num =int(input(" Número : ")) # Lectura de los otros numeros
    canEle = canEle + 1
    
# Termina el ciclo
if canEle != 0 :
    med = suma/canEle # Calcular la media
    print("la media es: ",med) # Imprimir la media
    
else:
    print("No hay número para calcular la media")
