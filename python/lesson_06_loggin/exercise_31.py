"""
Escribí un pequeño programa que pida dos números y calcule la división. 
Envolvé la operación en try/except ZeroDivisionError y except ValueError. 
En el primer caso, usá logger.exception() para registrar el traceback completo. 
En el segundo, usá logger.error() con un mensaje simple (sin traceback, porque 
acá no hace falta tanto detalle). Compará ambos resultados en el archivo de log 
y notá la diferencia de información disponible.
"""

import logging

logging.basicConfig(
    level=logging.INFO,
    filemode= "a",
    filename="exercise_31.log",
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8"
)

logger = logging.getLogger(__name__)

try:
    num_1 = float(input("Número 1: "))
    num_2 = float(input("Número 2: "))
    result = num_1 / num_2
    print(f"{num_1} / {num_2} = {result}")
except ZeroDivisionError as error:
    print("ERROR: No se puede dividir por 0.")
    logger.exception("El usuario intentó dividir por 0.")
except ValueError:
    print("ERROR: Debe ingresar un número.")
    logger.error("El usuario ingresó un caracter no numérico.")
