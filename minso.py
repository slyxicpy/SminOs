import os
import sys
import time
import importlib.util
import readline
from typing import List, Optional

OS_NAME = "Smin OS"
VERSION = "v0.1"
AUTHOR = "Styx"
GITHUB = "https://github.com/slyxicpy"
SYSTEM_DIR = "./system"
PLUGINS_DIR = "./plugins"

class Colors:
    RESET = '\033[0m'
    BOLD = '\033[1m'
    DIM = '\033[2m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    WHITE = '\033[97m'
    GRAY = '\033[90m'
    BG_BLACK = '\033[40m'
    BG_CYAN = '\033[46m'

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def animacion():
    print(f"{Colors.CYAN}[{Colors.WHITE} Iniciando {OS_NAME}... {Colors.CYAN}]{Colors.RESET}")
    loading_chars = ['⠋', '⠙', '⠹', '⠸', '⠼', '⠴', '⠦', '⠧', '⠇', '⠏']
    for i in range(20):
        char = loading_chars[i % len(loading_chars)]
        print(f"\r{Colors.CYAN}[{Colors.WHITE} {char} Cargando... {Colors.CYAN}]{Colors.RESET}", end='', flush=True)
        time.sleep(0.1)
    print(f"\r{Colors.GREEN}[{Colors.WHITE} ✓ cargado correctamente bitch!{Colors.GREEN}]{Colors.RESET}")
    time.sleep(0.5)

def montado():
    mount_points = [
        "/system", "/bubbys", "/plugins"
    ]
    #print(f"\n{Colors.YELLOW}{'#' * 40}{Colors.RESET}")
    print(f"{Colors.CYAN}[{Colors.WHITE} Montando... {Colors.CYAN}]{Colors.RESET}")
   
    for mount in mount_points:
        print(f"{Colors.CYAN}[{Colors.WHITE} Montanto {Colors.GREEN}{mount}{Colors.WHITE} {Colors.CYAN}]{Colors.RESET}")
        time.sleep(0.2)
    print(f"{Colors.CYAN}[{Colors.WHITE} Montado! {Colors.CYAN}]{Colors.RESET}")
    print(f"{Colors.GREEN}> chrooting{Colors.RESET}")

def mohamed():
    art = f"""
{Colors.MAGENTA}
                                                          .dP"Yb         
                                  db                    dP'   d'         
                                                                         
        .d888b.  `Yb d88b d88b   'Yb `Yb d88b d88b        'Yb    .d888b. 
        8'   `Yb  88P   88   8b   88  88P   8Y   8b        88    8'   `Yb
        Yb.   88  88    8P   88   88  88    8P   88        88    Yb.   88
            .dP   88  .dP  .dP   .8P .8P  bdP  bdP        .8P        .dP 
          .dP'   .888888888888b.                                   .dP'  
        .dP'                                                     .dP'    
{Colors.RESET}
    """

    bat_logo = f"""                               			{Colors.CYAN}             ⠠⢀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⡀⠄{Colors.RESET}
            ⠀⠀{Colors.CYAN}⠈⠻⢿⣷⣶⣦⣤⣤⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣤⣤⣶⣶⣾⣿⠟⠉⠀{Colors.RESET}⠀
            ⠀⠀⠀⠀⠀{Colors.CYAN}⠹⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀⠀⠀⠀⠐⡄⠀⢀⠂⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⠟⠁{Colors.RESET}⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀{Colors.CYAN}⠉⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⣷⣶⣾⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⠃{Colors.RESET}⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀{Colors.CYAN}   ⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣿⣿⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇{Colors.RESET}⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀{Colors.CYAN}⢰⣿⣿⣿⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⣿⣿⣿⡇{Colors.RESET}⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀{Colors.CYAN}⠈⠁⠀⠀⠀⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠁⠀⠀⠀⠀⠀⠈⠑{Colors.RESET}⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀{Colors.CYAN}⠈⠉⠻⣿⣿⣿⠟⠉⠉⠀{Colors.RESET}⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀{Colors.CYAN}⠈⢿⠙⠀{Colors.RESET}⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀{Colors.CYAN}⠁{Colors.RESET}⠀⠀
            {Colors.RED}		     By styx Vbeta{Colors.RESET}⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀"""    
    system_info = f"""
{Colors.CYAN}Usser@localhost{Colors.RESET}
{Colors.GRAY}{'─' * 15}{Colors.RESET}
{Colors.CYAN}OS:{Colors.RESET} {OS_NAME}
{Colors.CYAN}Host:{Colors.RESET} Olive Tyx
{Colors.CYAN}Kernel:{Colors.RESET} Sexshop-kamui {VERSION}
{Colors.CYAN}Uptime:{Colors.RESET} 6 day, 6 hours, 6 mins
{Colors.CYAN}Packages:{Colors.RESET} 666 (pacman)
{Colors.CYAN}Shell:{Colors.RESET} {OS_NAME} {VERSION}
{Colors.CYAN}Terminal:{Colors.RESET} AexTrm
{Colors.CYAN}Down-level:{Colors.RESET} 0%
{Colors.CYAN}IP:{Colors.RESET} 166.166.1.666/24
{Colors.CYAN}Battery:{Colors.RESET} 666% [Discharging]
{Colors.CYAN}Locale:{Colors.RESET} en_US.UTF-888
{Colors.YELLOW}█{Colors.BLUE}█{Colors.RED}█{Colors.RESET} {Colors.CYAN}+{Colors.RESET} {Colors.YELLOW}5{Colors.BLUE}9{Colors.RED}3{Colors.RESET}
    """
    print(art)
    print()
    info_lines = system_info.strip().split('\n')
    bat_lines = bat_logo.strip().split('\n')
    max_lines = max(len(info_lines), len(bat_lines))
    
    for i in range(max_lines):
        info_line = info_lines[i] if i < len(info_lines) else ""
        bat_line = bat_lines[i] if i < len(bat_lines) else ""
        print(f"{info_line:<50} {bat_line}")
    print()
    print(f"{Colors.GRAY}{'─' * 80}{Colors.RESET}")
    print(f"{Colors.CYAN}Version:{Colors.RESET} {Colors.WHITE}{VERSION}{Colors.RESET} | {Colors.CYAN}Author:{Colors.RESET} {Colors.WHITE}{AUTHOR}{Colors.RESET}")
    print(f"{Colors.CYAN}GitHub:{Colors.RESET} {Colors.BLUE}{GITHUB}{Colors.RESET}")
    print(f"{Colors.GRAY}{'─' * 80}{Colors.RESET}")

def load_module(path: str) -> Optional[object]:
    if not os.path.exists(path):
        return None
    try:
        spec = importlib.util.spec_from_file_location("module.name", path)
        if spec is None or spec.loader is None:
            return None
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        return mod
    except Exception as e:
        print(f"{Colors.RED}[Error al cargar módulo {path}]: {e}{Colors.RESET}")
        return None

def scan_commands() -> dict:
    commands = {'system': [], 'plugins': []}
    if os.path.exists(SYSTEM_DIR):
        for file in os.listdir(SYSTEM_DIR):
            if file.endswith('.py') and not file.startswith('__'):
                commands['system'].append(file[:-3])
    if os.path.exists(PLUGINS_DIR):
        for file in os.listdir(PLUGINS_DIR):
            if file.endswith('.py') and not file.startswith('__'):
                commands['plugins'].append(file[:-3])
    return commands

def show_help(commands: dict):
    print(f"\n{Colors.CYAN}[{Colors.WHITE} {OS_NAME} - Comandos {Colors.CYAN}]{Colors.RESET}")
    print(f"{Colors.GRAY}{'─' * 50}{Colors.RESET}")
    
    print(f"{Colors.BLUE}Sistema:{Colors.RESET}")
    if commands['system']:
        for cmd in sorted(commands['system']):
            print(f"  {Colors.CYAN}.{cmd}{Colors.RESET}")
    else:
        print(f"  {Colors.DIM}No hay sistema disponible{Colors.RESET}")
    
    print(f"\n{Colors.BLUE}Plugins:{Colors.RESET}")
    if commands['plugins']:
        for cmd in sorted(commands['plugins']):
            print(f"  {Colors.CYAN}${cmd}{Colors.RESET}")
    else:
        print(f"  {Colors.DIM}No hay plugins disponibles{Colors.RESET}")
    
    print(f"\n{Colors.BLUE}Integrados:{Colors.RESET}")
    print(f"  {Colors.CYAN}help{Colors.RESET}     - Esta ayuda")
    print(f"  {Colors.CYAN}clear{Colors.RESET}    - Limpia")
    print(f"  {Colors.CYAN}exit{Colors.RESET}     - Sale del sistema")
    print(f"  {Colors.CYAN}info{Colors.RESET}     - Info de sistema")
    print(f"  {Colors.CYAN}scan{Colors.RESET}     - Reescanea comandos disponibles")

def show_system_info():
    print(f"\n{Colors.CYAN}[{Colors.WHITE} Info Sistema {Colors.CYAN}]{Colors.RESET}")
    print(f"{Colors.GRAY}{'─' * 40}{Colors.RESET}")
    print(f"{Colors.YELLOW}Name:{Colors.RESET} {OS_NAME}")
    print(f"{Colors.YELLOW}V:{Colors.RESET} {VERSION}")
    print(f"{Colors.YELLOW}Autor:{Colors.RESET} {AUTHOR}")
    print(f"{Colors.YELLOW}Directorio Sistema:{Colors.RESET} {SYSTEM_DIR}")
    print(f"{Colors.YELLOW}Directorio Plugins:{Colors.RESET} {PLUGINS_DIR}")
    print(f"{Colors.YELLOW}Python V:{Colors.RESET} {sys.version.split()[0]}")

def run_command(cmd_input: str, commands: dict):
    if not cmd_input:
        return commands
    if cmd_input == "help":
        show_help(commands)
        return commands
    elif cmd_input == "clear":
        clear_screen()
        mohamed()
        return commands
    elif cmd_input == "info":
        show_system_info()
        return commands
    elif cmd_input == "scan":
        print(f"{Colors.CYAN}[{Colors.WHITE} Reescaneando comandos... {Colors.CYAN}]{Colors.RESET}")
        commands = scan_commands()
        print(f"{Colors.GREEN}[{Colors.WHITE} Comandos actualizados {Colors.GREEN}]{Colors.RESET}")
        return commands
    parts = cmd_input.split()
    cmd_name = parts[0]
    args = parts[1:]
    
    if cmd_name.startswith('.'):
        actual_cmd = cmd_name[1:]
        cmd_path = os.path.join(SYSTEM_DIR, f"{actual_cmd}.py")
        cmd_type = "sistema"
    elif cmd_name.startswith('$'):
        actual_cmd = cmd_name[1:]
        cmd_path = os.path.join(PLUGINS_DIR, f"{actual_cmd}.py")
        cmd_type = "plugin"
    else:
        system_path = os.path.join(SYSTEM_DIR, f"{cmd_name}.py")
        plugin_path = os.path.join(PLUGINS_DIR, f"{cmd_name}.py")
        
        if os.path.exists(system_path):
            cmd_path = system_path
            cmd_type = "sistema"
            actual_cmd = cmd_name
        elif os.path.exists(plugin_path):
            cmd_path = plugin_path
            cmd_type = "plugin"
            actual_cmd = cmd_name
        else:
            print(f"{Colors.RED}[Error]{Colors.RESET} {cmd_name}: comando no encontrado perra!")
            print(f"{Colors.DIM}Typea 'help' para ver comandos disponibles{Colors.RESET}")
            return commands
    
    print(f"{Colors.DIM}[Ejecutando {cmd_type}: {actual_cmd}]{Colors.RESET}")
    
    mod = load_module(cmd_path)
    if mod and hasattr(mod, "run"):
        try:
            mod.run(args)
        except Exception as e:
            print(f"{Colors.RED}[Error al ejecutar {actual_cmd}]: {e}{Colors.RESET}")
    else:
        print(f"{Colors.RED}[Error]{Colors.RESET} {actual_cmd}: no tiene función 'run' válida")
    
    return commands

def get_prompt():
    return f"{Colors.CYAN}codak@{OS_NAME.lower().replace(' ', '-')}{Colors.RESET}:{Colors.BLUE}~{Colors.RESET}$ "

def terminal():
    commands = scan_commands()
    
    print(f"\n{Colors.GREEN}[{Colors.WHITE} Iniciado correctamente perra! {Colors.GREEN}]{Colors.RESET}")
    print(f"{Colors.DIM}Typea 'help' para ver comandos disponibles{Colors.RESET}\n")
    
    while True:
        try:
            user_input = input(get_prompt()).strip()
            if not user_input:
                continue
            if user_input in ["exit", "quit", "logout"]:
                print(f"\n{Colors.CYAN}[{Colors.WHITE} Cerrando {OS_NAME}... {Colors.CYAN}]{Colors.RESET}")
                time.sleep(0.5)
                print(f"{Colors.GREEN}[{Colors.WHITE} ¡bye beach! {Colors.GREEN}]{Colors.RESET}")
                break
            
            commands = run_command(user_input, commands)
            
        except KeyboardInterrupt:
            print(f"\n{Colors.YELLOW}[{Colors.WHITE} Usa 'exit' para salir !{Colors.YELLOW}]{Colors.RESET}")
        except EOFError:
            print(f"\n{Colors.CYAN}[{Colors.WHITE} Saliendo... {Colors.CYAN}]{Colors.RESET}")
            break

def directorios():
    for directory in [SYSTEM_DIR, PLUGINS_DIR]:
        if not os.path.exists(directory):
            os.makedirs(directory)
            print(f"{Colors.GREEN}[{Colors.WHITE} Directorio creado: {directory} {Colors.GREEN}]{Colors.RESET}")

def main():
    clear_screen()
    animacion()
    montado()
    time.sleep(1)
    clear_screen()
    mohamed()
    directorios()
    terminal()

if __name__ == "__main__":
    main()
