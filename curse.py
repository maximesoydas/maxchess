import time
import curses



menu = ['Players', 'Tournaments', 'Reports', 'Exit']

player_menu = ['Add Player', 'View Players', 'Delete Players', 'Exit to Main Menu']

def print_menu(stdscr, selected_row_idx):
    stdscr.clear()
    h, w = stdscr.getmaxyx()

    for idx, row in enumerate(menu):
        x = w//2 - len(row)//2
        y = h//2 - len(menu)//2 + idx
        if idx == selected_row_idx:
            stdscr.attron(curses.color_pair(1))
            stdscr.addstr(y, x, row)
            stdscr.attroff(curses.color_pair(1))
        else:
            stdscr.addstr(y, x, row)

    stdscr.refresh()


def print_player_menu(stdscr, selected_row_idx):
    stdscr.clear()
    h, w = stdscr.getmaxyx()

    for idx, row in enumerate(player_menu):
        x = w//2 - len(row)//2
        y = h//2 - len(player_menu)//2 + idx
        if idx == selected_row_idx:
            stdscr.attron(curses.color_pair(1))
            stdscr.addstr(y, x, row)
            stdscr.attroff(curses.color_pair(1))
        else:
            stdscr.addstr(y, x, row)

    stdscr.refresh()


# def main(stdscr):
#     curses.curs_set(0)
#     curses.init_pair(1, curses.COLOR_RED, curses.COLOR_YELLOW)

#     h, w = stdscr.getmaxyx()

#     text = "Chess Tournament"

#     x = w//2 - len(text)//2

#     y = h//2


#     stdscr.attron(curses.color_pair(1))
#     stdscr.addstr(y, x, text)
#     stdscr.attroff(curses.color_pair(1))


#     stdscr.refresh()
#     time.sleep(3)

# curses.wrapper(main)

def main(stdscr):
    curses.curs_set(0)
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
    current_row_idx = 0

    print_menu(stdscr, current_row_idx)

    while 1:
        key = stdscr.getch()

        stdscr.clear()

        if key == curses.KEY_UP and current_row_idx > 0:
            current_row_idx -= 1 
        elif key == curses.KEY_DOWN and current_row_idx < len(menu)-1:
            current_row_idx += 1
        elif key == curses.KEY_ENTER or key in [10, 13]:
            stdscr.clear()
            stdscr.addstr(0, 0, "You pressed {}".format(menu[current_row_idx]))
            stdscr.refresh()
            stdscr.getch()
            if current_row_idx == len(menu)-1:
                break
            if current_row_idx == len(menu)-4:
                print_player_menu(stdscr, current_row_idx)

            

        print_menu(stdscr, current_row_idx)
        stdscr.refresh()

curses.wrapper(main)