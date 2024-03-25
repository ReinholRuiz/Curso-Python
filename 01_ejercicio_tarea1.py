
#Ejercicio 1 - Tarea 1 - Reinhol
"""
Escribir un programa que pregunte el nombre del usuario en la consola y después de
que el usuario lo introduzca muestre por pantalla la cadena ¡Hola <nombre>!, donde
<nombre> es el nombre que el usuario haya introducido.
"""

nombre=(input("Ingrese su nombre: "))
apellido_1=(input("Ingrese su primer apellido: "))
apellido_2=(input("Ingrese su segundo apellido: "))

nombre_completo=f"{nombre.lower().capitalize()} {apellido_1.lower().capitalize()} {apellido_2.lower().capitalize()}"
print(f"¡Hola {nombre_completo}!")