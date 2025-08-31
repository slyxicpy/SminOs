import platform
import os
import shutil
import psutil
import socket
import datetime
from rich.console import Console
from rich.panel import Panel
from rich.layout import Layout
from rich import box

def get_uptime():
    try:
        boot_time = psutil.boot_time()
        now = datetime.datetime.now().timestamp()
        uptime_seconds = now - boot_time
        days = int(uptime_seconds // (24 * 3600))
        hours = int((uptime_seconds % (24 * 3600)) // 3600)
        minutes = int((uptime_seconds % 3600) // 60)
        return f"{days}d {hours}h {minutes}m"
    except Exception as e:
        return f"Error: {str(e)}"

def get_memory_info():
    try:
        mem = psutil.virtual_memory()
        swap = psutil.swap_memory()
        return (
            f"{mem.used / (1024**3):.1f}/{mem.total / (1024**3):.1f} GB ({mem.percent}%)",
            f"{swap.used / (1024**3):.1f}/{swap.total / (1024**3):.1f} GB ({swap.percent}%)"
        )
    except Exception as e:
        return f"Error: {str(e)}", f"Error: {str(e)}"

def get_disk_info():
    try:
        disk = psutil.disk_usage('/')
        return f"{disk.used / (1024**3):.1f}/{disk.total / (1024**3):.1f} GB ({disk.percent}%)"
    except Exception as e:
        return f"Error: {str(e)}"

def get_network_info():
    try:
        hostname = socket.gethostname()
        ip = socket.gethostbyname(hostname)
        return hostname, ip
    except Exception as e:
        return f"Error: {str(e)}", f"Error: {str(e)}"

def get_cpu_info():
    try:
        cpu_name = platform.processor()
        if not cpu_name or cpu_name.strip() == "":
            if os.path.exists("/proc/cpuinfo"):
                with open("/proc/cpuinfo", "r") as f:
                    for line in f:
                        if line.startswith("model name"):
                            cpu_name = line.split(":")[1].strip()
                            break
            else:
                cpu_name = "Unknown CPU"
        return cpu_name or "N/A"
    except Exception as e:
        return f"Error: {str(e)}"


def run(args=None):
    console = Console()
    layout = Layout()
    try:
        uname = platform.uname()
        mem_used, swap_used = get_memory_info()
        hostname, ip = get_network_info()
        cpu_name = get_cpu_info()
        specs = f"""
[bold cyan]OS:[/bold cyan] {uname.system} {uname.release}
[bold cyan]Kernel:[/bold cyan] {uname.version.split()[0] if uname.version else 'N/A'}
[bold cyan]CPU:[/bold cyan] {cpu_name}
[bold cyan]CPU Cores:[/bold cyan] {psutil.cpu_count(logical=False) or 'N/A'} physical, {psutil.cpu_count() or 'N/A'} logical
[bold cyan]CPU Freq:[/bold cyan] {(psutil.cpu_freq().current if psutil.cpu_freq() else 'N/A'):.1f} MHz
[bold cyan]Machine:[/bold cyan] {uname.machine or 'N/A'}
[bold cyan]Memory:[/bold cyan] {mem_used}
[bold cyan]Swap:[/bold cyan] {swap_used}
[bold cyan]Disk:[/bold cyan] {get_disk_info()}
[bold cyan]Uptime:[/bold cyan] {get_uptime()}
[bold cyan]Hostname:[/bold cyan] {hostname}
[bold cyan]IP:[/bold cyan] {ip}
[bold cyan]Python:[/bold cyan] {platform.python_version()}
[bold cyan]Shell:[/bold cyan] {os.environ.get("SHELL", "N/A")}
[bold cyan]Terminal:[/bold cyan] {shutil.get_terminal_size().columns} cols x {shutil.get_terminal_size().lines} rows
"""

    except Exception as e:
        specs = f"[red]Error!!!@@@@ system info: {str(e)}[/red]"

    layout.update(
        Panel(specs, title="Info sistema!", border_style="cyan", box=box.ROUNDED)
    )
    console.print(layout)

if __name__ == "__main__":
    run()
