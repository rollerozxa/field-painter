import curses

screen = curses.initscr()
curses.noecho()
curses.cbreak()
screen.keypad(True)

def options():
	options_selection = 1
	while True:		
		screen.addstr(0,0,"================================ Field Painter ================================")
		if options_selection == 1:
			screen.addstr(1,0,"<! Input !>  <  Gameplay  >  <  Sound  >")
		elif options_selection == 2:
			screen.addstr(1,0,"<  Input  >  <! Gameplay !>  <  Sound  >")
		elif options_selection == 3:
			screen.addstr(1,0,"<  Input  >  <  Gameplay  >  <! Sound !>")
		char = screen.getch()
		if char == curses.KEY_UP:
			if options_selection == 1:
				options_selection = 4
			else:
				options_selection = options_selection - 1
		elif char == curses.KEY_DOWN:
			if options_selection == 4:
				options_selection = 1
			else:
				options_selection = options_selection + 1
		elif char == 10:
			if options_selection == 1:
				options_input()

def options_input():
	options_input_selection = 1
	while True:
		screen.addstr(0,0,"================================ Field Painter ================================")
		screen.addstr(1,0,"                                   < Input >")
		screen.addstr(2,0,"Up")
		
