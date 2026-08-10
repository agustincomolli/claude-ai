# Lección 5 — Funciones: `def`, parámetros, retorno, scope

> 🔄 Lección en curso.

## Objetivos

- Reemplazar bloques de código duplicados (arrastrados desde la Lección 1)
  por funciones reutilizables, con datos distintos en cada llamada.
- Entender la diferencia entre `return` (devolver un valor utilizable) y
  `print()` (solo mostrar en pantalla).
- Entender el alcance (*scope*) de las variables dentro y fuera de una
  función.

## Conceptos cubiertos

- `def nombre(parámetros):` — definir una función no la ejecuta; se ejecuta
  al llamarla.
- Parámetros y argumentos; argumentos posicionales vs. nombrados
  (*keyword arguments*).
- `return`: entrega un valor a quien llamó la función, corta la ejecución
  inmediatamente (igual que `break` en un bucle). Sin `return` explícito,
  la función devuelve `None`.
- Parámetros con valor por defecto (`def f(a, b=5):`) — deben ir después de
  los parámetros sin valor por defecto.
- Scope local vs. global: una variable creada dentro de una función no
  existe fuera de ella. Se puede **leer** una variable global desde una
  función, pero el curso evita deliberadamente `global` para modificarlas
  — en su lugar, la función recibe parámetros y devuelve el resultado con
  `return`.
- Composición de funciones (una función puede llamar a otra).
- Docstrings como documentación mínima de una función (se profundiza en el
  módulo de documentación, Bloque B).

## Ejercicios (25 a 29)

| # | Ejercicio | Tema | Estado |
|---|---|---|---|
| 25 | Función de validación reutilizable (retoma ej. 21) | Función con `return`, patrón `while`/`try`/`except`/`raise` encapsulado | 🔄 |
| 26 | Comparador de presupuestos con función (retoma ej. 15) | Función que devuelve múltiples valores | ⏳ |
| 27 | Clasificador de tickets con funciones (retoma ej. 12) | Separación cálculo (`return`) vs. presentación (`print`) | ⏳ |
| 28 | Carga de reparaciones con función (retoma ej. 24) | Función que construye y devuelve un diccionario, llamada dentro de un `for` | ⏳ |
| 29 | Diagnóstico de red con funciones (retoma ej. 19) | Eliminación de bloques duplicados de carga, función con tupla de retorno | ⏳ |

_(Esta tabla se actualiza a medida que se revisan los ejercicios.)_

## Errores reales encontrados y lección aprendida

_(pendiente de completar cuando se revisen los ejercicios 25 a 29)_

## Buenas prácticas incorporadas

- Dar nombre de verbo/frase verbal a las funciones (`calcular_...`,
  `validar_...`, `mostrar_...`), reflejando que una función *hace* algo.
- Separar funciones que **calculan y devuelven** de funciones que
  **muestran** — misma responsabilidad única aplicada a diseño de funciones.
- Evitar `global`: preferir pasar datos por parámetro y devolver resultados.
