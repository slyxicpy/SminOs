import base64, codecs, urllib.parse, sys, time, random

COLORS = [
    "\033[96m",
    "\033[91m",
    "\033[92m",
    "\033[93m",
]

RESET = "\033[0m"

def typeout(text, color="\033[96m"):
    for letra in text:
        sys.stdout.write(color + letra + RESET)
        sys.stdout.flush()
        time.sleep(random.uniform(0.02, 0.05))
    print("")

def encrypt(text, method):
    if method == "base64":
        return base64.b64encode(text.encode()).decode()
    elif method == "hex":
        return text.encode().hex()
    elif method == "rot13":
        return codecs.encode(text, "rot13")
    elif method == "url":
        return urllib.parse.quote(text)
    elif method == "bin":
        return " ".join(format(ord(c), "08b") for c in text)
    else:
        return None

def decrypt(text):
    try:
        return base64.b64decode(text).decode()
    except: pass
    try:
        return bytes.fromhex(text).decode()
    except: pass
    try:
        if any(c.isalpha() for c in text):
            return codecs.decode(text, "rot_13")
    except: pass
    try:
        decoded = urllib.parse.unquote(text)
        if decoded != text:
            return decoded
    except: pass
    try:
        if set(text.replace(" ", "")) <= {"0","1"}:
            return "".join(chr(int(b, 2)) for b in text.split())
    except: pass
    return None

def run(args):
    if not args or args[0] in ["-h", "--help"]:
        typeout("Uso: cryp -enc <metodo> <texto> | cryp -dec <texto>", random.choice(COLORS))
        typeout("Metodos disponibles: base64, hex, rot13, url, bin", random.choice(COLORS))
        return

    if args[0] == "-enc" and len(args) >= 3:
        method, text = args[1], " ".join(args[2:])
        res = encrypt(text, method)
        if res:
            typeout(f"[{method}] -> {res}", "\033[92m")
        else:
            typeout("no soportado!", "\033[91m")

    elif args[0] == "-dec" and len(args) >= 2:
        text = " ".join(args[1:])
        res = decrypt(text)
        if res:
            typeout(f"Deco -> {res}", "\033[92m")
        else:
            typeout("No se pudo detectar el tipo de encriptacion!, shit", "\033[91m")

    else:
        typeout("invalidos, usa -h para ayuda!", "\033[91m")
