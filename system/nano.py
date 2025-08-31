import os, subprocess

def run(args):
    if not args:
        print("typea: nano<archivo!>")
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
    base_dir = os.path.dirname(os.path.abspath(__file__))
    nanorc = os.path.join(base_dir, "nano", ".nanorc")
    try:
        subprocess.run(["nano", "-c", "-r", "80", "--rcfile", nanorc, destino])
    except FileNotFoundError:
        print("error!: nano no esta instalado en sistema!!")
