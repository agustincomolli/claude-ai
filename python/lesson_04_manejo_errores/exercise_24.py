"""
Sistema de carga de reparaciones con validación total 
(el más difícil, integrador)

Retomá el ejercicio 18 (ficha de cliente). Reescribilo agregando validación 
robusta con try/except en la carga de cada reparación: el costo tiene que 
ser un número válido (capturar ValueError) y, además, usando raise, no 
puede ser negativo ni cero (un costo de reparación de $0 no tiene sentido 
de negocio). Si el usuario se equivoca, tiene que poder reintentar esa 
reparación puntual sin perder las que ya cargó correctamente ni tener que 
reiniciar todo el programa.

El ejercicio 24 en particular integra prácticamente todo lo visto hasta 
ahora (diccionarios, listas, for, enumerate, while, try/except, raise) — 
tomate tu tiempo. Cuando los tengas, los revisamos con el mismo detalle 
de siempre.
"""

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

    reparation = {
        "fecha": date,
        "descripcion": description,
        "costo": cost
    }
    client["reparaciones"].append(reparation)

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
