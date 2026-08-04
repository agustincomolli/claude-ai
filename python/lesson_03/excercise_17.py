"""
Registro de diagnóstico de red sin duplicados

Pedí al usuario, dentro de un while, que vaya ingresando direcciones IP 
que respondieron a un ping (una por vez), hasta que ingrese la palabra 
"fin". Guardalas en un set (para que si por error carga la misma IP dos 
veces, no se duplique). Al finalizar, mostrá cuántas IPs únicas 
respondieron y listalas todas con un for.
"""

print("=== Registro de diagnóstico de red sin duplicados ===")

ip = ""
ip_list = []

while True:
    ip = input("\nDirección IP ('fin' para salir): ").lower()
    if ip == "fin":
        break
    ip_list.append(ip)

ip_addresses = set(ip_list)
print("\nIPs que respondieron: ")
for ip in ip_addresses:
    print(f"- {ip}")
