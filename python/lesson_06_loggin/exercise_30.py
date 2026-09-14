"""
Logger básico para el validador de números

Retomá la función ask_positive_number()/pedir_numero_positivo() del 
ejercicio 25. Agregale un logger (logging.getLogger(__name__)), 
configurado para escribir en un archivo validaciones.log. Cada vez 
que el usuario ingrese un valor inválido, registrá un logger.warning() 
con el valor que intentó ingresar. Cuando la validación sea exitosa, 
registrá un logger.info() con el número final aceptado.
"""

import logging

logging.basicConfig(
    level=logging.INFO,
    filename="validaciones.log",
    filemode="a",
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8"
)
logger = logging.getLogger(__name__)


def ask_positive_number(message):
    """
    Pide al usuario que ingrese un número mayor a 0.

    Args:
        message: Mensaje que se mostrará al usuario.

    Returns: Número float mayor a 0.
    """

    warning_message = "El usuario intentó ingresar '%s'"

    while True:
        try:
            user_input = input(message)
            number = float(user_input)
            if number <= 0:
                raise ValueError("El número debe ser mayor a 0.")
            logger.info("El usuario ingresó con éxito: %s", number)
            return number
        except ValueError as error:
            logger.warning(warning_message, user_input)
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
