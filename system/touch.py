import os

def run(args):
    try:
        with open(".vrt_path", "r") as f:
            vrt = f.read().strip()
    except FileNotFoundError:
        vrt = os.getcwd()
    if not args:
        print("Dime el nombre del archivo!")
        return
    nombre_archivo = args[0]
    destino = os.path.join(vrt, nombre_archivo)
    if not os.path.exists(destino):
        try:
            with open(destino, "w") as f:
                pass  # Archivo vacío
            print(f"Archivo '{nombre_archivo}' creado!")
        except OSError as e:
            print(f"Error al crear el archivo: {e}")
    else:
        print(f"El archivo '{nombre_archivo}' ya existe!")
    try:
        print("Directorio actual:", vrt)
        for item in os.listdir(vrt):
            print(f"  • {item}")
    except OSError as e:
        print(f"Error al listar!!: {e}")
