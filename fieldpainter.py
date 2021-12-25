import curses
import os
from game import *
#from functions import *
from options import *

screen = curses.initscr()
curses.noecho()
curses.cbreak()
screen.keypad(True)

mainmenu_selection = 1

try:
	while True:
		screen.addstr(0, 0, '================================ Field Painter ================================')
		screen.addstr(1, 0, '')
		if mainmenu_selection == 1:
			screen.addstr(2, 0, '[X] Start Game')
		else:
			screen.addstr(2, 0, '[ ] Start Game')
		if mainmenu_selection == 2:
			screen.addstr(3, 0, '[X] Help')
		else:
			screen.addstr(3, 0, '[ ] Help')
		if mainmenu_selection == 3:
			screen.addstr(4, 0, '[X] Options')
		else:
			screen.addstr(4, 0, '[ ] Options')
		if mainmenu_selection == 4:
			screen.addstr(5, 0, '[X] Exit')
		else:
			screen.addstr(5, 0, '[ ] Exit')

		char = screen.getch()
		screen.addstr(9, 0, str(char) + ' ')
		if char == curses.KEY_UP:
			if mainmenu_selection == 1:
				mainmenu_selection = 4
			else:
				mainmenu_selection = mainmenu_selection - 1
		elif char == curses.KEY_DOWN:
			if mainmenu_selection == 4:
				mainmenu_selection = 1
			else:
				mainmenu_selection = mainmenu_selection + 1
		elif char == 10:
			if mainmenu_selection == 1:
				game()
			elif mainmenu_selection == 2:
				screen.addstr(0,0,os.popen("fmt -w 80 help.txt").read())
				screen.getch()
			elif mainmenu_selection == 3:
				options()
			elif mainmenu_selection == 4:
				break
finally:
	# shut down cleanly
	curses.nocbreak(); screen.keypad(0); curses.echo()
	curses.endwin()
