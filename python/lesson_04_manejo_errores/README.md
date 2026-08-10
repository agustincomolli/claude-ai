# Lección 4 — Manejo de errores: `try`/`except`, `raise`

## Objetivos

- Evitar que el programa se caiga ante un input inesperado del usuario.
- Distinguir errores de conversión de tipo (`ValueError`) de otros errores
  específicos (`ZeroDivisionError`, `KeyError`, etc.).
- Lanzar excepciones propias con `raise` cuando un valor es técnicamente
  válido pero no tiene sentido para las reglas del programa.

## Conceptos cubiertos

- Modelo de excepciones: un error interrumpe el flujo normal y "sube"
  buscando quién lo maneje; si nadie lo maneja, el programa termina.
- `try`/`except`: si una línea del `try` falla, el resto del bloque `try`
  se corta inmediatamente y salta al `except` correspondiente.
- Excepciones específicas vs. `except:` genérico — un `except` genérico
  esconde bugs propios además de errores esperables del usuario. Regla:
  capturar siempre el tipo más específico posible.
- Tabla de excepciones comunes: `ValueError`, `ZeroDivisionError`,
  `KeyError`, `IndexError`, `TypeError`, `FileNotFoundError`.
- Capturar varios tipos a la vez: `except (ValueError, TypeError):`.
- `as error` para acceder al mensaje de la excepción.
- `else` (se ejecuta solo si el `try` no falló) y `finally` (se ejecuta
  siempre, haya habido error o no).
- Patrón central del módulo: `while True` + `try`/`except` + `break` para
  validar input hasta que sea válido — más robusto que el patrón de
  "valor centinela" usado en la Lección 2, porque cubre el error de
  conversión en sí mismo, no solo valores fuera de rango.
- `raise` para lanzar excepciones propias cuando el dato es del tipo
  correcto pero no cumple una regla de negocio (stock negativo, costo
  igual a cero, etc.).

## Ejercicios (20 a 24)

| # | Ejercicio | Tema |
|---|---|---|
| 20 | Ficha de equipo robusta (retoma ej. 1) | `while` + `try`/`except ValueError` |
| 21 | Calculadora de presupuesto con validación completa (retoma ej. 2) | Validación doble + `raise` para rechazar negativos |
| 22 | Divisor de gastos entre técnicos | `ZeroDivisionError` manejado por separado de la validación de tipo |
| 23 | Consulta segura de inventario (retoma ej. 16) | `except KeyError` sobre acceso a diccionario |
| 24 | Sistema de carga de reparaciones con validación total (retoma ej. 18) | Reintento de un ítem puntual sin perder los ya cargados |

## Errores reales encontrados y lección aprendida

- **Ejercicio 21**: `surcharge = subtotal > 50000` calculaba un `bool`, no
  el 5% del subtotal — bug silencioso (Python trata `True` como `1` en
  sumas), reaparición del mismo problema visto en la Lección 1 con el
  patrón `and`/`or`. Lección: una variable booleana ("¿corresponde
  recargo?") y el valor monetario resultante son dos cosas distintas —
  separarlas explícitamente.
- **Ejercicio 24**: al intentar diferenciar mensajes de error con
  `if str(error)`, faltó el prefijo `f` en el f-string (`"ERROR:
  {error}"` en vez de `f"ERROR: {error}"`), y la condición elegida nunca
  se cumplía en la práctica. Lección: una mejora "extra" no probada con
  cuidado puede introducir un bug nuevo sobre código que ya funcionaba;
  probar siempre after cualquier cambio, por menor que parezca.

## Buenas prácticas incorporadas

- Separar el bloque de validación (`try`/`except` de conversión) del
  cálculo posterior, salvo que ambos formen parte del mismo paso lógico
  (como en el ejercicio 23).
- Usar `raise` con mensaje descriptivo para reglas de negocio, no solo
  para errores de tipo.
- Permitir reintentar un ítem puntual de una carga en lote sin perder el
  trabajo ya válido.
