"""
Pedí una cantidad de memoria RAM en MB (int). Convertila a GB (float) y 
mostrá ambos valores. Extra: calculá cuántos "slots de 8GB" equivalentes 
representa usando el operador // (división entera) y % (resto).
"""

print("*** Conversión de unidades ***\n")
ram_in_mb = int(input("Ingrese la cantidad de memoria RAM en MB: "))
ram_in_gb = ram_in_mb / 1024
slots = int(ram_in_gb // 8)
remainder = ram_in_gb % 8

print(
    "\n=== RESUMEN DE LA CONVERSION ===\n"
    f"RAM en MB: {ram_in_mb}\n"
    f"RAM en GB: {ram_in_gb:.2f}\n"
    f"Slots: {slots}\n"
    f"Sobran: {remainder:.2f} GB"
    )
