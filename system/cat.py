import os

def run(args):
    if not args:
        print("Typea: cat <archivo>")
        return
    vrt_file = ".vrt_path"
    if os.path.exists(vrt_file):
        with open(vrt_file, "r") as f:
            vrt = f.read().strip()
    else:
        vrt = os.path.join(os.getcwd(), "os")
    archivo = args[0]
    if os.path.isabs(archivo):
        destino = archivo
    else:
        destino = os.path.join(vrt, archivo)
    destino = os.path.normpath(destino)
    if not os.path.exists(destino):
        print(f"el archivo '{archivo}' no existe!")
        return
    try:
        with open(destino, "r", encoding="utf-8") as f:
            print(f.read())
    except Exception as e:
        print(f"Error al leer!! '{archivo}': {e}")

