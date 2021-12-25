import curses
import tiles as tiles
from random import randint
import colorama
from colorama import Fore, Back

screen = curses.initscr()
curses.noecho()
curses.cbreak()
screen.keypad(True)

height = 17
width = 52
game_field = [[tiles.air for j in range(width)] for i in range(height)]

player_x = 1
player_y = 1
player_new_x = 0
player_new_y = 0
player_painted = 0

enemy_x = 50
enemy_y = 15
enemy_new_x = 0
enemy_new_y = 0
enemy_painted = 0

colorama.init(autoreset=True)

def game():
	global player_x, player_y, player_new_x, player_new_y, player_painted
	screen.clear()
	game_init()

	while True:
		screen.addstr(0,0,"")
		for row in game_field:
			screen.addstr(''.join([str(elem) for elem in row]))
			screen.addstr("\n")
		screen.addstr("Player: " + str(player_painted))
		screen.addstr(" | Computer: " + str(enemy_painted))
		
		char = screen.getch()
		if char == curses.KEY_UP:
			player_new_x = player_x
			player_new_y = player_y - 1
		elif char == curses.KEY_LEFT:
			player_new_x = player_x - 1
			player_new_y = player_y
		elif char == curses.KEY_DOWN:
			player_new_x = player_x
			player_new_y = player_y + 1
		elif char == curses.KEY_RIGHT:
			player_new_x = player_x + 1
			player_new_y = player_y
		
		if tiles.is_air(game_field[player_new_y][player_new_x]):
			game_field[player_y][player_x] = tiles.player_paint
			player_x = player_new_x
			player_y = player_new_y
			game_field[player_y][player_x] = tiles.player
			player_painted = player_painted + 1
		
		ai()

def game_init():
	# Set borders
	for x in range(0, width):
		game_field[0][x] = tiles.filled_char
	for x in range(0, height):
		game_field[x][0] = tiles.filled_char
	for x in range(0, width):
		game_field[height - 1][x] = tiles.filled_char
	for x in range(0, height):
		game_field[x][width - 1] = tiles.filled_char
	
	game_field[1][1] = tiles.player
	game_field[15][50] = tiles.enemy

def ai():
	global enemy_x, enemy_y, enemy_new_x, enemy_new_y, enemy_painted
	
	has_moved = False
	retry_count = 0

	while not has_moved:
		if retry_count == 8:
			# Prevent freezing in case AI is stuck.
			break
		retry_count = retry_count + 1
		ai_action = randint(1,4)
		if ai_action == 1:
			enemy_new_x = enemy_x
			enemy_new_y = enemy_y - 1
		elif ai_action == 2:
			enemy_new_x = enemy_x - 1
			enemy_new_y = enemy_y
		elif ai_action == 3:
			enemy_new_x = enemy_x
			enemy_new_y = enemy_y + 1
		elif ai_action == 4:
			enemy_new_x = enemy_x + 1
			enemy_new_y = enemy_y

		if tiles.is_air(game_field[enemy_new_y][enemy_new_x]):
			game_field[enemy_y][enemy_x] = tiles.enemy_paint
			enemy_x = enemy_new_x
			enemy_y = enemy_new_y
			game_field[enemy_y][enemy_x] = tiles.enemy
			enemy_painted = enemy_painted + 1
			has_moved = True

