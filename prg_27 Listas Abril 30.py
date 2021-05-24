# -*- coding: utf-8 -*-
"""
Created on Tue Apr 20 18:49:02 2021

@author: Yamile
"""

# Definicion un vector e inicializarlos
varEscNum=10
print (varEscNum)
varEscNum=20
print(varEscNum)

# Variables vectorial - N datos del mismo tipo de datos
# Aplicacion de estructura de datos
print("ARREGLO VECTORIAL")
varvectorNum=[10,20,30,12,35,10]
print(varvectorNum)

# Funciones de una lista

#Adicionar al final de la lista 
varvectorNum.append(2000)
print(varvectorNum)
 
#Adicionar datos por teclado a una lista 
varvectorNumTecUno=[]
# Adicionar datos por teclado a la lista 
for pos in range(3):
    datoTeclado=int(input("Digite valor:"))
    varvectorNumTecUno.append(datoTeclado)
    
print(varvectorNumTecUno)   
varvectorNumTecUno.append(3000)
print(varvectorNumTecUno)
    
# Borrar los elementos de la lista
#varvectorNumTecUno.clear()

# Crear una lista con su datos
varvectorNumTecDos=[2,4,6,8,10]
print(varvectorNumTecUno)
print(varvectorNumTecDos)

# Unir dos lista 
varvectorNumTecUno.extend(varvectorNumTecDos)
print(varvectorNumTecUno)

#conocer el tamaño  de la lista 

tamVect=len(varvectorNumTecUno)
print(tamVect)

#contar las repeticiones de un dato
print(varvectorNumTecUno.count(12))