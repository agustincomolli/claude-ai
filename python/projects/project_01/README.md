# Proyecto Integrador 1 — Sistema de Gestión de Tickets de Reparación

## Contexto

Primer proyecto integrador del curso, cierre del **Bloque A — Bases sólidas
y profesionales**. Versión en consola, simplificada, de un sistema con menú
interactivo para cargar, consultar y gestionar tickets de reparación de
equipos — conceptualmente emparentado con la PWA "Control de Reparaciones"
ya existente, pero resuelto únicamente con los conceptos vistos hasta la
Lección 5 (sin archivos, sin clases, sin librerías externas — todo en
memoria mientras el programa corre).

## Alcance funcional

Menú principal en bucle, con 6 opciones:

1. **Cargar nueva reparación** — nombre de cliente, equipo, descripción y
   costo estimado (validado, mayor a 0). Cada reparación recibe un ID
   numérico autoincremental y arranca en estado `"pendiente"`.
2. **Listar todas las reparaciones** — tabla con formato de anchos fijos;
   mensaje claro si no hay datos cargados.
3. **Buscar reparaciones por cliente** — búsqueda parcial de texto,
   normalizada a minúsculas; mensaje claro si no hay coincidencias.
4. **Marcar reparación como entregada** — por ID; maneja con elegancia el
   caso de un ID inexistente.
5. **Ver estadísticas** — total de reparaciones, pendientes vs. entregadas,
   costo total acumulado y costo promedio; evita división por cero si no
   hay datos.
6. **Salir**.

## Diseño técnico

- Estructura central: diccionario de diccionarios (`reparations`), indexado
  por ID como string.
- Separación en capas: funciones de validación/utilidad
  (`input_choice`, `input_cost`), lógica de negocio (`new_repair`,
  `find_reparations`, `update_reparation_status`, `view_statistics`) y
  presentación (`print_header`, `print_repairs`, `show_menu`).
- Todas las funciones de lógica de negocio reciben la estructura de datos
  **por parámetro** — ninguna depende de variables globales.
- Validación robusta con el patrón `while`/`try`/`except`/`raise` tanto
  para el costo de una reparación como para la opción del menú.

## Errores reales encontrados durante el desarrollo y lección aprendida

- **Dependencia de variables globales**: las primeras versiones de
  `find_reparations()`, `update_reparation_status()` y `view_statistics()`
  accedían directamente a la variable global `reparations` en vez de
  recibirla como parámetro. No generaba ningún error (la variable sí
  existía en el momento de la llamada), pero rompía la reutilización y
  testeabilidad de las funciones — mismo problema de fondo que los bugs de
  *scope* de la Lección 5, aplicado a un programa real.
- **`TypeError` al desempaquetar un resultado `None`**: al corregir la
  dependencia global de `update_reparation_status()`, la función quedó con
  dos caminos de retorno de distinta "forma" (`return clave, valor` vs. un
  `return` implícito de `None` en el `except`). El código que llamaba a la
  función intentaba desempaquetar el resultado en una tupla de dos
  variables sin verificar antes si había recibido `None`, causando
  `TypeError: cannot unpack non-iterable NoneType object` — un bug que solo
  aparecía al ingresar un ID inexistente. Se resolvió unificando la forma
  de retorno de la función (`return None, None` en el caso de error) para
  que el desempaquetado nunca falle.
- **Chequeo de `None` con `if variable:` en vez de `if variable is not
  None:`**: al validar si `update_reparation_status()` había encontrado la
  reparación, se usó `if reparation_key:` — que evalúa el string como
  booleano en vez de comparar explícitamente contra `None`. Funcionaba
  únicamente porque, en el diseño actual, los IDs nunca son `"0"` (string
  "falsy"); un cambio futuro en el esquema de IDs podría haber roto esta
  condición de forma silenciosa. Se corrigió a `is not None`, que expresa
  la pregunta real ("¿existe la clave?") en vez de depender de una
  coincidencia de los datos actuales.
- **Mutabilidad de diccionarios**: se identificó que reasignar
  `reparations[clave] = valor` después de modificar un diccionario obtenido
  por referencia (`reparation = data[clave]`) es redundante, porque los
  diccionarios son mutables y la modificación ya es visible fuera de la
  función sin necesidad de reasignación explícita — concepto adelantado
  para profundizar más adelante en el curso.

## Estado

✅ Completo y revisado. Cierra el Bloque A.
