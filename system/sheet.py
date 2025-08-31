# sheet: Sheets-wiki by Styx
#Actuales: python, js, c# c/++ ,go, rust, java, ASM, bash, linux(Scripting). (Proximamente mas)

import requests
from rich.console import Console 
from rich.markdown import Markdown 

console = Console()
BASE = 'https://raw.githubusercontent.com/slyxicpy/Sheet/main/'

def run(args):
    if args:
        show_cheat(args[0])
        return
    banner = r"""
⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠯⠓⠻⠈⢿⡇⢼⢧⢇⢻⡇⣿⣿⢸⣿⡟⣿⣿⣿╔═══════════════════════════════════╗
⣿⣿⣿⣿⣿⠟⢋⣥⡶⡲⡽⠃⠋⠀⠀⠀⠈⠈⠈⠜⠰⠹⠃⣿⣿⣻⣿⣿⣿║   煤 Cheats : ES                  ║
⣿⣿⣿⡟⢡⣴⣿⢮⠑⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠈⠃⠹⠳⢟⡾⢛║   衙 OWner  : Styx                ║
⣿⣿⠏⣴⣿⠿⠅⠁⠀⠀⠀⠀⠀⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣾║   浳 And    : Esp-lat             ║
⣿⢃⣾⡿⠀⠀⠀⢀⠀⢤⠀⠀⠀⢈⡇⠀⣿⣿⣿⣿⠆⠀⠀⠀⠠⣜⣿⣿⣿║   浤 Proxp  : 2Wkk2b              ║
⢏⣾⡿⠃⠀⣠⡀⢸⣆⠀⠀⠀⣠⣿⡟⢀⣿⣿⠟⠁⢀⠀⢚⣵⣾⣿⣿⣿⣿║   搰 Adict  : 𝓣𝓾𝓼𝓼𝓲               ║
⣾⡟⠁⣠⣾⣿⣷⣌⡀⠙⠟⠛⠙⠃⣠⣾⠟⠁⠀⠀⠠⣲⣭⣿⣟⣿⣿⣿⣿║   煤 Bitch  : 𝓨𝓸𝓾𝓻 𝓜𝓸𝓶            ║
⡟⢠⣾⡿⠿⠿⠿⠿⢿⣷⠶⠶⠞⠛⠉⠀⢀⢀⢀⢄⣚⣮⢿⣿⣿⣿⣿⣿⣿║   煵 Pruper : 𝓢𝓶𝓲𝓷-𝓞𝓢             ║
⣰⢟⣥⣶⣴⡲⣴⡔⣴⣤⡆⡄⢠⣄⠠⡰⣳⡵⢳⣳⣻⣿⣿⣿⣿⣿⣿⣿⣿║   嫠 Aplex  : 𝓢𝓮𝔁-𝓚𝓪𝓶𝓾𝓲           ║
⣿⣿⣿⣿⣿⣿⣿⣷⣿⣿⣧⣽⣧⣽⣀⣷⣿⣿⣿⣧⣿⣿⣿⣿⣿⣿⣿⣿⣿╚═══════════════════════════════════╝"""
    console.print(f"{banner}")
    console.print("Typea [cyan]help[/cyan] para ayuda o [red]exit[/red] para volver!\n")
    while True:
        try:
            cmd = input("sheet> ").strip()
        except (KeyboardInterrupt, EOFError):
            console.print("\nSaliendo de shett")
            break
        if not cmd:
            continue
        if cmd.lower() in ['exit', 'quit', 'salir', 'hakai']:
            console.print("Volviendo...")
            break
        if cmd.lower() in ["lista", "-lista", "all"]:
            list_all()
            continue
        import os
        if cmd.lower() in ["clear", "cls", "limpiar"]:
            os.system('clear')
            continue
        if cmd.lower() == "help":
            console.print("""[bold cyan]Uso: <lenguaje>/<tema> o <lenguaje>  Ejemplo: python/listas o python[/bold cyan]
            - [cyan]help[/cyan]   Muestra esta ayuda
            - [cyan]lista[/cyan]  Muestra listado disponible
            - [cyan]clear[/cyan]  Limpia pantalla
            - [red]exit[/red]   Vuelve""")
            continue
        show_cheat(cmd)

def show_cheat(path: str):
    parts = path.split("/", 1)
    if len(parts) > 1:
        lang, topic = parts
        fetch_and_show(lang, topic)
        return
    topic = parts[0]
    console.print(f"[bold magneta]Consultando '{topic}' en general!...[/bold magneta]\n")
    syx_url = "https://api.github.com/repos/slyxicpy/Sheet/contents"
    r = requests.get(syx_url)
    if r.status_code != 200:
        console.print("[red]No pude acceder![/red]")
        return
    found = False
    for folder in r.json():
        if folder.get("type") == "dir" and folder.get("name").lower() == topic.lower():
            lang = folder.get("name")
            api_url = f"https://api.github.com/repos/slyxicpy/Sheet/contents/{lang}"
            rr = requests.get(api_url)
            if rr.status_code != 200:
                continue
            for f in rr.json():
                if f["name"].endswith((".md", ".txt")):
                    name = f["name"].rsplit(".", 1)[0]
                    console.print(f"[cyan]{lang}[/cyan] -> [blue]{name}[/blue]")
                    found = True
    if not found:
        console.print(f"[red]No hay nada! nothing nothing con '{topic}'[/red]")

def list_all():
    api_url = "https://api.github.com/repos/slyxicpy/Sheet/contents"
    r = requests.get(api_url)
    if r.status_code != 200:
        console.print("[red]No he podido acceder, comprueba wifi![/red]")
        return
    for folder in r.json():
        if folder["type"] == "dir":
            console.print(f"[cyan]{folder['name']}[/cyan]")

def fetch_and_show(lang, topic):
    for ext in [".md", ".MD", ".txt"]:
        url = f"{BASE}{lang}/{topic}{ext}"
        r = requests.get(url)
        if r.status_code == 200:
            md = Markdown(r.text)
            console.print(f"[bold cyan]{lang}/{topic}[/bold cyan]\n")
            console.print(md)
            return
    console.print(f"[red]No encontre [bold]{lang}/{topic}[/bold][/red]")

if __name__ == "__main__":
    import sys
    run(sys.argv[1:])



            
