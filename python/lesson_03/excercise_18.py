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

W1, W2, W3 = 12, 33, 10
TOTAL_WIDTH = 60

client = {
    "nombre": "",
    "email": "",
    "reparations": []
}

print("=== Ficha de cliente con historial de reparaciones ===")

client["nombre"] = input("\nNombre: ")
client["email"] = input("Correo: ")
for i in range(3):
    reparation = {
        "date": input("Fecha: "),
        "descripton": input("Descripción: "),
        "cost": float(input("Costo: "))
    }
    client["reparations"].append(reparation)

print(f"+{'-'*(TOTAL_WIDTH - 2)}+")
print(f"{'FICHA DEL CLIENTE':^{TOTAL_WIDTH}}")
print(f"+{'-'*(TOTAL_WIDTH - 2)}+")
print(
    f"\n\tNombre:\t{client['nombre']}"
    f"\n\tCorreo:\t{client['email']}"
    f"\n\n {'FECHA':^{W1}} {'DESCRIPCION':<{W2}}{'COSTO':>{W3}}"
)

total = 0.0
for reparation in client["reparations"]:
    row = f" {reparation['date']:^{W1}} {reparation['descripton']:<{W2}} "
    row += f"${reparation['cost']:>{W3}.2f}"
    print(row)
    total += reparation['cost']

print(f"\n {'TOTAL':<{W1+W2+1}} ${total:>{W3}.2f}")

print(f"+{'-'*(TOTAL_WIDTH - 2)}+")
