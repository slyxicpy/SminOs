import os

def run(args):
    philin = ".vrt_path"
    if os.path.exists(philin):
        with open(philin, "r") as f:
            vrt = f.read().strip()
    else:
        vrt = os.getcwd()
    niveles = 1
    if args:
        try:
            niveles = max(1, int(args[0]))
        except ValueError:
            print(f"bk: '{args[0]}' no es un numero valido!, usa numero para bajar de niveles!, ej: bk 1")
    for _ in range(niveles):
        vrt = os.path.normpath(os.path.join(vrt, ".."))
    if os.path.isdir(vrt):
        with open(philin, "w") as f:
            f.write(vrt)
        print("dir actual:", vrt)
    else:
        print("bk: no pude retroceder mas !")
