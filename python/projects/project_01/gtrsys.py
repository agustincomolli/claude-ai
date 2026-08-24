"""
Sistema de Gestión de Tickets de Reparación

Versión en consola, simplificada, de un sistema con menú interactivo para
cargar, consultar y gestionar tickets de reparación de equipos.
"""

TOTAL_WIDTH = 80
MARGIN_LEFT = 12


def print_header():
    """
    Imprime el encabezado de la aplicación
    """
    title = "📋 === SISTEMA DE GESTIÓN DE REPARACIONES === [x]"

    # Imprimir el encabezado.
    print(f"\n+{'-' * (TOTAL_WIDTH - 2)}+")
    print(f"{title:^{TOTAL_WIDTH}}")
    print(f"+{'-' * (TOTAL_WIDTH - 2)}+\n")


def input_choice(menu_length):
    """
    Valida que el usuario ingrese un número entre las opciones de menú.

    Args:
        menu_lenght: cantidad de opciones que hay en el menú.

    Returns:
        El número de la opción elegida por el usuario.
    """
    while True:
        try:
            menu_selected = int(
                input(f"\n{' ' * MARGIN_LEFT}Seleccione una opción: "))
            if menu_selected <= 0 or menu_selected > menu_length:
                raise ValueError
            return menu_selected
        except ValueError:
            error_message = "❌ ERROR: Debe ingresar una opción válida del 1 "
            error_message += f"al {menu_length}."
            print(f"{' ' * MARGIN_LEFT}{error_message}")


def show_menu():
    """
    Muestra el menú de opciones en la pantalla.

    Returns:
        El número de menú elegido por el usuario.
    """
    menu_list = (
        "Cargar nueva reparación",
        "Listar todas las reparaciones",
        "Buscar reparaciones por cliente",
        "Marcar reparación como entregada",
        "Ver estadísticas",
        "Salir"
    )

    print_header()
    print(f"{' ' * MARGIN_LEFT}MENU PRINCIPAL\n")

    # Opciones del menú
    for i, menu_item in enumerate(menu_list):
        print(f"{' ' * MARGIN_LEFT}{i+1}. {menu_item}")

    return input_choice(len(menu_list))


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

    Returns:
        Diccionario que contiene los datos de la reparación.
    """

    print_header()
    print("NUEVA REPARACIÓN\n")

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


def press_enter_to_continue():
    """
    Genera una pausa en el programa hasta que el usuario presiona ENTER
    """

    input("\nPresione ENTER para continuar...")


def print_repairs():
    """
    Imprime una tabla con las reparaciones cargadas.
    """
    # Especificar anchos de columnas para la tabla.
    w1, w2, w3, w4, w5, sign = 4, 20, 25, 11, 15, 2

    print_header()
    print(f"{'LISTADO DE REPARACIONES':^{TOTAL_WIDTH}}\n")
    print(f"{'ID':>{w1}} {'CLIENTE':<{w2}} {'EQUIPO':<{w3}} "
          f"{'COSTO':>{w4 + sign}} {'ESTADO':<{w5}}")

    for reparation_id, reparation in reparations.items():
        row = f"{reparation_id:>{w1}} {reparation['nombre']:<{w2}} "
        row += f"{reparation['equipo']:<{w3}} "
        row += f"$ {reparation['costo estimado']:>{w4}.2f} "
        row += f"{reparation['estado']:<{w5}}"
        print(row)

    press_enter_to_continue()


# Maneja el ID autoincremental.
last_id = 0
reparations = {}

while True:
    user_choice = show_menu()
    if user_choice == 1:
        new_id = last_id + 1
        reparations[str(new_id)] = new_repair()
        last_id = new_id
    if user_choice == 2:
        print_repairs()
    if user_choice == 3:
        pass
    if user_choice == 4:
        pass
    if user_choice == 5:
        pass
    if user_choice == 6:
        print("\n¡Hasta pronto! 👋")
        break
