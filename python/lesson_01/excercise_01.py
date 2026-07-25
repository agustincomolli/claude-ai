"""
Pedí al usuario: marca, modelo, y años de antigüedad del equipo. Calculá si 
está "en garantía" (menos de 1 año) usando una variable booleana, y mostrá 
una ficha formateada con f-strings, por ejemplo:

=== FICHA DE EQUIPO ===
Marca: HP
Modelo: Pavilion 15
Antigüedad: 0 años
En garantía: True
"""

print("=== FICHA RAPIDA DE EQUIPO ===")
brand = input("Marca: ")
model = input("Modelo: ")
age_equipment = float(input("Antigüedad (en años): "))
warranty = age_equipment < 1

print("\n=== FICHA DE EQUIPO ===\n"
      f"Marca: {brand}\n"
      f"Modelo: {model}\n"
      f"Antigüedad: {age_equipment} años\n"
      f"En garantía: {warranty}"
      )
