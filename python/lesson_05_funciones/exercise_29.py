"""
Sistema completo de diagnóstico de red con funciones 
(el más difícil, integrador)

Retomá el ejercicio 19 (comparador de rondas de ping). Escribí una función 
cargar_ips_ronda(nombre_ronda) que reciba un string (por ejemplo "Día 1") 
para mostrar en el mensaje del input, pida IPs hasta que el usuario escriba 
"fin", y devuelva el set resultante. Llamala dos veces (una por cada ronda) 
en el programa principal — el bloque de carga con el while ya no debería 
estar duplicado. Extra: escribí también una función 
comparar_rondas(set_1, set_2) que devuelva las tres relaciones de conjuntos 
(ambas, solo primera, solo segunda) como una tupla de tres elementos.
"""


def load_ip_round(round_name):
    """
    Carga una serie de direcciones IP hasta que el usuario ingrese 'fin'

    Args:
        round_name: El nombre que identifica la serie de direcciones IP

    Returns:
        Conjunto (set) con las direcciones IP ingresadas.
    """

    print(f"\n{round_name}")
    ip_list = []
    while True:
        new_ip = input("Dirección IP ('fin' para salir): ").lower()
        if new_ip == "fin":
            break
        ip_list.append(new_ip)

    return set(ip_list)


def compare_rounds(set_1, set_2):
    """
    Compara los conjuntos de direcciones IP y devuelve
    las IPs que respondieron en ambas rondas, las que respondieron 
    en la primera pero no en la segunda, y las que respondieron
    en la segunda pero no en la primera.

    Args:
        set_1: Conjunto de direcciones IP de la primera ronda.
        set_2: Conjunto de direcciones IP de la segunda ronda.

    Returns:
        Devuelve una tupla con tres elementos resultantes de las tres
        comparaciones.
    """
    return (set_1 & set_2, set_1 - set_2, set_2 - set_1)


print("=== Comparador de rondas de ping, día 1 vs día 2 ===")

ip_set_1 = load_ip_round("Día 1")
ip_set_2 = load_ip_round("Día 2")
resp_both, resp_round_1, resp_round_2 = compare_rounds(ip_set_1, ip_set_2)

print("\nIPs que respondieron en ambas rondas:")
print(resp_both)

print("\nPosibles equipos que se cayeron: ")
print(resp_round_1)

print("\nPosibles equipos que se recuperaron o son nuevos: ")
print(resp_round_2)
