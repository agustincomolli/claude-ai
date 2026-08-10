"""
Reescritura robusta de la ficha de equipo (ejercicio 1)

Retomá tu ejercicio 1 (ficha de equipo). Envolvé la conversión de la 
antigüedad en un while + try/except, de forma que si el usuario ingresa 
un valor no numérico, se le pida de nuevo sin romper el programa, hasta 
que ingrese algo válido.
"""

print("=== FICHA RAPIDA DE EQUIPO ===")
brand = input("Marca: ")
model = input("Modelo: ")

while True:
    try:
        age_equipment = int(input("Antigüedad (en años): "))
        break
    except ValueError:
        print("ERROR: Debe ingresar un número entero.")

warranty = age_equipment < 1

print("\n=== FICHA DE EQUIPO ===\n"
      f"Marca: {brand}\n"
      f"Modelo: {model}\n"
      f"Antigüedad: {age_equipment} años\n"
      f"En garantía: {warranty}"
      )
