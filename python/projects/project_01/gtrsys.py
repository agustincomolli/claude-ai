"""
Sistema de Gestión de Tickets de Reparación

Versión en consola, simplificada, de un sistema con menú interactivo para 
cargar, consultar y gestionar tickets de reparación de equipos. 
"""


def input_choice(margin_left, menu_length):
    """
    Valida que el usuario ingrese un número entre las opciones de menú.
    
    Args:
        margin_left: margen izquierdo para empezar a imprimir mensajes.
        menu_lenght: cantidad de opciones que hay en el menú.

    Returns:
        El número de la opción elegida por el usuario.
    """
    while True:
        try:
            menu_selected = int(
                input(f"\n{' ' * margin_left}Seleccione una opción: "))
            if menu_selected <= 0 or menu_selected > menu_length:
                raise ValueError
            return menu_selected
        except ValueError:
            error_message = "❌ ERROR: Debe ingresar una opción válida del 1 "
            error_message += f"al {menu_length}."
            print(f"{' ' * margin_left}{error_message}")


def show_menu():
    """
    Muestra el menú de opciones en la pantalla.

    Returns:
        El número de menú elegido por el usuario.
    """
    menu_list = (
        "Cargar nueva reparació",
        "Listar todas las reparaciones",
        "Buscar reparaciones por cliente",
        "Marcar reparación como entregada",
        "Ver estadísticas",
        "Salir"
    )

    total_width = 80
    title = "📋 === SISTEMA DE GESTIÓN DE REPARACIONES === [x]"
    margin_left = 12

    # Imprimir el encabezado.
    print(f"\n+{'-' * (total_width - 2)}+")
    print(f"{title:^{total_width}}")
    print(f"+{'-' * (total_width - 2)}+\n")

    # Opciones del menú
    for i, menu_item in enumerate(menu_list):
        print(f"{' ' * margin_left}{i+1}. {menu_item}")

    return input_choice(margin_left, len(menu_list))


def input_cost(message):
    """
    Valida que el usuario ingrese un número mayor a 0.

    Args:
        message: Mensaje que se motrará al usuario.

    Returns:
        cost: número flotante que contiene el valor válido
    """
    while True:
        try:
            cost = float(input(message))
            if cost <= 0:
                raise ValueError("El valor ingresado debe ser mayo a 0.")
            return cost
        except ValueError as err:
            print(f"ERROR: {err}")


def new_repair():
    """
    Carga los datos de una nueva reparación.
    """
    name = input("Nombre: ")
    equipment = input("Equipo [marca/model]: ")
    description = input("Descripción: ")
    estimated_cost = input_cost("Costo estimado: ")
    state = "pendiente"

    return {
        "nombre": name,
        "equipo": equipment,
        "descripcion": description,
        "costo estimado": estimated_cost,
        "estado": state
    }


last_id = 0
reparations = {}

while True:
    user_choice = show_menu()
    if user_choice == 1:
        new_id = last_id + 1
        reparations[str(new_id)] = new_repair()
        last_id = new_id
    if user_choice == 2:
        pass
    if user_choice == 3:
        pass
    if user_choice == 4:
        pass
    if user_choice == 5:
        pass
    if user_choice == 6:
        print("\n¡Hasta pronto! 👋")
        break
    print(f"Eligió: {user_choice}")
    print(f"\n{reparations}")
    input()
