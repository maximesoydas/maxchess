import time
import curses


def main(stdscr):
    curses.curs_set(0)
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_YELLOW)

    h, w = stdscr.getmaxyx()

    text = "Chess Tournament"

    x = w//2 - len(text)//2

    y = h//2


    stdscr.attron(curses.color_pair(1))
    stdscr.addstr(y, x, text)
    stdscr.attroff(curses.color_pair(1))


    stdscr.refresh()
    time.sleep(3)

curses.wrapper(main)

def main2(stdscr):
    curses.curs_set(0)

    while 1:
        key = stdscr.getch()

        stdscr.clear()

        if key == curses.KEY_UP: 
            stdscr.addstr(0, 0, "you pressed up key")
        elif key == curses.KEY_DOWN:
            stdscr.addstr(0,0, "downkey")
        elif key == curses.KEY_ENTER or key in [10, 13]:
            stdscr.addstr(0, 0, "pressed enter")

        stdscr.refresh()

curses.wrapper(main2)