"""
Reescritura del comparador de 3 presupuestos (ejercicio 7)
Tomá tu excercise_07.py y reescribilo usando if/elif/else. Tiene que quedar 
drásticamente más corto y legible que la versión original con and/or encadenados.

- proveedor_1_es_el_mas_barato
- hay_empate_en_el_minimo (dos o más proveedores tienen exactamente el mismo 
precio mínimo)
- todos_dentro_de_rango (la diferencia entre el más caro y el más barato es 
menor al 15% del más barato)
"""

print("=== Comparación de tres presupuestos ===")

budget_1 = float(input("Presupuesto 'Porveedor 1': "))
budget_2 = float(input("Presupuesto 'Porveedor 2': "))
budget_3 = float(input("Presupuesto 'Porveedor 3': "))

is_first_cheaper = (budget_1 <= budget_2) and (budget_1 <= budget_3)
is_second_cheaper = (budget_2 < budget_1) and (budget_2 <= budget_3)
is_third_cheaper = (not is_first_cheaper) and (not is_second_cheaper)

is_draw = False
is_in_range = False

if (budget_1 == budget_2 or budget_1 == budget_3) and is_first_cheaper:
    is_draw = True
elif (budget_2 == budget_3) and not is_first_cheaper:
    is_draw = True

if is_first_cheaper:
    is_in_range = (budget_2 - budget_1 < budget_1 * 0.15) and (
        budget_3 - budget_1 < budget_1 * 0.15)
elif is_second_cheaper:
    is_in_range = (budget_1 - budget_2 < budget_1 * 0.15) and (
        budget_3 - budget_2 < budget_2 * 0.15)
elif is_third_cheaper:
    is_in_range = (budget_1 - budget_3 < budget_1 * 0.15) and (
        budget_2 - budget_3 < budget_3 * 0.15)

print(
    f"\n¿El primer proveedor es el más barato?     {is_first_cheaper}"
    f"\n¿Hay un empate en el mínimo?               {is_draw}"
    f"\n¿Todos los presupuestos están en el rango? {is_in_range}"
)
