# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 18:47:22 2021

@author: Yamileherrera
"""

# Programa que calcula la nota de un estudiante

# Entradas
# pedir el nombre del estudiante y sus 3 notas parciales


canEst=int(input("Cantidad de Estudiantes : "))
# Inicializar la variable que controla el ciclo
conRep=0
# Variable real para sumar las definitivas del grupo
sumDefGru=0.0
# Variable para calcular la nota promedio del grupo
notProDefGru=0.0

while(conRep < canEst) :
     # instruciones a repetir
     nomEst=input("Nombre Estudiante : ")
     notUnoEst= float(input("parcial uno: "))
     notDosEst= float(input("parcial dos: "))
     notTresEst= float(input("parcial tres: "))

     # Calculos
     notDefEst = (notUnoEst+notDosEst+notTresEst)/3
    
     # Acumulo las definitivas del grupo
     sumDefGru=sumDefGru+notDefEst
 
     # Imprimir los resultados - salidas
     print(f"1. la nota definitiva es :{notDefEst:2f}")
  
     #Incrementar la variable que controla el ciclo
     conRep = conRep+1
     
# calcular el promedio del grupo
notProDefGru = sumDefGru/canEst
    
#imprimir la nota promedio del grupo 
print(f"2. la nota promedio del grupo es : {notProDefGru:.2f}")


