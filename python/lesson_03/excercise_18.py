"""
Ficha de cliente con historial de reparaciones (avanzado)

Creá un diccionario que represente un cliente, con las claves: 
"nombre", "email", "reparaciones" (una lista de diccionarios, donde cada 
reparación tiene "fecha", "descripcion" y "costo"). Cargá los datos del 
cliente y 3 reparaciones por input, dentro de un for para las reparaciones. 
Después mostrá una ficha completa del cliente, recorriendo la lista de 
reparaciones con enumerate() para numerarlas, y calculá el costo total 
acumulado de todas sus reparaciones.
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
    reparation = {
        "fecha": input("Fecha: "),
        "descripcion": input("Descripción: "),
        "costo": float(input("Costo: "))
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
