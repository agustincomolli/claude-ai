# Lección 1 — Fundamentos: entorno, variables, tipos y E/S

## Objetivos

- Configurar un entorno de trabajo profesional (entornos virtuales).
- Entender tipos de datos básicos y cuándo usar cada uno.
- Aplicar convenciones de nombres y estilo desde la primera línea (PEP 8).
- Manejar entrada/salida básica con `input()`/`print()` y f-strings.

## Conceptos cubiertos

- Tipado dinámico: `str`, `int`, `float`, `bool`.
- Convenciones de nombres (`snake_case`, nombres descriptivos).
- `input()` siempre devuelve `str` — conversión explícita de tipos.
- f-strings y formato numérico (`:.2f`, alineación con `:>`, `:^`, `:<`).
- Operadores aritméticos, de comparación y lógicos (`and`, `or`, `not`).
- **Evaluación de cortocircuito**: `and`/`or` en Python no siempre devuelven
  `bool` — devuelven uno de los dos operandos evaluados. Base del patrón
  `condición and valor` (útil pero ambiguo en tipo; se resuelve mejor con el
  operador ternario, visto en la Lección 2).

## Ejercicios (1 a 9)

| # | Ejercicio | Tema |
|---|---|---|
| 1 | Ficha rápida de equipo | Variables, tipos, f-strings |
| 2 | Cálculo de presupuesto | Operadores + patrón `and`/`or` como valor |
| 3 | Conversión de unidades (RAM) | `//`, `%` |
| 4 | Comparador de dos presupuestos | Operadores lógicos combinados |
| 5 | Diagnóstico de temperatura de CPU | Porcentajes, formato |
| 6 | Cálculo de tiempo de backup | `//`/`%` encadenados, constantes con nombre |
| 7 | Comparación de tres presupuestos | Lógica booleana compleja sin `if` |
| 8 | Vida útil de batería | Cuidado con "consumido" vs. "restante" |
| 9 | Cotización con recargo/descuento | Patrón `condición and valor` aplicado dos veces |

## Errores reales encontrados y lección aprendida

- **Ejercicio 8**: lógica invertida — `porcentaje_consumido < 15` en vez de
  `porcentaje_restante < 15`. Bug silencioso, sin excepción, respuesta
  incorrecta con total confianza. Lección: siempre probar con valores
  "reales" de uso (no solo el primer número que se ocurre) y con casos límite.
- **Ejercicio 9**: `costo_final` sumaba el descuento en vez de restarlo.
  Lección: revisar el signo de cada operación contra el enunciado, no dar
  por sentado el signo "porque suena bien".

## Buenas prácticas incorporadas

- Un entorno virtual por curso, activado antes de trabajar.
- Nombres de variable en `snake_case`, descriptivos y en el idioma correcto
  (cuidado con falsos amigos como *trademark* vs. *brand*).
- Constantes con nombre semánticamente correcto (`SECONDS_IN_MINUTE` ≠
  `MINUTES_IN_HOUR`, aunque numéricamente coincidan).
