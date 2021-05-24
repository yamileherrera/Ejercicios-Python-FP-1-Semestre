# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 19:00:21 2021

@author: Yamile Herrera

Programa que lee el nombre y la nota definitiva de 3
materias (basic, fortran y pascal) d N estudiantes.
Condicion de salida nombre = ***
"""
# Variables de declaracion de variables

var_e_nom = "***"
var_e_bas = 0.0
var_e_for = 0.0
var_e_pas = 0.0

var_p_s_conEst = 0

var_p_s_mediEst = 0.0

# Leer nombre
var_e_nom = input("Digiye nombre del estudiante : ")

# Ciclo while
while(var_e_nom != "***"): 
    # Inicio del ciclo
    var_e_bas = float(input("definitiva Basic :"))
    var_e_for = float(input("definitiva Fortran:"))
    var_e_pas = float(input("definitiva Pascal :"))

# Proceso que calcula la media del estudiante
    var_p_s_mediEst = (var_e_bas+var_e_for+var_e_pas)/3
    print("La media de : " ,var_e_nom,"es ",var_p_s_mediEst)
    var_e_nom = input("Digiye nombre del estudiante : ")
    var_p_s_conEst = var_p_s_mediEst+1
# Fin del ciclo
print("Total de Estudiantes :",var_p_s_conEst)
print("ADIOS...")

