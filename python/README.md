# Curso de Python — Agustín Comolli

Curso personalizado de Python dictado por Claude en rol de profesor, orientado a
aplicar lo aprendido en herramientas reales de soporte técnico, sistemas y
gestión (municipal, clientes particulares y pequeñas empresas).

## Metodología

- Cada lección se explica en profundidad (no solo sintaxis, también el *porqué*
  de cada concepto) y se cierra con ejercicios de nivel intermedio/avanzado
  basados en escenarios reales de IT.
- Los ejercicios de una lección usan **únicamente** conceptos vistos en esa
  lección o en lecciones anteriores — nunca se adelanta contenido.
- Cada ejercicio se revisa con feedback detallado: bugs reales, buenas
  prácticas, legibilidad y mantenibilidad — no solo "funciona o no funciona".
- Al cerrar cada bloque temático se propone un **proyecto integrador**
  funcional y de uso cotidiano.

## Entorno de trabajo

Un único entorno virtual (`venv/`) compartido para todo el curso, en la raíz
del repositorio. Se activa así:

```bash
# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

`venv/` está excluido del control de versiones (ver `.gitignore`) — nunca se
sube a Git, se regenera localmente si hace falta.

## Estructura del repositorio

```
.
├── README.md                          ← este archivo
├── .gitignore
├── requirements.txt
├── venv/                              ← entorno virtual (ignorado por Git)
├── lesson_01_fundamentos/
├── lesson_02_control_flujo/
├── lesson_03_estructuras_datos/
├── lesson_04_manejo_errores/
├── lesson_05_funciones/
└── projects/                          ← proyectos integradores
```

## Progreso del curso

### Bloque A — Bases sólidas y profesionales ✅ Completo

| # | Lección | Estado |
|---|---|---|
| 1 | Fundamentos (variables, tipos, operadores, I/O) | ✅ Completa |
| 2 | Control de flujo (`if`/`elif`/`else`, `while`, `for`) | ✅ Completa |
| 3 | Estructuras de datos (listas, tuplas, dicts, sets) | ✅ Completa |
| 4 | Manejo de errores (`try`/`except`, `raise`) | ✅ Completa |
| 5 | Funciones (`def`, parámetros, retorno, scope) | ✅ Completa |

**Pendiente antes de avanzar al Bloque B:** proyecto integrador de cierre
del Bloque A, y `git init` del repositorio (primer commit).

### Próximos bloques

- **Bloque B** — Calidad de código profesional: logging, testing, documentación
- **Bloque C** — POO y arquitectura
- **Bloque D** — Persistencia e interacción con el mundo (archivos, SQLite, APIs)
- **Bloque E** — Interfaces (CLI avanzada, consola con `rich`/`textual`, GUI/web)
- **Bloque F** — Concurrencia y empaquetado

Git y GitHub se van a ir incorporando de forma progresiva como parte de las
buenas prácticas del curso, en paralelo a los bloques temáticos.

## Proyectos integradores

| Proyecto | Bloque | Estado |
|---|---|---|
| — | Bloque A | 🔄 Por definir |