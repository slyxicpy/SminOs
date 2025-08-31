import os, shutil

def run(args):
    if len(args) < 2:
        print('mv: se requiere origen, nombre o destino.. o ambas')
        return
    philin = ".vrt_path"
    if os.path.exists(philin):
        with open(philin, "r") as f:
            vrt = f.read().strip()
    else:
        vrt = os.getcwd()
    origen = args[0]
    destino = args[1]
    if not os.path.isabs(origen):
        origen = os.path.join(vrt, origen)
    if not os.path.isabs(destino):
        destino = os.path.join(vrt, destino)
    origen = os.path.normpath(origen)
    destino = os.path.normpath(destino)
    if not os.path.exists(origen):
        print(f"mv : '{origen}' no existe!")
        return
    if os.path.isdir(destino):
        destino = os.path.join(destino, os.path.basename(origen))
    try:
        shutil.move(origen, destino)
        print(f"'{origen}' movido/renombrado a '{destino}'")
    except Exception as e:
        print(f"mv: error al mover/renombrar :( {e}")
