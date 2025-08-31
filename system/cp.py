import os, shutil

def run(args):
    if len(args) < 2:
        print('cp: se requieren origen y destino')
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
        print(f"cp: '{origen}' no existe!")
        return
    try:
        if os.path.isdir(origen):
            shutil.copytree(origen, destino)
        else:
            shutil.copy2(origen, destino)
        print(f"'{origen}' copiado a '{destino}'")
    except FileExistsError:
        print(f"cp: '{destino}' ya existe!")
    except Exception as e:
        print(f"cp: error :( {e}")
            
