import os, subprocess, shutil

def run(args):
    dir = os.getcwd()
    if shutil.which('kak') is None:
        if os.path.isfile('/etc/debian_version'):
            install_cmd = ['sudo', 'apt', 'install', '-y', 'kakoune']
        elif os.path.isfile('/etc/arch-release'):
            install_cmd = ['sudo', 'pacman', '-S', '--noconfirm', 'kakoune']
        else:
            print("sistema no soportado!< instala kakoune manualmente para tu OS")
            return
        try:
            subprocess.check_call(install_cmd)
            print('kakoune instalado!!!')
        except subprocess.CalledProcessError as e:
            print(f"error instalando kakoune!!: {e}")
            return
        except Exception as e:
            print(f"ERROR!! {e}")
            return
    script_dir = os.path.dirname(os.path.abspath(__file__))
    config_dir = os.path.join(script_dir, 'kakoune')
    env = os.environ.copy()
    env['KAKOUNE_CONFIG'] = config_dir

    if not os.path.isdir(config_dir):
        print('config de kakoune encontrada!! shit!')
        return
    work_dir = os.path.join(script_dir, 'work')
    os.makedirs(work_dir, exist_ok=True)
    try:
        os.chdir(work_dir)
    except Exception as e:
        print('no he podido cambiar a work!!')
        return
    try:
        subprocess.call(['kak'], env=env)
    except Exception as e:
        print(f"error con kakoune!! {e}")
    finally:
         try:
             os.chdir(dir)
             print('aqui de vuelta!')
         except Exception as e:
             print(f"error al volver, ta shit! {e}")
