import curses

print("prepairing to initialize screen...")
screen = curses.initscr()
print("screen initialized")
screen.refresh()

curses.napms(2000)
curses.endwin()
print("window ended")