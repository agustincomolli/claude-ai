"""
Inventario de repuestos

Creá una lista de diccionarios, donde cada diccionario representa un 
repuesto con "nombre", "stock" (int) y "precio" (float). Cargá 4 repuestos 
pidiéndolos por input dentro de un for. Después, con otro for, mostrá un 
listado prolijo, y calculá: el valor total del inventario (stock * precio 
sumado de todos), y cuántos repuestos tienen stock menor a 3 (usando un 
contador, como en ejercicios anteriores).
"""

W1, W2, W3, W4 = 20, 10, 10, 10
TOTAL_WIDTH = W1+W2+W3+W4

print(f"{'=== Inventario de repuestos ===':^{TOTAL_WIDTH}}")

spare_parts = []

for i in range(4):
    name = input("\nNombre: ")
    stock = int(input("Stock: "))
    price = float(input("Precio: "))

    spare = {
        "nombre": name,
        "price": price,
        "stock": stock
    }
    spare_parts.append(spare)

print(f"\n+{'-'*(TOTAL_WIDTH)}+")
print(f" {'REPUESTO':<{W1}}{'PRECIO U.':>{W2}}{'STOCK':^{W3}}{'SUBTOTAL':>{W4}}")
print(f"+{'-'*(TOTAL_WIDTH)}+")

for spare in spare_parts:
    name = spare["nombre"]
    price = spare["price"]
    stock = spare["stock"]
    subtotal = stock * price
    print(
        f" {name:<{W1}}{price:>{W2}.2f}{stock:^{W3}.0f}{subtotal:>{W4}.2f}"
    )
