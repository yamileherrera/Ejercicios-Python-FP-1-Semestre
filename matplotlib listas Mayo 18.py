#  Ejercicio que almacena en listas - procesa en funciones - 
#  Declar las Librerias a usar para la solución
import matplotlib
import matplotlib.pyplot as plt

#  General las listas con los datos inicializados
nombreProducto=['Ron','Aguardiante','Vino','Cerveza','Tequila']
existenciaProducto=[75,50,100,150,40]

#  Funciones que resuelven el problema
def f_calc_tot_existencias():
    sumaExistencias=0
    for posLis in range(4):
        sumaExistencias=sumaExistencias+existenciaProducto[posLis]
    print("Total Existencias: ",sumaExistencias)

        
def f_calc_tot_existencias_2():
    sumaExistencias=0
    for posLis in range(4):
        sumaExistencias=sumaExistencias+existenciaProducto[posLis]
    return(sumaExistencias)


#  Función que calcula el promedio de las existencias
def f_calc_prom_existencias():
    promExistencias = f_calc_tot_existencias_2()/len(existenciaProducto)
    return(promExistencias)
    
#  Llamado a las funciones que realizan los cálculos    
f_calc_tot_existencias()
print("Total Existencias 2: ",f_calc_tot_existencias_2())

print("Promedio de Existencias : ",f_calc_prom_existencias())


#  Gráficar la Información
fig, ax = plt.subplots()
# Definir el título del Gráfico
ax.set_title('GRÁFICO DE EXISTENCIAS DE PRODUCTOS')
ax.set_xlabel('Productos')
ax.set_ylabel('Existencias')

#  Crear el Gráfico
plt.bar(nombreProducto,existenciaProducto)

#  Publico el gráfico
plt.show()








