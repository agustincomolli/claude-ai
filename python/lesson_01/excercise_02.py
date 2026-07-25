"""
Cálculo de presupuesto
Pedí el costo de repuesto y el costo de mano de obra (dos float). Calculá:

* El subtotal
* Un recargo del 5% si el total supera $50000 (usando comparación, guardalo 
en una variable booleana, no hace falta if todavía — pensá cómo resolverlo 
solo con operadores)
* El total final

Mostrá todo prolijo con f-strings, con 2 decimales (f"{valor:.2f}").
"""

print("*** Cálculo de presupuesto ***")
spare_part = float(input("Costo del repuesto: "))
labor = float(input("Mano de obra: "))
subtotal = spare_part + labor
surcharge = subtotal > 50000
total= subtotal + surcharge

print(
    "\n       === PRESUPUESTO ===\n"
    f"Costo del Repuesto: $ {spare_part:>10.2f}\n"
    f"Mano de obra:       $ {labor:>10.2f}\n"
    "----------------------------------\n"
    f"Subtotal:           $ {subtotal:>10.2f}\n"
    f"Recargo (5%):         {surcharge}\n"
    "----------------------------------\n"
    f"Total:              $ {total:>10.2f}"
)
