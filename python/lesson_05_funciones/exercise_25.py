"""
Función de validación reutilizable

Escribí una función pedir_numero_positivo(mensaje) que reciba un mensaje 
para el input, y devuelva (con return) un float válido y mayor a cero, 
usando el patrón while/try/except/raise que ya conocés. Usala para 
reescribir el ejercicio 21 (calculadora de presupuesto): ahora, pedir el 
costo del repuesto y la mano de obra tienen que ser simplemente dos 
llamadas a esta función, sin repetir el bloque de validación dos veces.
"""


def ask_positive_number(message):
    """
    Pide al usuario que ingrese un número mayor a 0.

    Args:
        message: Mensaje que se mostrará al usuario.

    Returns: Número float mayor a 0.
    """

    while True:
        try:
            number = float(input(message))
            if number <= 0:
                raise ValueError("El número debe ser mayor a 0.")
            return number
        except ValueError as error:
            print(f"ERROR: {error}")


print("=== Cálculo de presupuesto con FUNCIONES ===")

spare_part = ask_positive_number("\nCosto del repuesto: ")
labor = ask_positive_number("Mano de obra: ")

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
