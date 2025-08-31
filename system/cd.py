import os

def run(args):
    vrt_file = ".vrt_path"
    if os.path.exists(vrt_file):
        with open(vrt_file, "r") as f:
            vrt = f.read().strip()
    else:
        vrt = os.path.join(os.getcwd(), "os")
    if not args:
        destino = vrt
    else:
        ruta = args[0]
        if os.path.isabs(ruta):
            destino = ruta
        else:
            destino = os.path.join(vrt, ruta)
    destino = os.path.normpath(destino)
    if os.path.isdir(destino):
        with open(vrt_file, "w") as f:
            f.write(destino)
        print("Dir actual:", destino)
    else:
        print(f"cd: '{destino}' no es un directorio valido!!@")

