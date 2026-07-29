"""
Clasificador de tickets de soporte por prioridad
Pedí: tipo de problema (input, texto libre) y si el cliente es "empresa"
o "particular" (input). Usando if/elif/else (podés anidar), determiná 
la prioridad:

- Si el tipo de problema contiene la palabra "servidor" (usá el operador in 
sobre strings) Y es empresa → prioridad "CRÍTICA"
- Si contiene "servidor" pero es particular → prioridad "ALTA"
- Si no contiene "servidor" pero es empresa → prioridad "MEDIA"
- En cualquier otro caso → prioridad "BAJA"
"""

print("=== Clasificador de tickets de soporte por prioridad ===")

problem_type = input("Tipo de problema: ")
client = input("¿Empresa o particular? ")
IS_ENTERPRISE = client.lower() == "empresa"
KEYWORD = "servidor"

if KEYWORD in problem_type and IS_ENTERPRISE:
    PRIORITY = "CRITICA"
elif KEYWORD in problem_type:
    PRIORITY = "ALTA"
elif IS_ENTERPRISE:
    PRIORITY = "MEDIA"
else:
    PRIORITY = "BAJA"

print(
    "\n+-----------------------------+"
    "\n+ La prioridad del ticket es: +"
    "\n+-----------------------------+"
    f"\n             {PRIORITY}"
    "\n+-----------------------------+"
    )
