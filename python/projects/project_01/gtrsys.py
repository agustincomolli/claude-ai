"""
Sistema de Gestión de Tickets de Reparación

Versión en consola, simplificada, de un sistema con menú interactivo para 
cargar, consultar y gestionar tickets de reparación de equipos. 
"""


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

    print("\n📋 === SISTEMA DE GESTIÓN DE REPARACIONES === [x]\n")
    for i, menu_item in enumerate(menu_list):
        print(f"{' '*7}{i+1}. {menu_item}")

    while True:
        try:
            menu_selected = int(input("\nSeleccione una opción: "))
            if menu_selected <= 0 or menu_selected > len(menu_list):
                raise ValueError
            break
        except ValueError:
            print("ERROR: Debe ingresar una opción válida.")

    return menu_selected


while True:
    user_choice = show_menu()
    if user_choice == 6:
        print("\n¡Hasta pronto! 👋")
        break
    print(f"Eligió: {user_choice}")
    input()
