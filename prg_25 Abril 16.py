# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 19:04:37 2021

@author: Yamile

"""
def f_valorFactura(): #Encabezado de la funcion

  # Definicion de funcion
  # Definicion de variables
  ve_nomArt = ""
  ve_canArt = 0
  ve_valUniArt = 0.0
  cons_porIva= 0.19
  vps_netPag = 0.0
  vps_ivaPag = 0.0
  vps_totPag = 0.0

  # Entradas de datos
  ve_nomArt = input("Articulo: ")
  ve_canArt = int(input("Cantidad: "))
  ve_valUniArt = float(input("Valor Unitario: "))

  # Procesos
  vps_netPag=ve_canArt * ve_valUniArt
  vps_ivaPag=vps_netPag*cons_porIva
  vps_totPag=vps_netPag+vps_totPag

  # Salidas
  print("Neto:", vps_netPag)
  print("Iva:" , vps_ivaPag)
  print("total:" , vps_totPag)
  
  # Llamado a la funcion
  
  f_valorFactura()
 