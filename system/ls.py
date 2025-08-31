import os

def run(args):
    try:
        with open(".vrt_path", "r") as f:
            vrt = f.read().strip()
    except FileNotFoundError:
        vrt = os.getcwd()
    print("Directorio actual:", vrt)
    try:
        for item in os.listdir(vrt):
            print(f"  • {item}")
    except OSError as e:
        print(f"Error al listar el directorio: {e}")
