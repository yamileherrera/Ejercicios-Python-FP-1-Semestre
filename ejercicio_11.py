# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 20:25:04 2021

@author: Yamile
"""
# Entradas

num1=int(input("Ingrese primer valor:"))
num2=int(input("Ingrese segundo valor:"))

if num1>num2:   
    suma=num1+num2
    diferencia=num1-num2
    print("La suma de los valores es:")
    print(suma)
    print("La resta de los valore es:")
    print(diferencia)
    
else:
    producto=num1*num2
    division=num1/num2
    print("El producto de los valores es:")
    print(producto)
    print("La division de los valores es:")
    print(division)