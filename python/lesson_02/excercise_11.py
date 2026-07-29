"""
Validador de credenciales de acceso remoto
Simulá un sistema de acceso a una PC remota. Pedí usuario y contraseña 
con un while, dando máximo 3 intentos. Si acierta antes de agotar los 
intentos, mostrar   y cortar el bucle (usá break). 
Si agota los 3 intentos, mostrar "Acceso bloqueado por seguridad". 
(Usuario/clave válidos: fijalos como constantes en el código, 
ej. "admin" / "1234").
"""

VALID_USER = "admin"
VALID_PASS = "1234"

print("=== Validador de credenciales de acceso remoto ===")

attempts = 0
while attempts < 3:
    username = input("\nUsuario: ")
    password = input("Contraseña: ")
    if username == VALID_USER and password == VALID_PASS:
        print("\nAcceso concedido")
        break
    attempts += 1
    if attempts == 3:
        print("\nAcceso bloqueado por seguridad")
