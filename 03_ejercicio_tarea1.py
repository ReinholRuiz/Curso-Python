#Ejercicio 2 - Tarea 1 - Reinhol

""""
Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y
el número de años, y muestre por pantalla el capital obtenido en la inversión.

cantidad por (interés dividido 100 más 1) elevado años
"""

monto_inversion=int(input("Ingrese el monto que desea invertir: "))
interes_anual=float(input("Ingrese el valor de la tasa de interes anual: "))
numero_años=int(input("Ingrese el número de años que desea mantener la inversión: "))

cantidad=monto_inversion*((interes_anual/100)+1)**numero_años

mensaje=f"""

La cantidad obtenida de la inversión de {monto_inversion}, a una tasa {interes_anual} anual,
en un tiempo definido de {numero_años}, es de: {round(cantidad, 2)}

"""
print(mensaje)