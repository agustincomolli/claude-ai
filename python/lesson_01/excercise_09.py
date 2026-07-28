"""
Cotización con recargo por urgencia y descuento por cliente frecuente 
(el más difícil)
Pedí: costo base de la reparación (float), si el cliente pidió "urgente" 
(input que devuelve "si" o "no" — convertilo vos a bool), y la cantidad 
de reparaciones previas que tuvo ese cliente (int).

Calculá, sin usar if, solo con operadores lógicos y aritméticos:

- recargo_urgencia: 25% del costo base si es urgente, si no, 0
- descuento_cliente_frecuente: 10% del costo base si tuvo 5 o más reparaciones 
previas, si no, 0
- costo_final: costo base + recargo − descuento

Pista: vas a tener que reusar el mismo patrón condición and valor que analizamos 
arriba — pero ahora entendiendo por qué funciona, no de memoria. Mostrá el desglose 
completo, prolijo, con signo +/− visible en cada línea.
"""

print("=== Cotización con recargo por urgencia y descuento por cliente frecuente ===\n")

base_cost = float(input("Costo base de la reparación: "))
is_urgent = input("¿Es urgente? [s|n]: ") == "s"
previous_repairs = int(input("Cantidad de reparaciones previas: "))

print("\nCalculando 🤔 ...")

rush_surcharge = is_urgent and base_cost * 0.25
frequent_customer_discount = previous_repairs >= 5 and base_cost * 0.10
final_cost = base_cost + rush_surcharge + frequent_customer_discount

print(
    f"\nCosto base:            $ {base_cost:>10.2f}"
    f"\nRecargo por urgencia:  $ {rush_surcharge:>10.2f}"
    f"\nDescuento por cliente: $ {frequent_customer_discount:>10.2f}"
    f"\n------------------------------------------"
    f"\nTotal:                 $ {final_cost:>10.2f}"
)
