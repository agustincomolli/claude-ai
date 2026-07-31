"""
Refactorización del comparador de presupuestos (versión definitiva)

Reescribí una vez más el comparador de presupuestos, pero ahora usando un 
diccionario {"Proveedor 1": precio, "Proveedor 2": precio, "Proveedor 3": 
precio} cargado con un for (pedile al usuario los 3 precios dentro de un 
bucle, sin repetir 3 veces el input). Con un solo for sobre .items(), 
encontrá el proveedor más barato, el más caro, y calculá si "todos están 
dentro del rango" (diferencia entre el más caro y el más barato menor al 
15% del más barato) — todo sin repetir lógica por cada proveedor. Usá min(), 
max() y las funciones que viste en la teoría.
"""

print("=== Refactorización del comparador de presupuestos (versión definitiva) ===")

suppliers = {}

# 1 - Cargar el diccionario.
for i in range(1, 4):
    suppliers[f"Proveedor {i}"] = float(input(f"Proveedor {i}: "))

# 2 - Encontrar el precio mínimo y máximo.
most_cheaper = min(suppliers.values())
most_expensive = max(suppliers.values())

# 3 - Saber si el primer proveedor es el más barato y si más de un proveedor
#     con el precio más barato.
is_first_cheaper = False
cheaper_count = 0
for supplier, price in suppliers.items():
    if price == most_cheaper:
        cheaper_count += 1
        is_first_cheaper = supplier == "Proveedor 1"

# 4 - Comprobar si todos están en rango.
is_in_range = (most_expensive - most_cheaper) < (most_cheaper * 0.15)

print(
    f"\n¿El primer proveedor es el más barato?     {is_first_cheaper}"
    f"\n¿Hay un empate en el mínimo?               {cheaper_count > 1}"
    f"\n¿Todos los presupuestos están en el rango? {is_in_range}"
)
