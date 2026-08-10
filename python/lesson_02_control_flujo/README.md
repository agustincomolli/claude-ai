# Lección 2 — Control de flujo: `if`/`elif`/`else`, `while`, `for`

## Objetivos

- Tomar decisiones explícitas con `if`/`elif`/`else`, reemplazando el patrón
  `and`/`or` de la Lección 1 por algo legible y sin ambigüedad de tipos.
- Repetir código de forma controlada con `while` (condición) y `for` (rango
  conocido de antemano).
- Usar `break`/`continue` para controlar el flujo dentro de un bucle.
- Buscar texto dentro de strings con el operador `in` (y `not in`).

## Conceptos cubiertos

- Sintaxis de `if`/`elif`/`else`: indentación como sintaxis (no cosmética),
  orden de evaluación (Python ejecuta solo la primera condición verdadera).
- Operador ternario: `valor_si_true if condicion else valor_si_false` — forma
  explícita y segura en tipos de resolver lo que antes se hacía con
  `condición and valor`.
- Comparaciones encadenadas: `0 <= edad < 1`.
- Operador `in`/`not in` sobre strings — **sensible a mayúsculas/minúsculas**,
  siempre normalizar con `.lower()` antes de comparar texto de usuario.
- `while`: condición de corte, riesgo de bucle infinito si ninguna variable
  de la condición cambia dentro del bucle.
- `for` con `range(inicio, fin, paso)` — el límite superior nunca se incluye.
- Diferencia de uso: `while` cuando no se sabe de antemano cuántas
  repeticiones habrá; `for` cuando sí se sabe.
- `break` (corta el bucle por completo) vs. `continue` (salta solo la
  iteración actual).

## Ejercicios (10 a 14)

| # | Ejercicio | Tema |
|---|---|---|
| 10 | Reescritura del comparador de 3 presupuestos (ej. 7) | `if`/`elif`/`else` reemplazando lógica booleana encadenada |
| 11 | Validador de credenciales de acceso remoto | `while` + `break`, máximo de intentos |
| 12 | Clasificador de tickets por prioridad | `in` sobre texto normalizado |
| 13 | Diagnóstico de red (simulación de ping) | `for` + `range()`, validación de input dentro de un `while` interno |
| 14 | Calculadora de cuotas con validación | `while` de validación + `if`/`elif` + `for` de detalle |

## Errores reales encontrados y lección aprendida

- **Ejercicio 10**: en la refactorización con `if`, dos de las tres ramas de
  `is_in_range` usaban el porcentaje de referencia equivocado (`budget_1 *
  0.15` en vez de `budget_2`/`budget_3 * 0.15`). Lección: cuando se escriben
  varias ramas simétricas a mano, revisar cada una comparando línea por
  línea, no confiar en que "ya se corrigió una vez, debe estar bien en
  todos lados".
- **Ejercicio 12 y 13**: comparación de texto sin normalizar mayúsculas
  (`problem_type` sin `.lower()`, y `response` comparado contra la versión
  sin normalizar después de validarlo en minúscula). Lección: normalizar
  el texto de usuario **una sola vez**, apenas se captura, y trabajar
  siempre con esa versión — no mantener una "versión cruda" y una
  "normalizada" del mismo dato dando vueltas.

## Buenas prácticas incorporadas

- Aplanar la lógica con `elif` en vez de anidar `if` innecesariamente
  ("código en escalera").
- Normalizar texto de usuario (`.lower()`) inmediatamente al capturarlo.
- Detectar código duplicado con variación de datos (ramas casi idénticas)
  como señal de que el problema pide una función o una estructura de datos
  — anticipo de la Lección 5.
