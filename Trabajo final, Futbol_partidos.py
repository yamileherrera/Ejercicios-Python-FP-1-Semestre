# -*- coding: utf-8 -*-
"""
Created on Sun May 23 08:14:47 2021

@author: DELL
"""
# Lectura de archivos tipo excel 
# Importar librerías
import matplotlib.pyplot as plt
import pandas as pd 

df_archivoExcel = pd.read_excel('Futbol_Partidos.xlsx')#,index_col="Producto")
#archivoExcel = pd.read_excel('Futbol_Partidos.xlsx')
n_goles_local= df_archivoExcel['goles_local']
n_goles_visita= df_archivoExcel['goles_visita']


#  Función desarrollada por el programador
# 1. Calcular Cantidad de goles de los equipos locales y graficar
def goles_local1():
    Tgoles_local = df_archivoExcel['goles_local'].sum()#  Función propia del lenguaje
    return Tgoles_local
# 2. Calcular Cantidad de goles de los equipos visitantes y graficar
def goles_visita2():
    Tgoles_visita = df_archivoExcel['goles_visita'].sum()#  Función propia del lenguaje
    return Tgoles_visita
# 3. Calcular Cantidad total de goles de todos los partidos y graficar
def tot_goles3():
    total_goles=df_archivoExcel['goles_local'].sum() + df_archivoExcel['goles_visita'].sum()
    return total_goles

def tot_goles_camp4():
    for i in df_archivoExcel.index:
        print("Total goles de local de "+ df_archivoExcel["local"][i]+ " en: "  +df_archivoExcel['torneo'][i]+ " es: "  +str(df_archivoExcel['goles_local'][i]) )


print("El total de goles de los locales es",(goles_local1()))
print("El total de goles de los visitantes es",(goles_visita2()))
print("El total de goles marcados en todos los partidos es ",(tot_goles3()))
print("El total de goles de los equipos locales por torneo es ", (tot_goles_camp4()))


fig, df = plt.subplots()
df.set_title("Goles local")
df.set_ylabel("Goles local")
df.set_xlabel(" # de Goles")
#crear el gráfico

plt.barh(df_archivoExcel['local'],df_archivoExcel['goles_local'] )
plt.show()

fig, df = plt.subplots()
df.set_title("Goles visitante")
df.set_ylabel("Goles visitante")
df.set_xlabel(" # de Goles")

plt.barh(df_archivoExcel['visitante'],df_archivoExcel['goles_visita'])
plt.show()

fig, df = plt.subplots()
df.set_title("Cantidad de goles de todos los partidos")
df.set_ylabel("Equipo")
df.set_xlabel(" # de Goles")

plt.barh(df_archivoExcel['pais_x'], df_archivoExcel['goles_local'] + df_archivoExcel['goles_visita'])
plt.rc('xtick', labelsize=10) 
plt.rc('ytick', labelsize=6)
plt.show()



#plt.barh(archivoExcel['goles_local'] , [ 'local'],archivoExcel['goles_visita'] , ['visita'])
#plt.show()
#plt.pie(archivoExcel['goles_visita'],labels=archivoExcel['goles_local'])
#plt.show()}