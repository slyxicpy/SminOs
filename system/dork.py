import os
import requests
from rich.console import Console 
from rich.markdown import Markdown 

console = Console()
BASE = "https://raw.githubusercontent.com/slyxicpy/dorkis/main/"

def run(args):
    banner = r"""
        ╔══════════════════════════════════════╗
        ║             DORKS BLYXS              ║
        ╚══════════════════════════════════════╝
        𝐝𝐞𝐬𝐜: [cyan]𝙲𝚎𝚗𝚝𝚛𝚊𝚕 𝚍𝚋 𝚍𝚎 𝚍𝚘𝚛𝚔𝚜 𝙱𝚢 𝙼𝚒𝚗𝙾𝚜 𝙲𝚘𝚗𝚎𝚌𝚝𝚒𝚘𝚗~[/cyan]"""
    console.print(f"{banner}")
    console.print(f"Typea [cyan] lista[/cyan] para ver categorias diponibles!,[cyan] help[/cyan] para ayuda y [red]exit[/red] para volver!\n")
    while True:
        try:
            cmd = input("dork> ").strip()
        except (KeyboardInterrupt, EOFError):
            console.print("\nVolviendo..")
            break
        if not cmd:
            continue
        if cmd.lower() in ["exit", "salir", "quit", "hakai"]:
            console.print("Volviendo...")
            break
        if cmd.lower() in ["-lista", "lista"]:
            listar_carpetas()
            continue
        if cmd.lower() in ["-clear", "clear"]:
            os.system("clear")
            continue
        if cmd.lower() in ["-help", "help", "menu"]:
            console.print(f"[bold cyan]              --- Central Dorks Bylx ---[/bold cyan]")
            console.print(f"""
            [bold cyan]Uso:[/bold cyan] /combos/dork o /db
            [cyan]-lista[/cyan]   Muestra listado disponible
            [cyan]-help[/cyan]    Muestra este menu
            [cyan]-clear[/cyan]   Limpia
            [red]exit[/red]     Vuelve
            """)
            continue
        if cmd.startswith("/"):
            manejar_path(cmd[1:])
            continue
        console.print("[red]Comando no reconocido[/red][cyan]Uso: /combos o /combos/dork.md")

def listar_carpetas(path=""):
    url = f"https://api.github.com/repos/slyxicpy/dorkis/contents/{path}"
    r = requests.get(url)
    if r.status_code != 200:
        console.print(f"[red]No pude acceder a {path or '/'}[/red]")
        return
    console.print(f"[bold cyan]Contenido dispo: {path or ''}[/bold cyan]")
    for f in r.json():
        if f["type"] == "dir":
            console.print(f"[cyan]{f['name']}[/cyan]/")

def manejar_path(path):
    url = f"https://api.github.com/repos/slyxicpy/dorkis/contents/{path}"
    r = requests.get(url)
    if r.status_code != 200:
        console.print(f"[red]No pude acceder a /{path}[/red]")
        return
    data = r.json()
    if isinstance(data, dict) and data.get("type") == "file":
        mostrar_archivo(path)
    elif isinstance(data, list):
        console.print(f"[bold cyan]/{path}[/bold cyan]\n")
        for f in data:
            if f["type"] == "file" and f["name"].endswith((".md", ".txt")):
                console.print(f"[green]{f['name']}[/green]")
            elif f["type"] == "dir":
                console.print(f"[blue]{f['path']}[/blue]")

def mostrar_archivo(path):
    for ext in ["", ".md", ".txt"]:
        url = f"{BASE}{path}{ext}"
        r = requests.get(url)
        if r.status_code == 200:
            console.print(f"[bold cyan]/{path}{ext}[/bold cyan]\n")
            if ext == ".md":
                md = Markdown(r.text)
                console.print(md)
            else:
                console.print(r.text)
            return
    console.print(f"[red]No encontre /{path}[/red]")

if __name__ == "__main__":
    run()

