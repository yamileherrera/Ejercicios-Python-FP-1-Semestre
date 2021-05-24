# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 19:19:23 2021

@author: yamile

# Practica_1 con Arreglos-vectores

# Almacenar en un vector las 5 notas del parcial

#Declarar el vector Lista 
listaNotas=[]
sumaNotas=0.0

# Asignar valores a la lista con ciclo
for posLista in range(5):
    #Leer desde teclado la nota
    notaEst=float(input("Digite nota:"))
    sumaNotas=sumaNotas+notaEst
    #Almacenamos la escaalar en el arreglo
    listaNotas.append(notaEst)
    
# Imprimir el arreglo
print(listaNotas)   
print("La suma de las notas es:",sumaNotas)

#==========================================

