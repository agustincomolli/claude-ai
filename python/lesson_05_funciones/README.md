# Lección 5 — Funciones: `def`, parámetros, retorno, scope

## Objetivos

- Reemplazar bloques de código duplicados (arrastrados desde la Lección 1)
  por funciones reutilizables, con datos distintos en cada llamada.
- Entender la diferencia entre `return` (devolver un valor utilizable) y
  `print()` (solo mostrar en pantalla).
- Entender el alcance (*scope*) de las variables dentro y fuera de una
  función, y por qué una función no debe depender de variables globales
  para funcionar correctamente.

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
  existe fuera de ella, y viceversa — una función no debe depender de
  nombres definidos en el programa principal. El curso evita
  deliberadamente `global`: una función recibe todo lo que necesita por
  parámetro y devuelve el resultado con `return`.
- Composición de funciones (una función puede llamar a otra).
- Docstrings Google-style como documentación mínima de una función (una
  línea por parámetro en `Args:`; se profundiza en el módulo de
  documentación, Bloque B).

## Ejercicios (25 a 29)

| # | Ejercicio | Tema |
|---|---|---|
| 25 | Función de validación reutilizable (retoma ej. 21) | Función con `return`, patrón `while`/`try`/`except`/`raise` encapsulado |
| 26 | Comparador de presupuestos con función (retoma ej. 15) | Función que devuelve múltiples valores |
| 27 | Clasificador de tickets con funciones (retoma ej. 12) | Separación cálculo (`return`) vs. presentación (`print`) |
| 28 | Carga de reparaciones con función (retoma ej. 24) | Función que construye y devuelve un diccionario, llamada dentro de un `for` |
| 29 | Diagnóstico de red con funciones (retoma ej. 19) | Eliminación de bloques duplicados de carga, función con tupla de retorno |

## Errores reales encontrados y lección aprendida

- **Ejercicio 26**: dentro de la función, el cálculo final usaba nombres de
  variable (`most_cheaper`, `most_expensive`) distintos a los definidos
  localmente (`budget_most_cheaper`, `budget_most_expensive`) — Python no
  las encontró en ningún scope disponible en ese momento y el programa
  terminó con `NameError`. Lección: dentro de una función, usar siempre
  los nombres que la propia función definió (parámetros y variables
  locales), nunca asumir que va a "encontrar" algo del programa principal.
- **Ejercicio 27**: la función usaba variables globales (`problem_type`,
  `IS_ENTERPRISE`) en dos de sus tres condiciones, en vez de los parámetros
  que ella misma declaraba (`description`, `is_company`). No generó error
  porque esas variables sí existían en el scope global al momento de la
  llamada — pero el comportamiento fue accidental, no correcto: la función
  dejó de ser reutilizable de forma confiable, y de paso reintrodujo el bug
  de mayúsculas/minúsculas que ya se había resuelto en la Lección 2 (una
  de las condiciones comparaba texto sin `.lower()`). Lección central del
  módulo: una función bien diseñada depende únicamente de sus parámetros
  y devuelve todo por `return` — nunca debe apoyarse en que existan
  variables con nombres específicos fuera de ella.

## Buenas prácticas incorporadas

- Dar nombre de verbo + objeto a las funciones (`calcular_total`,
  `validar_stock`, no `total_calculo`), reflejando que una función *hace*
  algo.
- Separar funciones que **calculan y devuelven** de funciones que
  **muestran** — misma responsabilidad única aplicada a diseño de
  funciones (ej. 27: `classify_priority()` vs. `show_results()`).
- Evitar `global`: preferir pasar datos por parámetro y devolver resultados
  — verificado explícitamente en los ejercicios 26 y 27 tras encontrar los
  bugs de scope.
- Funciones autocontenidas y reutilizables (ej. 28 y 29): todo lo que
  necesitan entra por parámetro, nada depende del contexto externo en el
  que se las llame.

## Cierre de Bloque A

Con esta lección se completa el **Bloque A — Bases sólidas y profesionales**
(fundamentos, control de flujo, estructuras de datos, manejo de errores y
funciones). Corresponde el primer **proyecto integrador** del curso antes
de avanzar al Bloque B (logging, testing, documentación).