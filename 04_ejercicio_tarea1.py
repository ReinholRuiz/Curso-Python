#Ejercicio 4 - Tarea 1 - Reinhol

""""
Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. Suele
hacer venta por correo y la empresa de logística les cobra por peso de cada paquete
así que deben calcular el peso de los payasos y muñecas que saldrán en cada
paquete a demanda. Cada payaso pesa 112 g y cada muñeca 75 g. Escribir un
programa que lea el número de payasos y muñecas vendidos en el último pedido y
calcule el peso total del paquete que será enviado.

"""
num_payasos = int(input("Ingrese el número de payasos vendidos: "))
num_munecas = int(input("Ingrese el número de muñecas vendidas: "))


peso_payaso = num_payasos*112  
peso_muneca = num_munecas*75   
    
peso_total_paquete = peso_payaso + peso_muneca
    


mensaje=f"""

El Peso de {num_payasos} payasos, equivale a {peso_payaso} gramos
El Peso de {num_munecas} muñecas, equivale a {peso_muneca} gramos
El peso total del paquete que será enviado es de {peso_total_paquete} gramos.
"""
print(mensaje)
