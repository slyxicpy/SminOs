import os
import shutil
import subprocess

def run(*args, **kwargs):
    dir = os.getcwd()
    if shutil.which('vim') is None:
        if os.path.isfile('etc/debian_version'):
            install_cmd = ['sudo', 'apt', 'install', '-y', 'vim']
        elif os.path.isfile('etc/arch-release'):
            install_cmd = ['sudo', 'pacman', '-S', '--noconfirm', 'vim']
        else:
            print('sistema no soportado para instalar vim, prueba instalarlo manualmente')
            return
        try:
            subprocess.check_call(install_cmd)
            print('Vim instalado!')
        except subprocess.CalledProcessError as e:
            print(f"error instalando vim!: {e}")
            return
        except Exception as e:
            print(f"ERROR! {e}")
            return
    script_dir = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(script_dir, 'vim/.vimrc')
    if not os.path.isfile(config_path):
        print(f"Vimrc no encontrado! shit!")
        return
    work_dir = os.path.join(script_dir, 'work')
    if not os.path.exists(work_dir):
        try:
            os.mkdir(work_dir)
            print("Puesto de trabajo creado ! a coddear !")
        except Exception as e:
            print(f"Erro en crear puesto de work! shit {e}")
            return
    try:
        os.chdir(work_dir)
    except Exception as e:
        print(f"No he podio cambiar a /work!")
        return
    try:
        subprocess.call(['vim', '-u', config_path, '--cmd', 'set noshowcmd | set noruler | set laststatus=0'])
    except Exception as e:
        print(f"Error con vim!: {e}")
    finally:
        try:
            os.chdir(dir)
            print('aqui de vuelta!')
        except Exception as e:
            print(f"Error al volver, ta shit! {e}")
