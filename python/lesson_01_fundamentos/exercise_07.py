"""
Comparación de tres presupuestos con lógica combinada
Pedí precios de tres proveedores (float). Sin usar if, generá estas variables 
booleanas usando solo comparaciones y operadores lógicos (and, or, not):

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

is_first_cheaper = budget_1 <= budget_2 and budget_1 <= budget_3
is_second_cheaper = budget_2 < budget_1 and budget_2 <= budget_3
is_third_cheaper = (not is_first_cheaper) and (not is_second_cheaper)

draw_case_1 = (budget_1 == budget_2) and (budget_1 <= budget_3)
draw_case_2 = (budget_1 == budget_3) and (budget_1 <= budget_2)
draw_case_3 = (budget_2 == budget_3) and (budget_2 <= budget_1)
is_draw = draw_case_1 or draw_case_2 or draw_case_3

range_case_1 = is_first_cheaper and (
    budget_2 - budget_1 < budget_1 * .15) and (
    budget_3 - budget_1 < budget_1 * .15)
range_case_2 = is_second_cheaper and (
    budget_1 - budget_2 < budget_2 * .15) and (
    budget_3 - budget_2 < budget_2 * .15)
range_case_3 = is_third_cheaper and (
    budget_1 - budget_3 < budget_3 * .15) and (
    budget_2 - budget_3 < budget_3 * .15)
is_in_range = range_case_1 or range_case_2 or range_case_3

print(
    f"\n¿El primer proveedor es el más barato?     {is_first_cheaper}\n"
    f"¿Hay un empate en el mínimo?               {is_draw}\n"
    f"¿Todos los presupuestos están en el rango? {is_in_range}"
)
