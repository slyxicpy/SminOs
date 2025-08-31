import os
import shutil

def run(args):
    try:
        with open(".vrt_path", "r") as f:
            vrt = f.read().strip()
    except FileNotFoundError:
        vrt = os.getcwd()

    if not args:
        print("Dime el nombre del archivo o carpeta!")
        return

    nombre = args[0]
    destino = os.path.join(vrt, nombre)

    if os.path.exists(destino):
        try:
            if os.path.isfile(destino):
                os.remove(destino)
                print(f"Archivo '{nombre}' eliminado!")
            elif os.path.isdir(destino):
                shutil.rmtree(destino)
                print(f"Carpeta '{nombre}' eliminada!")
            print("Directorio actual:", vrt)
            for item in os.listdir(vrt):
                print(f"  • {item}")
        except OSError as e:
            print(f"Error al eliminar: {e}")
    else:
        print(f"'{nombre}' no existe!")
