# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 19:19:23 2021

@author: yamile
"""

n=1
cuadrado=0
suma=0

while n<100:
    cuadrado=n**2
    suma=suma+cuadrado
    print ("n es:",n)
    print ("cuadrado es:",cuadrado)
    print ("suma es acumulada de los cuadrados de los números es:",suma)
    print()
    n=n+1