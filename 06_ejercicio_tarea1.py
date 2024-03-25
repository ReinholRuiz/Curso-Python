#Ejercicio 6 - Tarea 1 - Reinhol

""""
Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene
un descuento del 60%. Escribir un programa que comience leyendo el número de
barras vendidas que no son del día. Después el programa debe mostrar el precio
habitual de una barra de pan, el descuento que se le hace por no ser fresca y el coste
final total.

"""

num_barras_no_frescas = int(input("Ingrese el número de barras de pan no frescas vendidas: "))
precio_por_barra = 3.49

descuento = 0.60 * precio_por_barra
costo_total = (precio_por_barra - descuento) * num_barras_no_frescas


mensaje=f"""

El precio normal de una barra de pan es: {precio_por_barra}€")
El descuento por no ser fresca es: {descuento}€ por barra")
El costo final total es: {round(costo_total,2)}€")

"""
print(mensaje)


