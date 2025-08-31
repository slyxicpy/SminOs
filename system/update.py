import subprocess, os
from rich.console import Console 

console = Console()
REPO_DIR = os.path.dirname(os.path.abspath(__file__))

def run(args):
    try:
        result = subprocess.run(
            ["git", "pull", "origin", "main"],
            capture_output=True,
            cwd=REPO_DIR,
            text=True
        )
        if result.returncode == 0:
            console.print("[cyan]Actualizacion DOn3![/cyan]")
            console.print(result.stdout)
        else:
            console.print("[red]Err000r en update![/red]")
            console.print(result.stderr)
    except Exception as e:
        console.print(f"[red]Fallo: {e}[/red]")
