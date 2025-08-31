# Docs: Acceso a documentacion!
# fuck you

import os
import requests
from rich.console import Console
from rich.markdown import Markdown 

console = Console()
BASE = "https://raw.githubusercontent.com/slyxicpy/docsyx/main/"

def run(args):
    if args:
        explore(args[0].lstrip("/"))
        return
    banner = r"""
        ╔══════════════════════════════════════╗
        ║        DOCS Explorer by SminOs       ║
        ║         Repo: slyxicpy/docsyx        ║
        ╚══════════════════════════════════════╝
        𝐝𝐞𝐬𝐜: [cyan]𝙲𝚎𝚗𝚝𝚛𝚊𝚕 𝚍𝚘𝚌𝚞𝚖𝚎𝚗𝚝𝚊𝚌𝚒𝚘𝚗 𝙴𝚂, 𝙿𝚘𝚛𝚝 𝚂𝚖𝚒𝚗 𝙾𝚜[/cyan]"""
    console.print(f"{banner}")
    console.print("Typea [cyan]lista[/cyan] para ver listado, [cyan]help[/cyan] para ver ayuda y [red]exit[/red] para volver")
    while True:
        try:
            cmd = input("docs> ").strip()
        except (KeyboardInterrupt, EOFError):
            console.print("\nVolviendo...")
            break
        if not cmd:
            continue
        if cmd.lower() in ["exit", "quit", "salir", "hakai"]:
            console.print("Volviendo...")
            break
        if cmd.lower() in ["lista", "-lista"]:
            list_all()
            continue
        import os
        if cmd.lower() in ["clear", "clean", "cls"]:
            os.system("clear")
            continue
        if cmd.lower() in ["menu", "help", "ayuda"]:
            console.print(f"""
            [bold cyan]Uso:[/bold cyan] /python/scapy o /python
            [cyan]-lista[/cyan]   Muestra listado disponible
            [cyan]-help[/cyan]    Muestra este menu
            [cyan]-clear[/cyan]   Limpia
            [red]exit[/red]     Vuelve
            """)
            continue
        explore(cmd.lstrip("/"))
        
def list_root():
    """Lista solo la raíz del repo"""
    api_url = "https://api.github.com/repos/slyxicpy/docsyx/contents"
    r = requests.get(api_url)
    if r.status_code != 200:
        console.print("[red]No pude acceder al repo[/red]")
        return

    for item in r.json():
        if item["type"] == "dir":
            console.print(f"[cyan]{item['name']}[/cyan]")
        else:
            console.print(f"[blue]{item['name']}[/blue]")


def explore(path):
    """Explora un path: puede ser carpeta o archivo"""
    api_url = f"https://api.github.com/repos/slyxicpy/docsyx/contents/{path}"
    r = requests.get(api_url)

    # Caso: existe como carpeta
    if r.status_code == 200 and isinstance(r.json(), list):
        console.print(f"\n[bold magenta]/{path}[/bold magenta]\n")
        for item in r.json():
            if item["type"] == "dir":
                console.print(f"[cyan]{item['name']}/[/cyan]")
            else:
                name = item['name'].replace(".md", "").replace(".txt", "")
                console.print(f"[blue]{name}[/blue]")
        return
    
    for ext in [".md", ".txt"]:
        url = f"{BASE}{path}{ext}"
        rr = requests.get(url)
        if rr.status_code == 200:
            md = Markdown(rr.text)
            console.print(f"\n[bold cyan]/{path}[/bold cyan]\n")
            console.print(md)
            return

    console.print(f"[red]No encontre nada en '/{path}'[/red]")

def list_all():
    api_url = "https://api.github.com/repos/slyxicpy/docsyx/contents"
    r = requests.get(api_url)
    if r.status_code != 200:
        console.print("[red]No he podido acceder, comprueba wifi![/red]")
        return
    for folder in r.json():
        if folder["type"] == "dir":
            console.print(f"[cyan]{folder['name']}[/cyan]")

def show_doc(path: str):
    parts = path.split("/", 1)
    if len(parts) > 1:
        lang, topic = parts
        fetch_and_show(lang, topic)
        return
    topic = parts[0]
    console.print(f"[bold magenta]Consultando '{topic}' en general...[/bold magenta]")
    api_url = "https://api.github.com/repos/slyxicpy/docsyx/contents"
    r = requests.get(api_url)
    if r.status_code != 200:
        console.print("[red]No pude acceder, verifica red[/red]")
        return
    found = False
    for folder in r.json():
        if folder["type"] == "dir":
            sub_url = f"https://api.github.com/repos/slyxicpy/docsyx/contents/{folder['name']}"
            rr = requests.get(sub_url)
            if rr.status_code != 200:
                continue
            for f in rr.json():
                if f["name"].lower().startswith(topic.lower()):
                    name = f["name"].replace(".md", "").replace(".txt", "")
                    console.print(f"[cyan]{folder['name']}[/cyan] -> [blue]{name}[/blue]")
                    found = True
    if not found:
        console.print(f"[red]No he encontrado nada con '{topic}'[/red]")

def fetch_and_show(lang, topic):
    for ext in [".md", ".MD", ".txt"]:
        url = f"{BASE}{lang}/{topic}{ext}"
        r = requests.get(url)
        if r.status_code == 200:
            md = Markdown(r.text)
            console.print(f"[bold cyan]{lang}/{topic}[/bold cyan]\n")
            console.print(md)
            return
    console.print(f"[red]No he encontrado '{topic}' en {lang}[/red]")

if __name__ == "__main__":
    import sys
    run(sys.argv[1:])
