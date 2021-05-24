# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 20:45:13 2021

@author: Yamile Herrera_Jacobo Buitrago_Andres Giron
"""
# Punto 4
# Opcion 1 serie Fibonacci
def fib(n1): # funcion definida Fibonacci

    a = 0 # variable a y b
    b = 1
    while a < n1: # contador de repeticiones while
        print(a, end=' ')
        a, b = b, a+b
    print()
fib(610)

# Opcion 2 valor a encontrar en la secuencia 

n2=int(input("Ingrese el valor que quiere encontrar: "))
def fib(n2):
    a = 0
    b = 1
    
    for k in range(n2):
        c = b+a
        a = b
        b = c
        
    return a
fib(n2)
print(fib(n2))

# Opcion 3 leer un rango y  sumarlo 
def fib(n):
    a = 0
    b = 1
    
    for k in range(n-1):
        c = a+b
        a = b
        b = c
        
    return b

for x in range(0):
    print(fib(x))
       
print(fib(3),fib(4),fib(5),fib(6))
print(fib(3)+fib(4)+fib(5)+fib(6))





