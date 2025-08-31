import os

def run(args):
    try:
        with open(".vrt_path", "r") as f:
            vrt = f.read().strip()
    except FileNotFoundError:
        vrt = os.getcwd()
    nombre_dir = args[0] if args else "nuevo_dir"
    destino = os.path.join(vrt, nombre_dir)

    if not os.path.exists(destino):
        os.mkdir(destino)
        print("directorio creado!")
    else:
        print("el directorio ya existe!")
    try:
        print("Directorio actual:", vrt)
        for item in os.listdir(vrt):
            print(f"  • {item}")
    except OSError as e:
        print(f"Error al listar!: {e}")
