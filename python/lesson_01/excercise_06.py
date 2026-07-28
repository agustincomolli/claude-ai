"""
Cálculo de tiempo de backup
Pedí el tamaño total de datos a respaldar en GB (float) y la velocidad 
de transferencia en MB/s (float). Calculá el tiempo estimado en segundos, 
y convertilo a horas, minutos y segundos usando // y % (sin usar el módulo 
time ni nada externo, solo aritmética). Mostrá el resultado como "2h 15m 42s".
"""

SECONDS_IN_HOUR = 3600
SECONDS_IN_MINUTE = 60

print("=== Cálculo de tiempo de backup ===")

total_size_gb = float(input("Tamaño total en GB: "))
transfer_speed = float(input("Velocidad de transferencia: "))

total_size_mb = total_size_gb * 1024
estimated_time = total_size_mb / transfer_speed
hours = estimated_time // SECONDS_IN_HOUR
remaining_seconds = estimated_time % SECONDS_IN_HOUR
minutes = remaining_seconds // SECONDS_IN_MINUTE
seconds = remaining_seconds % SECONDS_IN_MINUTE

print(f"\nTiempo estimado de copia: {hours:.0f}h {minutes:.0f}m {seconds:.0f}s")
