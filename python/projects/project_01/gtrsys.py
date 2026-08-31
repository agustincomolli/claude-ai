"""
Sistema de Gestión de Tickets de Reparación

Versión en consola, simplificada, de un sistema con menú interactivo para
cargar, consultar y gestionar tickets de reparación de equipos.
"""

TOTAL_WIDTH = 80
MARGIN_LEFT = 12

DATA_TEST = {'1': {'nombre': 'Agustín',
                   'equipo': 'HP 250 G8',
                   'descripcion': 'Formateo',
                   'costo estimado': 100000.0,
                   'estado': 'pendiente'
                   },
             '2': {'nombre': 'Lorena',
                   'equipo': 'HP 250 G6',
                   'descripcion': 'Instalación de Office 365',
                   'costo estimado': 40000.0,
                   'estado': 'pendiente'},
             '3': {'nombre': 'Leonardo Alem',
                   'equipo': 'PC',
                   'descripcion': 'Eliminación de malware',
                   'costo estimado': 100000.0,
                   'estado': 'pendiente'},
             '4': {'nombre': 'Tito Marquez',
                   'equipo': 'PC',
                   'descripcion': 'Reemplazo motherboard',
                   'costo estimado': 500000.0,
                   'estado': 'pendiente'},
             '5': {'nombre': 'Carlitos',
                   'equipo': 'MSI', 'descripcion': 'Formateo',
                   'costo estimado': 100000.0,
                   'estado': 'pendiente'},
             '6': {'nombre': 'Gabriel Alayón',
                   'equipo': 'PC Cx Intel I3', 'descripcion':
                   'Cambio de gabinete', 'costo estimado': 100000.0,
                   'estado': 'pendiente'},
             '7': {'nombre': 'Adrián',
                   'equipo': 'Notebook',
                   'descripcion': 'Instalación de Linux Mint',
                   'costo estimado': 100000.0,
                   'estado': 'pendiente'},
             '8': {'nombre': 'Agustín',
                   'equipo': 'Samsung NP300EAC',
                   'descripcion': 'Instalación de Linux Mint XFCE',
                   'costo estimado': 100000.0,
                   'estado': 'pendiente'},
             '9': {'nombre': 'Gustavo',
                   'equipo': 'MacBook Pro M4',
                   'descripcion': 'Instalación Office',
                   'costo estimado': 50000.0,
                   'estado': 'pendiente'},
             '10': {'nombre': 'Gabriel Alayón',
                    'equipo': 'PC',
                    'descripcion': 'Reemplazo de fuente',
                    'costo estimado': 40000.0,
                    'estado': 'pendiente'}}


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
        menu_length: cantidad de opciones que hay en el menú.

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
            error_message = "ERROR: Debe ingresar una opción válida del 1"
            error_message += f"al {menu_length}. ❌"
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
        message: Mensaje que se mostrará al usuario.

    Returns:
        cost: número flotante que contiene el valor válido
    """
    while True:
        try:
            cost = float(input(message))
            if cost <= 0:
                raise ValueError("El valor ingresado debe ser mayor a 0. ❌")
            return cost
        except ValueError as err:
            print(f"ERROR: {err} ❌")


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


def print_repairs(data):
    """
    Imprime una tabla con las reparaciones cargadas.

    Args:
        data: Diccionario con los datos a imprimir.
    """
    # Especificar anchos de columnas para la tabla:
    # w1: ID, w2: Cliente, w3: Equipo, w4: Costo,
    # w5: Estado, sign: '$ '
    w1, w2, w3, w4, w5, sign = 4, 20, 25, 11, 15, 2

    print_header()
    print(f"{'LISTADO DE REPARACIONES':^{TOTAL_WIDTH}}\n")

    if not data:
        print("No hay datos para mostrar. ❌")
        press_enter_to_continue()
        return

    print(f"{'ID':>{w1}} {'CLIENTE':<{w2}} {'EQUIPO':<{w3}} "
          f"{'COSTO':>{w4 + sign}} {'ESTADO':<{w5}}")

    for reparation_id, reparation in data.items():
        row = f"{reparation_id:>{w1}} {reparation['nombre']:<{w2}} "
        row += f"{reparation['equipo']:<{w3}} "
        row += f"$ {reparation['costo estimado']:>{w4}.2f} "
        row += f"{reparation['estado']:<{w5}}"
        print(row)

    press_enter_to_continue()


def find_reparations(data):
    """
    Pide el nombre de un cliente y busca las reparaciones que tiene.

    Args:
        data: Diccionario con las reparaciones.

    Returns:
        Un diccionario de diccionarios con la coincidencias encontradas.
    """
    print_header()
    print(f"{'BUSCAR REPARACIONES':^{TOTAL_WIDTH}}\n")
    name = input("Nombre del cliente: ").lower()
    filtered_dict = {}
    for key, value in data.items():
        if name in value["nombre"].lower():
            filtered_dict[key] = value

    return filtered_dict


def update_reparation_status(data):
    """
    Pide un ID de reparación y cambia su estado a "entregada".

    Args:
        data: Diccionario con las reparaciones.
    """

    print_header()
    print(f"{'ACTUALIZAR ESTADO DE REPARACION':^{TOTAL_WIDTH}}\n")

    while True:
        try:
            reparation_id = int(input("ID de reparación: "))
            break
        except ValueError:
            print("\nERROR: Debe ingresar un número entero. ❌")

    try:
        reparation = data[str(reparation_id)]
        reparation["estado"] = "entregada"
        return str(reparation_id), reparation
    except KeyError:
        print("\nERROR: No existe ese número de reparación. ❌")
        press_enter_to_continue()


def view_statistics(data):
    """
    Muestra la cantidad total de reparaciones cargadas, cantidad pendientes 
    vs. entregadas, el costo total acumulado de todas las reparaciones, y el 
    costo promedio

    Args:
        data: Diccionario con las reparaciones.
    """
    total_reparations = len(data)
    pending, delivered = 0, 0
    total_cost, average_cost = 0.0, 0.0

    print_header()
    print(f"{'VER ESTADISTICAS':^{TOTAL_WIDTH}}\n")

    if total_reparations:
        for value in data.values():
            if value["estado"] == "pendiente":
                pending += 1
            else:
                delivered += 1
            total_cost += value["costo estimado"]

        average_cost = total_cost / total_reparations

        print(f"\nTotal de reparaciones:   {total_reparations:>9}"
              f"\nReparaciones pendientes: {pending:>9}"
              f"\nReparaciones entregadas: {delivered:>9}"
              f"\nCosto total acumulado:   $ {total_cost:>10.2f}"
              f"\nCosto promedio:          $ {average_cost:>10.2f}"
              )
    else:
        print("No hay reparaciones cargadas. ❌")

    press_enter_to_continue()


# Maneja el ID autoincremental.
last_id = 0
reparations = {}
# Datos de prueba, para producción comentar las dos líneas.
reparations = DATA_TEST.copy()
last_id = int(list(reparations)[-1])

while True:

    user_choice = show_menu()
    if user_choice == 1:
        new_id = last_id + 1
        reparations[str(new_id)] = new_repair()
        last_id = new_id
        print("\nReparación agregada correctamente. ✔️")
        press_enter_to_continue()
    elif user_choice == 2:
        print_repairs(reparations)
    elif user_choice == 3:
        filtered_reparations = find_reparations(reparations)
        if filtered_reparations:
            print_repairs(filtered_reparations)
        else:
            print("\nNo se han encontrado reparaciones para ese cliente. ❌")
            press_enter_to_continue()
    elif user_choice == 4:
        reparation_key, reparation_value = update_reparation_status(
            reparations)
        reparations[reparation_key]=reparation_value
        print("\nEstado de la reparación: ENTREGADA ✔️")
        press_enter_to_continue()
    elif user_choice == 5:
        view_statistics(reparations)
    elif user_choice == 6:
        print("\n¡Hasta pronto! 👋")
        break
