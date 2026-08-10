"""
Divisor de gastos entre técnicos (nuevo escenario)

* Pedí un monto total de un gasto compartido (float) y la cantidad de 
técnicos entre los que se divide (int), ambos con validación try/except. 
* Calculá cuánto le toca a cada uno, manejando específicamente el caso de 
ZeroDivisionError si alguien ingresa 0 técnicos (mostrando un mensaje 
claro, sin que el programa se caiga).
"""

print("=== Divisor de gastos entre técnicos ===\n")

while True:
    try:
        shared_expenses = float(input("Gastos compartidos: "))
        break
    except ValueError:
        print("ERROR: Debe ingresar un número.")

while True:
    try:
        technicians = int(input("Cantidad de técnicos: "))
        break
    except ValueError:
        print("ERROR: Debe ingresar un número.")

try:
    to_pay = shared_expenses / technicians
    print(f"\nCada técnico tendrá que pagar $ {to_pay:.2f}")
except ZeroDivisionError:
    print("ERROR: No se puede dividir por 0.")
