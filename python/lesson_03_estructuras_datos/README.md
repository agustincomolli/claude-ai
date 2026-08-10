# Lección 3 — Estructuras de datos: listas, tuplas, dicts, sets

## Objetivos

- Agrupar datos relacionados bajo un solo nombre, en vez de variables sueltas.
- Recorrer colecciones con `for`, combinando índice y valor cuando hace falta.
- Elegir la estructura correcta según el problema (orden, mutabilidad,
  duplicados, acceso por posición o por clave).

## Conceptos cubiertos

- **Listas (`list`)**: ordenadas, mutables, admiten duplicados. Acceso por
  índice (empieza en 0; índices negativos acceden desde el final).
  Métodos: `.append()`, `.insert()`, `.remove()`, `.pop()`, `del`.
  `len()`, `sum()`, `max()`, `min()`, `sorted()` (no modifica) vs. `.sort()`
  (modifica en el lugar). `enumerate()` para iterar con índice y valor.
  List comprehensions como forma "pythónica" de crear listas derivadas.
- **Tuplas (`tuple`)**: ordenadas, **inmutables**. Se usan para datos que
  conceptualmente no deberían cambiar (coordenadas, rangos fijos).
- **Diccionarios (`dict`)**: pares clave-valor, acceso por clave (no por
  posición). `.get(clave, default)` para acceso seguro. `.items()`,
  `.keys()`, `.values()` para iterar. `in` sobre un dict verifica claves.
  Resuelven la duplicación de lógica que se venía arrastrando desde el
  ejercicio 7 (Lección 1).
- **Sets (`set`)**: sin orden, sin duplicados. Útiles para eliminar
  duplicados y para operaciones de conjuntos: `&` (intersección), `|`
  (unión), `-` (diferencia) — muy aplicable a comparar rondas de diagnóstico
  de red.

## Ejercicios (15 a 19)

| # | Ejercicio | Tema |
|---|---|---|
| 15 | Comparador de presupuestos con diccionario | `dict`, `min()`/`max()` sobre `.values()` |
| 16 | Inventario de repuestos | Lista de diccionarios, formato tabular |
| 17 | Registro de diagnóstico de red sin duplicados | `set`, patrón de carga con centinela `"fin"` |
| 18 | Ficha de cliente con historial de reparaciones | Diccionario anidado (lista de dicts dentro de un dict), `enumerate()` |
| 19 | Comparador de rondas de ping (día 1 vs. día 2) | Operaciones de conjuntos (`&`, `-`) |

## Errores reales encontrados y lección aprendida

- **Ejercicio 15**: `is_first_cheaper` se recalculaba dentro de un `for`,
  quedando "contaminada" por la última coincidencia recorrida en vez de
  reflejar una pregunta puntual sobre un dato conocido. Lección: preguntas
  sobre un elemento específico se resuelven con acceso directo por clave
  (`dict["clave"]`), no iterando toda la colección; el `for` se reserva
  para preguntas que sí necesitan revisar todos los elementos.
- **Ejercicio 16 y 18**: requisito faltante (contador de stock bajo) y typo
  de clave (`"descripton"`) que luego generó un `KeyError` al corregirlo a
  medias en un solo lugar. Lección: cuando una clave/nombre aparece en
  varios lugares del código, hay que rastrear **todas** las apariciones al
  corregir, no solo la más visible — usar buscar y reemplazar del editor.
- Mezcla de idiomas en claves de diccionario (`"nombre"` + `"price"` en el
  mismo dict): no es un bug, pero genera fricción de mantenimiento.
  Lección: elegir un idioma para nombres/claves y mantenerlo en todo el
  proyecto.

## Buenas prácticas incorporadas

- Elegir la estructura de datos según sus propiedades (orden, mutabilidad,
  duplicados), no por costumbre.
- Diccionarios con nombres de clave consistentes en idioma y sin errores de
  tipeo — repasar antes de dar un ejercicio por terminado.
- Reconocer cuándo un bloque de carga repetido (dos rondas de ping, tres
  reparaciones) es candidato a convertirse en función — anticipo de la
  Lección 5.
