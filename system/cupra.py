import sys, os, random
from cryptography.fernet import Fernet
from termcolor import colored 

def xor_data(data: bytes, key: bytes) -> bytes:
    key_len = len(key)
    return bytes([b ^ key[i % key_len] for i, b in enumerate(data)])

def genkey(path="key.key"):
    key = Fernet.generate_key()
    with open(path, "wb") as f:
        f.write(key)
    print(colored(f"[Key generada: {path}]", "magenta"))

def readf(file_path):
    with open(file_path, "rb") as f:
        data = f.read()
    pad_len = random.randint(0, 16)
    data += os.urandom(pad_len)
    return data

def writef(file_path, data):
    with open(file_path, "wb") as f:
        f.write(data)

# Fnc Run by MinOs

def run(args):
    if not args:
        print(colored("Uso: crupa -enc|-dec <archivo> <clave> [--overwrite] [--out nombre] (genera clave con crupa genkey)", "magenta"))
        return
    if args[0].lower() == "genkey":
        genkey()
        return
    if len(args) < 3:
        print(colored("falta argumento!!!", "red"))
        return
    action = args[0].lower()
    file_path = args[1]
    key_path = args[2]
    overwrite = "--overwrite" in args
    out_index = args.index("--out")+1 if "--out" in args else None
    out_file_custom = args[out_index] if out_index else None
    if not os.path.exists(file_path):
        print(colored(f"error!: archivo '{file_path}' no encontrado!", "red"))
        return
    if not os.path.exists(key_path):
        print(colored(f"error!: clave '{key_path}' no encontrada!", "red"))
        return
    with open(key_path, "rb") as kf:
        key = kf.read()
    fernet = Fernet(key)
    if action == "-enc":
        data = readf(file_path)
        xored = xor_data(data, key)
        encrypted = fernet.encrypt(xored)
        out_file = out_file_custom if out_file_custom else file_path + ".enc"
        if overwrite:
            out_file = file_path
        writef(out_file, encrypted)
        print(colored(f"archivo encriptado!: {out_file}", "blue"))
    elif action == "-dec":
        with open(file_path, "rb") as f:
            encrypted_data = f.read()
        try:
            decrypted_xor = fernet.decrypt(encrypted_data)
            decrypted = xor_data(decrypted_xor, key)
        except:
            print(colored("error!: no se pudo desencriptar, la clave es correcta?", "red"))
            return
        out_file = out_file_custom if out_file_custom else file_path.replace(".enc", ".dec")
        if overwrite:
            out_file = file_path
        writef(out_file, decrypted)
        print(colored(f"archivo desencriptado con exito!!: {out_file}", "blue"))
    else:
        print(colored("accion invalida! use: '-enc' o '-dec'", "red"))

if __name__ == "__main__":
    run(sys.argv[1:])
