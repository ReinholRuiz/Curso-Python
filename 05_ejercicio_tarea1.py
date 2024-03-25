#Ejercicio 5 - Tarea 1 - Reinhol

""""
Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de
interés al año. Estos ahorros debido a intereses, que no se cobran hasta finales de
año, se te añaden al balance final de tu cuenta de ahorros. Escribir un programa que
comience leyendo la cantidad de dinero depositada en la cuenta de ahorros,
introducida por el usuario. Después el programa debe calcular y mostrar por pantalla la
cantidad de ahorros tras el primer, segundo y tercer años. Redondear cada cantidad a
dos decimales.

"""

monto_ahorro=float(input("Ingrese el monto que desea depositar a su cuenta de ahorros: "))

#conversión de la tasa (4%)= 4/100
tasa_interes_anual=0.04

#Función para el calculo del saldo por año
def calcular_saldo_anual(monto_ahorro, tasa_interes_anual, años):
    saldo = monto_ahorro * (1 + tasa_interes_anual) ** años
    return round(saldo, 2)

# Calcular y mostrar el saldo después de cada año
for año in range(1, 4):
    saldo = calcular_saldo_anual(monto_ahorro, tasa_interes_anual, año)
    print(f"Después del año {año}, el saldo es: {saldo}")

