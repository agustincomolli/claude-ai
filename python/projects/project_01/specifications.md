# Sistema de Gestión de Tickets de Reparación
Proyecto Integrador 1 —  (consola)
## Contexto

Vas a construir una versión en consola, simplificada, de algo conceptualmente parecido a tu "Control de Reparaciones" (la PWA que ya tenés en producción) — un sistema con menú interactivo para cargar, consultar y gestionar tickets de reparación de equipos. Es la primera vez en el curso que vas a integrar todo el Bloque A en un solo programa con estructura real, no un ejercicio de una sola pantalla.

**Restricción de conceptos**: solo lo visto en las Lecciones 1 a 5 (variables, tipos, operadores, `if`/`elif`/`else`, `while`, `for`, listas, tuplas, dicts, sets, `try`/`except`/`raise`, funciones con return). Nada de archivos, clases, ni librerías externas — eso llega en bloques posteriores. Los datos viven en memoria mientras el programa corre; al cerrar el programa, se pierden (es esperable y correcto en esta etapa).

## Requisitos funcionales

El programa tiene que mostrar un **menú principal** en un bucle que se repite hasta que el usuario elija salir:
```
=== SISTEMA DE GESTIÓN DE REPARACIONES ===
1. Cargar nueva reparación
2. Listar todas las reparaciones
3. Buscar reparaciones por cliente
4. Marcar reparación como entregada
5. Ver estadísticas
6. Salir

Seleccione una opción:
```
Cada opción tiene que estar resuelta con **una función propia** (nada de lógica de más de 2-3 líneas suelta en el bucle principal del menú — el `while` principal solo debería leer la opción y delegar a la función correspondiente).

### 1. Cargar nueva reparación
Pide: nombre del cliente, equipo (marca/modelo, texto libre), descripción del problema, y costo estimado. El costo tiene que validarse (número, mayor a 0) con el patrón `while`/`try/except`/`raise` que ya dominás. Cada reparación se guarda con un **ID numérico autoincremental** (empezá en 1 y sumá de a uno por cada carga) y un estado inicial `"pendiente"`. Guardá todo en una estructura central que sobreviva durante toda la ejecución del programa (pensalo bien: ¿lista de diccionarios? ¿diccionario de diccionarios, indexado por ID? Ambas son válidas, pero tienen distintas ventajas para las siguientes operaciones).

### 2. Listar todas las reparaciones
Muestra una tabla prolija (podés reusar tu criterio de formato con anchos fijos, como en ejercicios anteriores) con ID, cliente, equipo, estado y costo de **todas** las reparaciones cargadas. Si todavía no se cargó ninguna, mostrar un mensaje claro en vez de una tabla vacía rara.

### 3. Buscar reparaciones por cliente
Pide un nombre (o parte del nombre) y, usando el operador `in` sobre texto normalizado (¿te acordás por qué hay que normalizar?), mostrá todas las reparaciones que coincidan — puede haber más de una reparación por cliente. Si no hay coincidencias, avisar claramente.

### 4. Marcar reparación como entregada
Pide un ID de reparación y cambia su estado a `"entregada"`. Tiene que manejar con elegancia el caso de que el ID no exista (sin que el programa se rompa).

### 5. Ver estadísticas
Mostrá: cantidad total de reparaciones cargadas, cantidad pendientes vs. entregadas, el costo total acumulado de todas las reparaciones, y el costo promedio. Si no hay reparaciones cargadas, evitar una división por cero.

### 6. Salir
Corta el bucle principal con un mensaje de despedida.

## Requisitos técnicos (lo que quiero ver aplicado explícitamente)
- Como mínimo 5-6 funciones bien separadas por responsabilidad (una función, una tarea).
- Cada función con docstring Google-style.
- Al menos dos validaciones distintas con `try`/`except`/`raise` (costo al cargar, ID al marcar como entregada — pensá si ahí también aplica algún tipo de validación).
- Uso de al menos una lista y un diccionario (o diccionario de diccionarios) de forma central en el programa.
- El menú principal (`while True`) tiene que validar que la opción ingresada sea un número entre 1 y 6, con manejo de error si el usuario escribe algo no numérico o fuera de rango — sin que el programa se caiga ni entre en un estado raro.
- Nombres de variables, funciones y claves de diccionario consistentes y en el mismo idioma (ya sabés cuál es mi implacable insistencia con esto).
## Sugerencia de organización (no obligatoria, pero recomendada)

Pensalo en capas, de abajo hacia arriba:

- Funciones de **validación/utilidad** (ej: pedir un costo válido).
- Funciones de **lógica de negocio** (ej: cargar una reparación, buscar por cliente, calcular estadísticas) — estas trabajan sobre la estructura de datos central, que les llega **por parámetro**, no por variable global (acordate del ejercicio 27).
- Funciones de **presentación** (ej: mostrar la tabla, mostrar el menú) — separadas de las que calculan, mismo criterio que el ejercicio 27.
- El bucle principal del menú, que solo coordina: lee la opción, llama a la función que corresponde.

No hace falta que seas perfectamente ortodoxo con esto — es una guía, no una imposición — pero cuanto más lo respetes, más fácil te va a resultar cuando lo retomemos en el Bloque C (POO) y lo convirtamos en una clase.