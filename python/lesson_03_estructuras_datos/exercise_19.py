"""
Comparador de rondas de ping, día 1 vs día 2 (el más difícil)

Pedí al usuario que cargue, en un set, las IPs que respondieron en una 
primera ronda de ping (usando el mismo patrón de "fin" del ejercicio 17). 
Después, pedile que cargue en un segundo set las IPs que respondieron en 
una segunda ronda. Usando operaciones de conjuntos (&, |, -), calculá y 
mostrá: las IPs que respondieron en ambas rondas, las IPs que respondieron 
en la primera pero no en la segunda (posibles equipos que se cayeron), y 
las IPs que respondieron en la segunda pero no en la primera (posibles equipos 
que se recuperaron o son nuevos).
"""

print("=== Comparador de rondas de ping, día 1 vs día 2 ===")

# Cargar IPs del día 1
print("\nDIA 1")
ip_list = []
while True:
    ip = input("Dirección IP ('fin' para salir): ").lower() 
    if ip == "fin":
        break
    ip_list.append(ip)

ip_set_1 = set(ip_list)

# Cargar Ips del día 2
print("\nDIA 2")
ip_list = []
while True:
    ip = input("Dirección IP ('fin' para salir): ").lower() 
    if ip == "fin":
        break
    ip_list.append(ip)

ip_set_2 = set(ip_list)

print("\nIPs que respondieron en ambas rondas:")
print(ip_set_1 & ip_set_2)

print("\nPosibles equipos que se cayeron: ")
print(ip_set_1 - ip_set_2)

print("\nPosibles equipos que se recuperaron o son nuevos: ")
print(ip_set_2 - ip_set_1)
