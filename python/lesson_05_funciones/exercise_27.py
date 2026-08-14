"""
Sistema de clasificación de tickets con función (usando el ejercicio 12)

Escribí una función clasificar_prioridad(descripcion, es_empresa) que 
devuelva el string de prioridad ("CRÍTICA", "ALTA", "MEDIA", "BAJA") 
según la misma lógica del ejercicio 12. Escribí también una función 
mostrar_resultado(prioridad) que se encargue solamente de imprimir el 
resultado con el formato de caja que ya tenías. El programa principal 
pide los datos, llama a clasificar_prioridad(), guarda el resultado, 
y se lo pasa a mostrar_resultado().
"""


def classify_priority(description, is_company):
    """
    Clasifica la prioridad de un ticket de soporte técnico.

    Args:
        description: La descripción del problema
        is_company: True si el cliente es una empresa

    Returns:
        Devuelve un string con la prioridad ("CRÍTICA", "ALTA", "MEDIA", 
        "BAJA")
    """
    keyword = "servidor"
    description = description.lower()

    if keyword in description and is_company:
        return "CRITICA"
    if keyword in description:
        return "ALTA"
    if is_company:
        return "MEDIA"

    return "BAJA"


def show_results(priority):
    """
    Imprime en pantalla qué prioridad tiene un ticket.

    Args:
        priority: "CRÍTICA", "ALTA", "MEDIA", "BAJA"
    """
    print(
        "\n+-----------------------------+"
        "\n| La prioridad del ticket es: |"
        "\n+-----------------------------+"
        f"\n             {priority}"
        "\n+-----------------------------+"
    )


print("=== Clasificador de tickets de soporte por prioridad ===")

problem_type = input("Tipo de problema: ")
client = input("¿Empresa o particular? ")
IS_ENTERPRISE = client.lower() == "empresa"

PRIORITY_TYPE = classify_priority(problem_type, IS_ENTERPRISE)

show_results(PRIORITY_TYPE)
