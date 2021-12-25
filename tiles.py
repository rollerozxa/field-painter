air = " "
filled_char = "█"
player = "O"
enemy = "Ø"
player_paint = "▓"
enemy_paint = "▒"

def is_air(tile):
	if tile == air:
		return True
	elif tile == player_paint:
		return True
	elif tile == enemy_paint:
		return True
	else:
		return False
