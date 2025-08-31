import curses
import random
import time

CHARS = list("日月水火木金土田山川上下左右大中小日本語汉字天地人愛夢希望和平龍心静風光雲ア イ ウ エ オ カ キ ク ケ コ サ シ ス セ ソ タ チ ツ テ ト ナ ニ ヌ ネ ノ ハ ヒ フ ヘ ホ マ ミ ム メ モ ヤ ユ ヨ ラ リ ル レ ロ ワ ヲ ン あ い う え お か き く け こ さ し す せ そ た ち つ て と な に ぬ ね の は ひ ふ へ ほ ま み む め も や ゆ よ ら り る れ ろ わ を ん 0123456789")

def run(args=None):
    def matrix_rain(stdscr):
        curses.curs_set(0)
        stdscr.nodelay(True)
        stdscr.timeout(15)
        
        curses.start_color()
        curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLACK)
        curses.init_pair(3, 8, curses.COLOR_BLACK)
        
        height, width = stdscr.getmaxyx()
        
        drops = []
        for i in range(width):
            drops.append({
                'y': random.randint(-height, 0),
                'speed': random.randint(1, 3),
                'length': random.randint(height // 4, height // 2),
                'chars': [random.choice(CHARS) for _ in range(height)]
            })
        
        frame_count = 0
        
        while True:
            stdscr.erase()
            
            for col in range(width):
                drop = drops[col]
                start_y = int(drop['y'])
                length = drop['length']
                
                for row in range(length):
                    y_pos = start_y + row
                    
                    if 0 <= y_pos < height:
                        try:
                            char_index = (y_pos + frame_count) % len(drop['chars'])
                            char = drop['chars'][char_index]
                            
                            if row == 0:
                                stdscr.addstr(y_pos, col, char, curses.color_pair(2) | curses.A_BOLD)
                            elif row < length // 3:
                                stdscr.addstr(y_pos, col, char, curses.color_pair(1) | curses.A_BOLD)
                            elif row < (2 * length) // 3:
                                stdscr.addstr(y_pos, col, char, curses.color_pair(1))
                            else:
                                stdscr.addstr(y_pos, col, char, curses.color_pair(3))
                        except curses.error:
                            pass
                
                drop['y'] += drop['speed']
                
                if drop['y'] > height:
                    drop['y'] = random.randint(-height // 2, -1)
                    drop['speed'] = random.randint(1, 3)
                    drop['length'] = random.randint(height // 4, height // 2)
                    drop['chars'] = [random.choice(CHARS) for _ in range(height)]
            
            for _ in range(width // 8):
                if random.randint(1, 100) <= 2:
                    new_col = random.randint(0, width - 1)
                    drops[new_col]['y'] = random.randint(-height // 4, -1)
                    drops[new_col]['speed'] = random.randint(1, 4)
                    drops[new_col]['length'] = random.randint(height // 6, height // 2)
            
            frame_count += 1
            if frame_count > 1000:
                frame_count = 0
            
            stdscr.refresh()
            time.sleep(0.03)
            
            key = stdscr.getch()
            if key != -1:
                break
    
    curses.wrapper(matrix_rain)
