"""
Función con múltiples validaciones (avanzado)

Escribí una función cargar_reparacion() que pida por input fecha, 
descripción y costo de una reparación (validando el costo como en 
el ejercicio 24, con reintentos ante error), y devuelva un diccionario 
con esos tres datos. Usala dentro de un for que la llame 3 veces para 
reescribir el ejercicio 24 — el bloque de carga de una reparación 
individual ya no debería estar repetido/expandido en el cuerpo 
principal del programa.
"""


def load_reparation():
    """
    Genera un diccionario con los datos de una reparación.

    Returns:
        job: Diccionario que contiene la información cargada sobre una 
             reparación.
    """
    date = input("Fecha: ")
    description = input("Descripción: ")
    while True:
        try:
            cost = float(input("Costo: "))
            if cost <= 0:
                raise ValueError("El costo debe ser mayor a 0.")
            break
        except ValueError as error:
            print(f"ERROR: {error}")

    job = {
        "fecha": date,
        "descripcion": description,
        "costo": cost
    }

    return job


W1, W2, W3, W4 = 6, 12, 33, 10
TOTAL_WIDTH = 66

client: dict = {
    "nombre": "",
    "email": "",
    "reparaciones": []
}

print("=== Ficha de cliente con historial de reparaciones ===")

client["nombre"] = input("\nNombre: ")
client["email"] = input("Correo: ")
for i in range(3):
    new_reparation = load_reparation()
    client["reparaciones"].append(new_reparation)

print(f"+{'-'*(TOTAL_WIDTH - 2)}+")
print(f"{'FICHA DEL CLIENTE':^{TOTAL_WIDTH}}")
print(f"+{'-'*(TOTAL_WIDTH - 2)}+")
print(
    f"\n\tNombre:\t{client['nombre']}"
    f"\n\tCorreo:\t{client['email']}"
    f"\n\n {'REP.':^{W1}}{'FECHA':^{W2}} {'DESCRIPCION':<{W3}}{'COSTO':>{W4}}"
)

total = 0.0
for index, reparation in enumerate(client["reparaciones"]):
    row = f" {index+1:^{W1}}{reparation['fecha']:^{W2}} {reparation['descripcion']:<{W3}} "
    row += f"${reparation['costo']:>{W4}.2f}"
    print(row)
    total += reparation['costo']

print(f"\n {'TOTAL':<{W1+W2+W3+1}} ${total:>{W4}.2f}")

print(f"+{'-'*(TOTAL_WIDTH - 2)}+")
