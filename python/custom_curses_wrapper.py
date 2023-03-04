import os
import curses

# Initialize curses
stdscr = curses.initscr()
# Turn off echoing of keys, and enter cbreak mode,
# where no buffering is performed on keyboard input
curses.noecho()
curses.cbreak()
# In keypad mode, escape sequences for special keys
# (like the cursor keys) will be interpreted and
# a special value like curses.KEY_LEFT will be returned
stdscr.keypad(1)
# Enable scrolling
stdscr.scrollok(True)
stdscr.idlok(True)

# re-define print() function using curses (rudimentary implementation)
_print = print
_screenbuffer = []
def print(*objects, sep=' ', end='\n', file=None, flush=False):
    _screenbuffer.append(*objects)
    curses.update_lines_cols()
    # TODO: '\n' and other formating characters currently not processed
    for s in objects:
        stdscr.addstr(s)
        stdscr.addch(sep)
    if end == '\n':
        _line, _col = curses.getsyx()
        _line += 1
        if _line < curses.LINES:
            stdscr.move(_line, 0)
        else:
            #scroll window for newline at bottom of screen
            stdscr.move(_line-1,0)
            stdscr.scroll()
    stdscr.refresh()


def main():
    # Clear screen
    stdscr.clear()
    key = ' '

    # This raises ZeroDivisionError when i == 10.
    for i in range(0, 120):
        v = i-10
        # 'S' key can skip over the error
        if key == 's':
            key = ' '
            continue
        print('10 divided by {} is {}'.format(v, 10/v))
        key = stdscr.getkey()

try:
    # put your codes here
    main()
except:
    # handle exception here
    pass
finally:
    # cleanup before exit
    stdscr.keypad(0)
    curses.echo()
    curses.nocbreak()
    curses.endwin()
    # re-print screenbuffer
    for objects in _screenbuffer:
        _print(objects)

