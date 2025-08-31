import os
import shutil
import subprocess

def run(*args, **kwargs):
    original_dir = os.getcwd()
    if shutil.which('nvim') is None:
        if os.path.isfile('/etc/debian_version'):
            install_cmd = ['sudo', 'apt', 'install', '-y', 'neovim']
        elif os.path.isfile('/etc/arch-release'):
            install_cmd = ['sudo', 'pacman', '-S', '--noconfirm', 'neovim']
        else:
            print("Sistema no soportado para nvim intenta instalar manualmente, los siento ;C.")
            return
        try:
            subprocess.check_call(install_cmd)
            print("Neovim instalado!")
        except subprocess.CalledProcessError as e:
            print(f"Error al instalar Neovim: {e}")
            return
        except Exception as e:
            print(f"Error!: {e}")
            return

    script_dir = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(script_dir, 'nvim/init.lua')
    if not os.path.isfile(config_path):
        print("init.lua no encontrado! shit")
        return
    work_dir = os.path.join(script_dir, 'work')
    if not os.path.exists(work_dir):
        try:
            os.mkdir(work_dir)
            print("Carpeta 'work' creada.")
        except Exception as e:
            print(f"Error al crear carpeta 'work': {e}")
            return
    try:
        os.chdir(work_dir)
    except Exception as e:
        print(f"Error al cambiar al directorio 'work': {e}")
        return
    try:
        subprocess.call(['nvim', '-u', config_path, '--cmd', 'set noshowcmd | set noruler | set laststatus=0'])
    except Exception as e:
        print(f"Error Neovim: {e}")
    finally:
        try:
            os.chdir(original_dir)
            print("Aqui de nuevol!")
        except Exception as e:
            print(f"Error al volver al directorio original: {e}")
