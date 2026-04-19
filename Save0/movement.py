def toggle_dir(direction):
	if direction == North:
		return South
	elif direction == South:
		return North		
	elif direction == West:
		return East
	elif direction == East:
		return West 
		
def better_movement(y_dir, next_move):
	move(next_move)
	pos_y = get_pos_y()
	if pos_y == (get_world_size() - 1) or pos_y == 0:
		if next_move == East:
			y_dir = toggle_dir(y_dir)
			next_move = y_dir
		else:
			next_move = East
	return y_dir, next_move 
		