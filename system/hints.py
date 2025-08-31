# Hints: tips for programmers!

import random, sys, time

COLORS = [
    "\033[96m",
    "\033[94m",
    "\033[34m",
    "\033[37m"
    ]

RESET = "\033[0m"

def run(args):
    hints = [
        "Python: Usa enumerate() en lugar de range(len()) para recorrer listas más limpio.",
        "Bash: Usa !! para repetir el último comando ejecutado.",
        "Git: Haz commits pequeños y descriptivos para facilitar el debug.",
        "Seguridad: Nunca subas tokens o contraseñas a GitHub, usa archivos .env.",
        "JavaScript: Usa === en lugar de == para evitar comparaciones inesperadas.",
        "CSS: Usa variables (:root { --color: red; }) para mantener tu estilo ordenado.",
        "Linux: htop es mejor que top, más claro y visual.",
        "Linux: Usa alias en tu .bashrc para ahorrar tiempo.",
        "Productividad: Aprende atajos de teclado en tu editor.",
        "Python: f-strings son más rápidos y legibles que format() o concatenaciones.",
        "Git: Usa ramas (branch) para cada feature, evita romper main.",
        "GitHub: README bien hecho da más confianza a tu repo.",
        "Consejo: Comenta tu código pensando en tu yo del futuro.",
        "C: Ten cuidado con los punteros, un error y todo se rompe.",
        "Rust: Confía en el compilador, suele tener la razón.",
        "Seguridad: Valida siempre la entrada del usuario.",
        "Python: Usa list comprehensions, más cortas y rápidas.",
        "Ruby: Todo es un objeto, incluso los números.",
        "JavaScript: Usa console.table() para imprimir arrays de objetos.",
        "Linux: Usa grep -r 'texto' . para buscar en todos los archivos.",
        "Python: Usa pathlib en lugar de os.path, es más moderno.",
        "Consejo: Leer documentación ahorra horas de sufrimiento.",
        "Seguridad: Hashea contraseñas, nunca las guardes en texto plano.",
        "Git: Usa git stash para guardar cambios sin hacer commit.",
        "General: Escribe código como si lo fuera a mantener otra persona.",
        "Productividad: Divide tareas grandes en tareas pequeñas.",
        "Debug: Print ayuda, pero un buen debugger es mejor.",
        "Python: Aprende pipx para gestionar paquetes de forma aislada.",
        "General: Automatizar pequeñas tareas te ahorra tiempo.",
    ]
    hint = random.choice(hints)
    color = random.choice(COLORS)
    for letra in hint:
          sys.stdout.write(color + letra + RESET)
          sys.stdout.flush()
          time.sleep(random.uniform(0.03, 0.07))
    print("\n")
