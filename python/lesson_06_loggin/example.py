"""
Ejemplo de uso del módulo loggin.
"""

import logging

logging.basicConfig(
    level=logging.INFO,
    filename="program.log",
    filemode="a",
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8"
)

logging.info("Programa iniciado")
logging.warning("El ID ingresado no corresponde a ninguna reparación")

try:
    cost = float(input("Costo: "))
except ValueError:
    print("Debe ingresar un número.")
    logging.error("El usuario ingresó un valor no numérico para el cost")

try:
    result = 100 / 0
except ZeroDivisionError:
    logging.exception("Error al calcular la división")

logger = logging.getLogger(__name__)

logger.info("Reparación cargada correctamente")
