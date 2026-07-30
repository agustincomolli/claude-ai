"""
Generador de reporte de diagnóstico de red
Con un for y range(), simulá "ping" a 5 IPs consecutivas desde 192.168.1.1 
(podés armar el string de la IP concatenando el número de host con el resto 
fijo). En cada vuelta, pedí por input si respondió ("s"/"n"). Contá cuántas 
respondieron y cuántas no. Al final, con if/elif/else: todas respondieron → 
"Red estable"; menos del 50% respondió → "Fallo crítico de red"; cualquier 
otro caso → "Red inestable, revisar equipos caídos".
"""

print("=== Generador de reporte de diagnóstico de red ===")

PINGS = 5
affirmative = 0

for i in range(1, PINGS + 1):
    print(f"ping 192.168.1.{i}")
    while True:
        response = input("¿Respondió? [s|n]: ")
        if response.lower() in ("s", "n"):
            break
        print("Tiene que ingresar 's' o 'n'.")
    if response == "s":
        affirmative += 1

if affirmative == PINGS:
    print("Red estable")
elif affirmative < PINGS / 2:
    print("Fallo crítico de red")
else:
    print("Red inestable, revisar equipos caídos")
