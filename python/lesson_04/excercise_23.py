"""
Consulta segura de inventario (usando lo del ejercicio 16)

* Armá un diccionario fijo en el código (no por input) que simule un 
inventario, por ejemplo {"mouse": 15, "teclado": 8, "monitor": 3}. 
* Pedí al usuario, en un bucle que se repite hasta que escriba "salir", 
el nombre de un producto, y mostrá su stock. 
* Manejá con try/except KeyError el caso de que el producto no exista en 
el inventario, mostrando un mensaje claro en vez de que el programa se rompa.
"""

inventory = {
    "disco ssd": 3,
    "memoria ddr4": 1,
    "pendrive 128gb": 2,
    "mouse usb": 4,
    "teclado usb": 4
}

print("=== Consulta segura de inventario ===")

while True:
    try:
        print("\nIngrese el producto a buscar o escriba 'salir' para finalizar")
        product = input(">: ").lower()
        if product == "salir":
            break
        print(f"Hay {inventory[product]} unidades en el inventario.")
    except KeyError:
        print("ERROR: el producto ingresado no existe en el inventario.")
