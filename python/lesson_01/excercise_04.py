"""
Comparador de dos presupuestos
Pedí el precio de dos proveedores distintos para la misma reparación. 
Usando solo operadores de comparación y lógicos, generá tres variables 
booleanas: primero_mas_barato, son_iguales, diferencia_significativa 
(diferencia mayor al 20% del menor precio). Mostralas todas.
"""

print("=== Comparador de dos presupuestos ===")

budget_1 = float(input("Presupuesto 'Porveedor 1': "))
budget_2 = float(input("Presupuesto 'Porveedor 2': "))

is_first_cheaper = budget_1 < budget_2
are_equals = budget_1 == budget_2
case_1 = (budget_1 < budget_2) and ((budget_2 - budget_1) > budget_1 * .2)
case_2 = (budget_2 < budget_1) and ((budget_1 - budget_2) > budget_2 * .2)
is_significant_difference = case_1 or case_2

print(
    f"\n¿El primer presupuesto es menor? {is_first_cheaper}\n"
    f"¿Los dos presupuestos son iguales? {are_equals}\n"
    f"¿Hay alguna diferencia significativa (> al 20%)? {is_significant_difference}"
    )
