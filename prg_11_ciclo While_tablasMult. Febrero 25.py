# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 19:03:24 2021

@author: Yamileherrera
"""


# Programa que lee una tabla y la imprime desde el 1 hasta el 20 y suma los resultados

# Declarar variables:
tabla = 0    
multiplicador = 1
resultado = 0
sumaResultados = 0
conRepCiclo = 1

# Leer el numero de la tabla para la cual vamos a realizar las operaciones
tabla = int(input("tabla :"))
# Leer multiplicador
multiplicador = int(input("multiplicador : "))

# Inicio el ciclo repetitivo WHILE
while(conRepCiclo <= multiplicador):
    resultado = tabla * conRepCiclo
    sumaResultados = sumaResultados + resultado
    print(tabla, " * ", conRepCiclo, " = ",resultado)
    # Incrementar la variable que controla el ciclo
    conRepCiclo = conRepCiclo + 1
print("la suma de los resultados es : ", sumaResultados)
