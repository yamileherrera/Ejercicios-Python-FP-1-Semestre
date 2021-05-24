#  Librerias
import matplotlib
import matplotlib.pyplot as plt

#  Generar Datos
#  Interactuar con listas
nombreProductos=['Arroz','Azucar','Vino','Leche']
ventaProductos=[100,50,30,20]

# Funciones que resuelven las preguntas

def totalVentas():
    sumTotVen=0
    for pos in range(4):
        sumTotVen=sumTotVen+ventaProductos[pos]
    print("El total de Venta es: ",sumTotVen)
    return sumTotVen   
    
def promVenTot():
    promVen=0.0
    promVen=(totalVentas()/len(ventaProductos))
    return(promVen)
    
#Llamar a la función    
print("Total Ventas: ", totalVentas())
print("Promedio de Ventas: ", promVenTot())

#   Generar el gráfico
fig, ax = plt.subplots()
ax.set_title('VENTAS DE LA EMPRESA')
ax.set_ylabel('Valor')
ax.set_xlabel('Nombre Producto')
#  Crear el gráfico
plt.bar(nombreProductos,ventaProductos)
plt.show()








