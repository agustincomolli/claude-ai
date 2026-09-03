# Guía de commits — Conventional Commits aplicado al curso

## 1. Por qué importa esto

Un commit no es solo "guardar cambios" — es **documentación**. Dentro de un
año, cuando necesites entender por qué cambió una línea específica, `git log`
va a ser la primera herramienta que uses. Un historial con mensajes claros y
un cambio lógico por commit convierte a Git en una bitácora útil; un
historial con mensajes vagos o commits que mezclan varias cosas lo convierte
en ruido.

## 2. El formato: Conventional Commits

```
tipo(alcance opcional): descripción breve en modo imperativo

Cuerpo opcional, explicando el POR QUÉ del cambio (no el qué —
eso ya lo dice el diff). Se usa cuando el motivo no es obvio.

Footer opcional (referencias a issues, breaking changes, etc.)
```

### Tipos más usados

| Tipo | Cuándo usarlo | Ejemplo |
|---|---|---|
| `feat` | Código nuevo: un ejercicio nuevo, una función nueva, una feature | `feat: agregar ejercicio 30 (recursividad)` |
| `fix` | Corrección de un bug en código ya existente | `fix: corregir lógica invertida en cálculo de vida útil de batería` |
| `refactor` | Reorganizar código sin cambiar su comportamiento | `refactor: extraer validación de costo a función reutilizable` |
| `docs` | Cambios solo en documentación (README, docstrings, comentarios) | `docs: actualizar README de lección 5` |
| `style` | Formato, espacios, nombres — sin cambio de lógica | `style: aplicar snake_case consistente en claves de diccionario` |
| `test` | Agregar o corregir tests (a partir del Bloque B) | `test: agregar casos límite para validar_stock` |
| `chore` | Tareas de mantenimiento que no tocan código de la app (`.gitignore`, dependencias) | `chore: actualizar .gitignore` |

### Reglas de estilo para la descripción

- **Modo imperativo**, como si le dieras una orden a alguien: "agregar", "corregir", "eliminar" — no "agregado", "agregando", "agregué".
- **Minúscula** al empezar (salvo nombres propios), **sin punto final**.
- **Concisa** — idealmente bajo 50-60 caracteres. Si necesitás explicar más, usá el cuerpo del mensaje (una línea en blanco después del título, y ahí desarrollás).
- **Un idioma, siempre el mismo** — para este curso, español, igual que tu código y tus docstrings.

### Ejemplos concretos, antes/después de lo que ya escribiste

```
❌ add: exercise 26
✅ feat: agregar ejercicio 26 (comparador de presupuestos con función)

❌ fix: names of files add: exercises 27 and 28
✅ (dos commits separados)
   fix: corregir nombres de archivos de ejercicios
   feat: agregar ejercicios 27 y 28

❌ add: coments
✅ docs: agregar comentarios explicativos al sistema de reparaciones
```

## 3. El problema que planteaste: "empiezo un ejercicio nuevo y encuentro un bug en uno viejo"

Esto pasa todo el tiempo en desarrollo real, no es un problema tuyo — es
parte del trabajo. La solución **no es** meter todo en un commit con dos
tipos (`fix: ... feat: ...`), porque eso rompe la regla de oro: **un commit,
un cambio lógico**. La solución es controlar **qué** le decís a Git que
guarde en cada commit, usando `git add` de forma selectiva en vez de
`git add .` a ciegas.

### Caso A — el bug corregido y el ejercicio nuevo están en archivos distintos

Es el caso más común en este curso (cada ejercicio es su propio archivo).
Acá es simple: agregás y commiteás cada archivo por separado.

```bash
# Encontraste y corregiste un bug en exercise_08.py mientras
# trabajabas en exercise_30.py (todavía sin terminar)

git status
# venís de: exercise_08.py modificado, exercise_30.py nuevo

git add lesson_01_fundamentos/exercise_08.py
git commit -m "fix: corregir cálculo de vida útil restante en ejercicio 8"

# seguís trabajando en exercise_30.py, lo terminás, y recién ahí:
git add lesson_06_recursividad/exercise_30.py
git commit -m "feat: agregar ejercicio 30 (recursividad)"
```

`git add <ruta_específica>` le dice a Git "preparar solo este archivo para
el próximo commit", ignorando cualquier otro cambio pendiente en la carpeta.
Es la clave de todo este flujo.

### Caso B — el bug y el trabajo nuevo están en el mismo archivo

Más difícil, pero Git tiene una herramienta pensada exactamente para esto:
`git add -p` (de *patch*), que te deja elegir, **fragmento por fragmento**
(*hunk*) dentro de un mismo archivo, qué partes del cambio incluir en el
commit actual.

```bash
git add -p exercise_15.py
```

Git te va a mostrar cada bloque de cambios, uno por uno, y preguntarte qué
hacer con ese fragmento específico:

```
Stage this hunk [y,n,q,a,d,s,e,?]?
```

Las respuestas más usadas:
- `y` — sí, incluir este fragmento en el commit.
- `n` — no, dejarlo afuera (por ahora).
- `s` — dividir el fragmento en partes más chicas (si el cambio es muy grande y mezcla cosas).
- `q` — salir, dejando como estaba lo que no revisaste todavía.

Vas marcando `y` solo en los fragmentos que corresponden a la corrección del
bug, y `n` en los que son el trabajo nuevo del ejercicio. Al terminar,
`git commit -m "fix: ..."` va a incluir **solo** lo que marcaste con `y`. Lo
que dejaste afuera sigue ahí, sin confirmar, esperando el próximo commit.

### Caso C — alternativa más simple si `git add -p` te resulta confuso al principio

Podés lograr el mismo resultado "poniendo en pausa" el trabajo nuevo con
`git stash` (que guarda los cambios sin confirmarlos, aparte, y te devuelve
a un estado limpio), corrigiendo y commiteando el bug tranquilo, y después
retomando:

```bash
git stash                     # "guarda aparte" todos los cambios sin confirmar
# ahora tu carpeta está como en el último commit

# corregís el bug tranquilo, sin la mezcla
git add exercise_15.py
git commit -m "fix: corregir bug en comparador de presupuestos"

git stash pop                 # devuelve el trabajo nuevo que habías pausado
# seguís donde lo dejaste, sin el bug de antes
```

Esta opción es más fácil de razonar al principio porque no tenés que
decidir fragmento por fragmento — simplemente "escondés" el trabajo en
progreso, resolvés una cosa a la vez, y lo recuperás.

### Regla práctica para elegir entre A, B y C

- ¿Archivos distintos? → **Caso A**, el más simple, usalo siempre que puedas.
- ¿Mismo archivo, cambios en zonas claramente separadas? → **Caso B** (`git add -p`).
- ¿Mismo archivo, cambios entremezclados o te cuesta separarlos a simple vista? → **Caso C** (`git stash`).

## 4. Verificar antes de commitear

Antes de cualquier `git commit`, dos comandos que conviene tener de hábito:

```bash
git status      # qué está preparado (staged) y qué no
git diff --staged   # qué contenido EXACTO va a entrar en el próximo commit
```

`git diff --staged` te muestra línea por línea qué vas a confirmar — es la
forma de verificar, antes de escribir el mensaje, que efectivamente
preparaste solo lo que querías (por ejemplo, confirmar que el `fix` no se
llevó puesto código del ejercicio nuevo por error).

## 5. Resumen del flujo completo

```bash
git status                          # ver el panorama
git diff                            # revisar qué cambió, en detalle

# --- separar en commits lógicos ---
git add <archivo_del_fix>
git diff --staged                   # confirmar que es solo el fix
git commit -m "fix: descripción breve"

git add <archivo_del_feature>
git diff --staged                   # confirmar que es solo el feature
git commit -m "feat: descripción breve"

git push                            # subir ambos commits a GitHub
```

Un detalle final: no hace falta hacer `git push` después de cada commit
individual — podés acumular varios commits locales y subir todos juntos con
un solo `git push` cuando termines la sesión de trabajo. Lo importante es
que **cada commit, individualmente, represente un solo cambio lógico** —
eso es independiente de cuándo decidas sincronizar con GitHub.
