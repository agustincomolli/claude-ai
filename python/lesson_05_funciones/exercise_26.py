"""
Refactorización del comparador de presupuestos (versión final, con función)

Retomá el ejercicio 15. Escribí una función 
analizar_presupuestos(presupuestos) que reciba el diccionario de presupuestos 
y devuelva (con return, podés devolver varios valores separados por coma) 
el precio más barato, el más caro, y si están todos dentro del rango del 15%. 
El programa principal solo tiene que cargar el diccionario y llamar a esta 
única función.
"""

print("=== Refactorización del comparador de presupuestos (con función) ===")


def analyze_budgets(budgets):
    """
    Compara un grupo de presupuestos e indica cuál es el más barato, cuál es
    el más caro y si están dentro del rango del 15%.

    Args:
        budgets: Diccionario que contiene los presupuestos.

    Returns:
        budget_most_cheaper: El presupuesto más barato,
        budget_most_expensive: El presupuesto más caro,
        budgets_is_in_range: indica si están en el rango adecuado
    """
    # Encontrar el precio mínimo y máximo.
    budget_most_cheaper = min(budgets.values())
    budget_most_expensive = max(budgets.values())

    # Comprobar si todos están en rango.
    budgets_is_in_range = (
        budget_most_expensive - budget_most_cheaper
    ) < (budget_most_cheaper * 0.15)

    return budget_most_cheaper, budget_most_expensive, budgets_is_in_range


suppliers = {}

# Cargar el diccionario.
for i in range(1, 4):
    suppliers[f"Proveedor {i}"] = float(input(f"Proveedor {i}: "))

most_cheaper, most_expensive, is_in_range = analyze_budgets(suppliers)

# Saber si el primer proveedor es el más barato y si más de un proveedor
#   con el precio más barato.
is_first_cheaper = suppliers["Proveedor 1"] == most_cheaper
cheaper_count = 0
for supplier, price in suppliers.items():
    if price == most_cheaper:
        cheaper_count += 1


print(
    f"\n¿El primer proveedor es el más barato?     {is_first_cheaper}"
    f"\n¿Hay un empate en el mínimo?               {cheaper_count > 1}"
    f"\n¿Todos los presupuestos están en el rango? {is_in_range}"
)
