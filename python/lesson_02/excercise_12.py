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
