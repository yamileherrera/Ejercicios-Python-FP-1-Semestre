# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 21:44:51 2021

@author: 82202114537 (Andres Giron), 82202115298 (Yamile Herrera), 82202115335 (Jacobo Buitrago)
"""

GeneroM = 0
GeneroF = 0 
Seccion1 = 0
Seccion2= 0
Seccion3= 0
 
Empleados = int(input("Digite el numero de empleados ")) 
 
 
def trabajo(Salario,Seccion,Genero):
    global Seccion1
    global Seccion2
    global Seccion3
    global GeneroM
    global GeneroF
    if Seccion == 1:
        Seccion1 = Seccion1 + Salario
    if Seccion == 2:
        Seccion2 = Seccion2 + Salario 
    if Seccion == 3:
        Seccion3 = Seccion3+ Salario 
    if Genero == 'M':
        GeneroM= GeneroM + Salario 
    if Genero == 'F':
        GeneroF= GeneroF + Salario 
 
for i in range(Empleados):
    VH = int(input("Valor por hora "))
    H = int(input("Horas de trabajo "))
    if H <= 35:
       Nombre = str(input("Digite su nombre "))
       Genero = str(input("Digite su sexo, M sea masculino o f femenino "))
       Seccion = int(input("Digite la seccion a la que pertenece 1,2 o 3"))
       SalarioNeto = VH * H
       Salud = ((SalarioNeto * 12.5)/100) 
       ICBF = ((SalarioNeto*4)/100)
       if(SalarioNeto > 2000000 and SalarioNeto <= 3000000):
            SalarioTarifa=((SalarioNeto * 5)/100)
            SalarioTotal = SalarioNeto - SalarioTarifa - Salud - ICBF
            print(f'El empleado {Nombre} de la sección {Seccion} gano un salario de {SalarioTotal} ')
            trabajo(SalarioTotal, Seccion, Genero)
 
       if(SalarioNeto > 3000001 and SalarioNeto <= 4000000):
            SalarioTarifa=((SalarioNeto * 7)/100)
            SalarioTotal = SalarioNeto - SalarioTarifa - Salud - ICBF
            print(f'El empleado {Nombre} de la sección {Seccion} gano un salario de {SalarioTotal} ')
            trabajo(SalarioTotal, Seccion, Genero) 
 
       if(SalarioNeto > 4000001 and SalarioNeto <= 5000000):
            SalarioTarifa=((SalarioNeto * 9)/100)
            SalarioTotal = SalarioNeto - SalarioTarifa - Salud - ICBF
            print(f'El empleado {Nombre} de la sección {Seccion} gano un salario de {SalarioTotal} ')
            trabajo(SalarioTotal, Seccion, Genero)
 
       if(SalarioNeto > 5000000 ):
            SalarioTarifa=((SalarioNeto * 11)/100)
            SalarioTotal = SalarioNeto - SalarioTarifa - Salud - ICBF
            print(f'El empleado {Nombre} de la sección {Seccion} gano un salario de {SalarioTotal} ')
            trabajo(SalarioTotal, Seccion, Genero)
 
       if(SalarioNeto <= 2000000):
            SalarioTotal = SalarioNeto - Salud - ICBF
            print(f'El empleado {Nombre} de la sección {Seccion} gano un salario de {SalarioTotal} ')
            trabajo(SalarioTotal, Seccion, Genero)
 
    if H > 35:
        Nombre = str(input("Digite nombre "))
        Genero = str(input("Digite su sexo, M sea masculino o f femenino "))
        Seccion = int(input("Digite la seccion a la que pertenece 1,2 o 3"))
        Hextras = H - 35
        SalarioNeto = VH * H
        SalarioExtra = ((VH*35)+(Hextras*(VH * 1.5))) 
        Salud = ((SalarioExtra * 12.5)/100) 
        ICBF = ((SalarioExtra*4)/100)      
 
        if(SalarioExtra > 2000000 and SalarioExtra <= 3000000):
            SalarioTarifa=((SalarioExtra * 5)/100)
            SalarioTotal = SalarioExtra - SalarioTarifa - Salud - ICBF
            print(f'El empleado {Nombre} de la sección {Seccion} gano un salario de {SalarioTotal}')
            trabajo(SalarioTotal, Seccion, Genero)
 
        if(SalarioExtra > 3000001 and SalarioExtra <= 4000000):
            SalarioTarifa=((SalarioExtra * 7)/100)
            SalarioTotal = SalarioExtra - SalarioTarifa - Salud - ICBF
            print(f'El empleado {Nombre} de la sección {Seccion} gano un salario de {SalarioTotal}')
            trabajo(SalarioTotal, Seccion, Genero)  
 
        if(SalarioExtra > 4000001 and SalarioExtra <= 5000000):
            SalarioTarifa=((SalarioExtra * 9)/100)
            SalarioTotal = SalarioExtra - SalarioTarifa - Salud - ICBF
            print(f'El empleado {Nombre} de la sección {Seccion} gano un salario de {SalarioTotal}')
            trabajo(SalarioTotal, Seccion, Genero)
 
        if(SalarioExtra > 5000000 ):
            SalarioTarifa=((SalarioExtra * 11)/100)
            SalarioTotal = SalarioExtra - SalarioTarifa - Salud - ICBF
            print(f'El empleado {Nombre} de la sección {Seccion} gano un salario de {SalarioTotal}')
            trabajo(SalarioTotal, Seccion, Genero) 
 
        if(SalarioNeto <= 2000000):        
            SalarioTotal = SalarioNeto - Salud - ICBF
            print(f'El empleado {Nombre} de la sección {Seccion} gano un salario de {SalarioTotal}')
            trabajo(SalarioTotal, Seccion, Genero)
 
 
print('La seccion 1 gano un total' ,Seccion1)
print('La seccion 2 gano un total' ,Seccion2)
print('La seccion 3 gano un total' ,Seccion3)
print('los generos masculinos ganaron' ,GeneroM)
print('los generos femeninos ganaron' ,GeneroF)    