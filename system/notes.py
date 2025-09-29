import os
import curses
import sys

NOTES_DIR = os.path.expanduser("sminHome/notes")

def run(*args):
    note_name = None
    if args and len(args) > 0:
        if isinstance(args[0], list) and len(args[0]) > 0:
            note_name = args[0][0]
        elif isinstance(args[0], str):
            note_name = args[0]
    try:
        os.makedirs(NOTES_DIR, exist_ok=True)
    except Exception as e:
        print(f"Error al crear directorio {NOTES_DIR}: {e}")
        return

    def open_note(stdscr, path):
        curses.curs_set(1)
        try:
            if os.path.isfile(path):
                with open(path, "r", encoding="utf-8") as f:
                    lines = f.read().splitlines()
            else:
                lines = []
        except Exception as e:
            stdscr.clear()
            stdscr.addstr(0, 0, f"Error al leer la nota: {e}")
            stdscr.addstr(2, 0, "Presiona cualquier tecla para continuar...")
            stdscr.refresh()
            stdscr.getch()
            return

        input_str = ""
        scroll_offset = 0
        modified = False
        while True:
            try:
                max_y, max_x = stdscr.getmaxyx()
                display_lines = max_y - 6
                
                stdscr.clear()
                stdscr.addstr(0, 0, f"---- ‿̩͙⊱༒︎༻Notes♱Usser༺༒︎⊰‿̩͙ ---- {os.path.basename(path)}")
                
                for i in range(scroll_offset, min(scroll_offset + display_lines, len(lines))):
                    line_num = i + 1
                    display_line = lines[i][:max_x-6] if len(lines[i]) > max_x-6 else lines[i]
                    stdscr.addstr(i - scroll_offset + 2, 0, f"{line_num:02d}| {display_line}")
                status = "MODIFICADO - " if modified else ""
                stdscr.addstr(max_y - 3, 0, f"{status}':w' guardar, ':q' salir")
                prompt_line = f"> {input_str}"
                if len(prompt_line) > max_x - 1:
                    prompt_line = f"> ...{input_str[-(max_x-8):]}"
                stdscr.addstr(max_y - 1, 0, prompt_line)
                stdscr.refresh()
                key = stdscr.getch()
                if key in [10, 13]:
                    if input_str == ":w":
                        try:
                            os.makedirs(os.path.dirname(path), exist_ok=True)
                            with open(path, "w", encoding="utf-8") as f:
                                if lines:
                                    f.write("\n".join(lines) + "\n")
                                else:
                                    f.write("")
                            modified = False
                            stdscr.clear()
                            stdscr.addstr(0, 0, f"¡Guardado en {path}!")
                            stdscr.addstr(1, 0, "Presiona cualquier tecla para continuar...")
                            stdscr.refresh()
                            stdscr.getch()
                        except Exception as e:
                            stdscr.clear()
                            stdscr.addstr(0, 0, f"Error al guardar: {e}")
                            stdscr.addstr(2, 0, "Presiona cualquier tecla para continuar...")
                            stdscr.refresh()
                            stdscr.getch()
                    elif input_str == ":q":
                        if modified:
                            stdscr.clear()
                            stdscr.addstr(0, 0, "Hay cambios sin guardar!")
                            stdscr.addstr(1, 0, "':w' para guardar, ':q!' para salir sin guardar")
                            stdscr.refresh()
                            stdscr.getch()
                        else:
                            break
                    elif input_str == ":q!":
                        break
                    else:
                        if input_str.strip():
                            lines.append(input_str)
                            modified = True
                            if len(lines) > display_lines:
                                scroll_offset = max(0, len(lines) - display_lines)
                    input_str = ""
                elif key == 27:
                    input_str = ""
                elif key in [curses.KEY_BACKSPACE, 127, 8]:
                    input_str = input_str[:-1]
                elif key == curses.KEY_UP and scroll_offset > 0:
                    scroll_offset -= 1
                elif key == curses.KEY_DOWN and scroll_offset < max(0, len(lines) - display_lines):
                    scroll_offset += 1
                elif 32 <= key <= 126:
                    input_str += chr(key)
            except curses.error:
                pass
    if note_name:
        if not note_name.endswith(".txt"):
            note_name += ".txt"
        path = os.path.join(NOTES_DIR, note_name)
        try:
            curses.wrapper(open_note, path)
        except Exception as e:
            print(f"Error al abrir la nota lo siento pipip: {e}")
    else:
        try:
            if not os.path.exists(NOTES_DIR):
                print("No hay notas. Crea una usando: notes nombre_de_nota")
                return
            all_files = os.listdir(NOTES_DIR)
            notes_list = [f for f in all_files if f.endswith(".txt") and os.path.getsize(os.path.join(NOTES_DIR, f)) >= 0]
            print(f"Db: Archivos en {NOTES_DIR}: {all_files}")
            print(f"Db: Notas encontradas: {notes_list}")
            if not notes_list:
                print("No hay notas. Crea una usando: notes nombre_nota")
                return
            notes_list.sort()
        except Exception as e:
            print(f"Error al listar notas: {e}")
            return
        def menu(stdscr):
            curses.curs_set(0)
            current = 0
            scroll_offset = 0 
            while True:
                try:
                    max_y, max_x = stdscr.getmaxyx()
                    display_lines = max_y - 4
                    stdscr.clear()
                    stdscr.addstr(0, 2, "Selecciona con flechas & ♱ Enter (Esc para salir!)")
                    stdscr.addstr(1, 2, "-" * 50)
                    for idx in range(scroll_offset, min(scroll_offset + display_lines, len(notes_list))):
                        display_name = notes_list[idx]
                        if len(display_name) > max_x - 8:
                            display_name = display_name[:max_x-11] + "..."
                        if idx == current:
                            stdscr.attron(curses.A_REVERSE)
                            stdscr.addstr(idx - scroll_offset + 2, 4, f"► {display_name}")
                            stdscr.attroff(curses.A_REVERSE)
                        else:
                            stdscr.addstr(idx - scroll_offset + 2, 4, f"  {display_name}")
                    stdscr.refresh()
                    key = stdscr.getch()
                    if key == curses.KEY_UP:
                        if current > 0:
                            current -= 1
                            if current < scroll_offset:
                                scroll_offset = current
                    elif key == curses.KEY_DOWN:
                        if current < len(notes_list) - 1:
                            current += 1
                            if current >= scroll_offset + display_lines:
                                scroll_offset = current - display_lines + 1
                    elif key in [10, 13]:
                        selected_note = os.path.join(NOTES_DIR, notes_list[current])
                        stdscr.clear()
                        stdscr.refresh()
                        curses.wrapper(open_note, selected_note)
                        return
                    elif key == 27:
                        break 
                except curses.error:
                    pass
        try:
            curses.wrapper(menu)
        except Exception as e:
            print(f"Error en el menu!!!@: {e}")

if __name__ == "__main__":
    try:
        if len(sys.argv) > 1:
            run(sys.argv[1])
        else:
            run()
    except KeyboardInterrupt:
        print("\nOperación cancelada!")
    except Exception as e:
        print(f"Error: {e}")
