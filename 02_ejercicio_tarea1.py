#Ejercicio 2 - Tarea 1 - Reinhol
""""
Escribir un programa que pida al usuario dos números enteros y muestre por pantalla
la <n> entre <m> da un cociente <c> y un resto <r> donde <n> y <m> son los números
introducidos por el usuario, y <c> y <r> son el cociente y el resto de la división entera
respectivamente.

"""
n=int(input("Ingrese el valor del primero número entero: "))
m=int(input("Ingrese el valor del segundo número entero: "))

c=n//m
r=n%m

mensaje=f"""

El resultado de {n} entre {m} da un cociente {c},
esta misma operación da un resto {r}, donde {n} y {m} son números enteros, 
{c} y {r} son el cociente y el resto de la división entera respectivamente.
"""
print(mensaje)