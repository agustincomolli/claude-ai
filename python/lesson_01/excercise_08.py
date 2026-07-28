"""
Cálculo de vida útil restante de una batería
Pedí la cantidad de ciclos de carga que ya tiene una batería (int) y la 
cantidad de ciclos de vida útil que garantiza el fabricante 
(int, típicamente 500 o 1000). Calculá:

- porcentaje_de_vida_consumido (float, con 2 decimales)
- ciclos_restantes (int)
- necesita_reemplazo_pronto: True si le queda menos del 15% de vida útil
- garantia_vencida: asumiendo que la garantía cubre 300 ciclos, True si ya los superó
"""

print("=== Cálculo de vida útil restante de una batería ===")

current_charging_cycles = int(input("Ciclos de carga actuales: "))
useful_life = int(input("Ciclos garantizados: "))

useful_life_consumed = (current_charging_cycles * 100) / useful_life
remaining_cycles = useful_life - current_charging_cycles
is_necessary_replace = useful_life_consumed < 15
is_warranty_expired = current_charging_cycles > 300

print(
    f"\nPorcentaje consumido:      {useful_life_consumed:.2f}%"
    f"\nCiclos restantes:          {remaining_cycles}"
    f"\n¿Es necesario reemplazar?  {is_necessary_replace}"
    f"\n¿Está la garantía vencida? {is_warranty_expired}\n"
)
