"""
Calculadora de cuotas con validación (el más difícil)
Pedí monto a financiar (float) y cantidad de cuotas (int), validando con 
while que estén entre 1 y 12 (repetir el pedido con mensaje de error si 
no). Con if/elif/else, aplicá interés total:

1 a 3 cuotas → 0%
4 a 6 cuotas → 8%
7 a 12 cuotas → 15%

Con un for, mostrá el detalle cuota por cuota numerado ("Cuota 1: $ ...", etc.).
"""

print("=== Calculadora de cuotas con validación ===")

amount = float(input("Monto a financiar: "))
while True:
    installments = int(input("Cuotas (hasta 12): "))
    if 1 <= installments <= 12:
        break
    print("La cantidad de cuotas es entre 1 y 12.")

if 1 <= installments <= 3:
    INTEREST = 1.0
elif 4 <= installments <= 6:
    INTEREST = 1.08
else:
    INTEREST = 1.15

for i in range(1, installments + 1):
    print(f"Cuota {i:>2}: $ {(amount / installments) * INTEREST:.2f}")
