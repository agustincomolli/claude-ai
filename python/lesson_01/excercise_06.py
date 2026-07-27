"""
Cálculo de tiempo de backup
Pedí el tamaño total de datos a respaldar en GB (float) y la velocidad 
de transferencia en MB/s (float). Calculá el tiempo estimado en segundos, 
y convertilo a horas, minutos y segundos usando // y % (sin usar el módulo 
time ni nada externo, solo aritmética). Mostrá el resultado como "2h 15m 42s".
"""

MINUTES_IN_HOUR = 60
SECONDS_IN_HOUR = 3600

print("=== Cálculo de tiempo de backup ===")

total_size_gb = float(input("Tamaño total en GB: "))
transfer_speed = float(input("Velocidad de transferencia: "))

total_size_mb = total_size_gb * 1024
estimated_time = total_size_mb / transfer_speed
hours = estimated_time // SECONDS_IN_HOUR
minutes_left = estimated_time % SECONDS_IN_HOUR
minutes = minutes_left // MINUTES_IN_HOUR
seconds = minutes_left % MINUTES_IN_HOUR

print(f"\nTiempo estimado de copia: {hours:.0f}h {minutes:.0f}m {seconds:.0f}s")
