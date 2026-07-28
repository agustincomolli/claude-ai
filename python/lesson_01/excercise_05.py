"""
Diagnóstico de temperatura de CPU
Pedí la temperatura actual de una CPU en grados Celsius (float) y la 
temperatura máxima segura según el fabricante (float). Calculá:

- porcentaje_del_maximo: qué porcentaje representa la temperatura actual 
  respecto a la máxima.
- margen_restante: cuántos grados faltan para llegar al máximo.
- estado_critico: True si la temperatura actual supera el 90% del máximo.

Mostrá todo con 1 decimal de precisión, prolijo.
"""

print("=== Diagnóstico de temperatura de CPU ===")

current_temp = float(input("Temperatura actual: "))
maximum_safe_temp = float(input("Temperatura máxima: "))

percentage_of_maximum = (current_temp * 100) / maximum_safe_temp
remaining_margin = maximum_safe_temp - current_temp
critical_state = percentage_of_maximum > 90

print(
    "\n"
    f"Temperatura actual:        {current_temp:>4.1f}°\n"
    f"Temperatura máxima segura: {maximum_safe_temp:>4.1f}°\n"
    f"Porcentaje del máximo:     {percentage_of_maximum:>4.1f}%\n"
    f"Margen restante:           {remaining_margin:>4.1f}°\n"
    f"Estado crítico:            {critical_state}"
)
