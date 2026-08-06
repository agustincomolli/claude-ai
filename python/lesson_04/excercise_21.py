"""
Calculadora de presupuesto con validación completa

Retomá el ejercicio 2 (cálculo de presupuesto). Pedí el costo de repuesto 
y de mano de obra usando el patrón while + try/except para ambos valores. 
Además, usando raise ValueError dentro del mismo try, rechazá explícitamente 
valores negativos (un costo no puede ser negativo) — el except tiene que 
capturar tanto el error de conversión como el que vos mismo lanzás con raise.
"""

print("=== Cálculo de presupuesto ===")

while True:
    try:
        spare_part = float(input("Costo del repuesto: "))
        if spare_part < 0:
            raise ValueError("El número ingresado NO puede ser negativo.")
        break
    except ValueError as error:
        print(f"ERROR: {error}")

while True:
    try:
        labor = float(input("Mano de obra: "))
        if labor < 0:
            raise ValueError("El número ingresado NO puede ser negativo.")
        break
    except ValueError as error:
        print(f"ERROR: {error}")

subtotal = spare_part + labor
surcharge = subtotal * 0.05 if subtotal > 50000 else 0.0
total = subtotal + surcharge

print(
    "\n       === PRESUPUESTO ===\n"
    f"Costo del Repuesto: $ {spare_part:>10.2f}\n"
    f"Mano de obra:       $ {labor:>10.2f}\n"
    "----------------------------------\n"
    f"Subtotal:           $ {subtotal:>10.2f}\n"
    f"Recargo (5%):       $ {surcharge:>10.2f}\n"
    "----------------------------------\n"
    f"Total:              $ {total:>10.2f}"
)
