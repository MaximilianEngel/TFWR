from __builtins__ import *
from tools import *
from mapper import *

current_x_direction = None
current_y_direction = None
next_direction = None
prio_move = None
last_step = None
furthest_reached_x = 0
		
def default_movement():
	next_move = get_next_direction()
	y_dir = get_current_y_direction()
	move(next_move)
	x,y = get_coordinates()
	if x >= get_my_world_size():
		reset_default_movement()
		return
	if y == (get_my_world_size() - 1) or y == 0:
		if next_move == East:
			y_dir = toggle_dir(y_dir)
			next_move = y_dir
		else:
			next_move = East
	set_current_y_direction(y_dir)
	set_next_direction(next_move)


def snake_movement():
	next_move = get_next_direction()
	x_dir = get_current_x_direction()
	y_dir = get_current_y_direction()
	x,y = get_coordinates()
	
	moved_in_next_column = next_move in [West, East]
		
	move(next_move)
	x,y = get_coordinates()
	ws = get_my_world_size()
	if (y == (ws - 1) and y_dir == North) or (y == 0 and y_dir == South):
		if next_move == West or next_move == East:
			y_dir = toggle_dir(y_dir)
			next_move = y_dir
		else:
			next_move = x_dir
		
		if (x == (ws - 1) and x_dir == East) or (x == 0 and x_dir == West):
			if next_move == North or next_move == South:
				x_dir = toggle_dir(x_dir)
				next_move = y_dir
			else:
				next_move = x_dir 
				
	set_current_x_direction(x_dir)
	set_current_y_direction(y_dir)
	set_next_direction(next_move)
	return moved_in_next_column
	
	
def moveTo(tx,ty):
	x,y = get_coordinates()
	
	vector = calc_best_vector(x, y, tx, ty)
	
	directions = [East, North]
	if 0 > vector[0]:
		directions[0] = West
	if 0 > vector[1]:
		directions[1] = South
	
	abs_vector = (abs(vector[0]), abs(vector[1]))
	sv = get_smallest(abs_vector)
	index_farther_direction = toggle_binary(sv["index"])
	closer_vector = sv["value"]
	farther_vector = abs_vector[index_farther_direction]
	
	for step_count in range(abs(closer_vector)):
		move(directions[0])
		move(directions[1])
	
	for remaining_steps in range(farther_vector - closer_vector):  
		move(directions[index_farther_direction])
		
def cactus_movement():
	x_dir = get_current_x_direction()
	y_dir = get_current_y_direction()
	x, y = get_coordinates()
	prio_move = get_prio_move()
	last_step = get_last_step()
	
	if prio_move:
		next_move = prio_move
		
		
	elif last_step:
		next_move = last_step
	else:
		next_move = y_dir
	
	if last_step in [West, East]:
		next_move = y_dir
	else:
		next_move = avoid_obstacle(next_move)
	
	move(next_move)
	set_last_step(next_move)
	
	
		 
def avoid_obstacle(current_move):
	y_dir = get_current_y_direction()
	x_dir = get_current_x_direction()
	x,y = get_coordinates()
	
	blocked = get_blocked_fields()
	free_spaces = get_free_spaces()
	coor_change = {
		North: (0, +1),
		West: (-1, 0),
		East: (+1, 0),
		South: (0, -1)
	}
	
	next_move = current_move 
	square_ahead = (x + coor_change[current_move][0], y + coor_change[current_move][1])
	
	while square_ahead in blocked or not in_square_boundries(square_ahead):
		
		if next_move in [North, South]:
			next_move = get_current_x_direction()
			set_current_y_direction(toggle_dir(y_dir))
		elif next_move in [West, East]:
			direction_avoided = next_move
			next_move = get_current_y_direction()
			
			if not in_square_boundries(square_ahead) or len(free_spaces[x + coor_change[next_move][0]]) == 0:
				set_current_x_direction(toggle_dir(get_current_x_direction()))
				next_move = get_current_x_direction()
			else: 
				set_prio_move(direction_avoided)
				
		square_ahead = (x + coor_change[next_move][0], y + coor_change[next_move][1])
	
	if get_prio_move() == next_move:
		set_prio_move(None)
		return next_move
		
	if (current_move == next_move) and (current_move in [West, East]):
		next_move = get_current_y_direction()
	
	
	return next_move
		
	

############################## GETTER/SETTER ###############################
	
def get_current_x_direction():
	global current_x_direction
	return current_x_direction
	
def get_current_y_direction():
	global current_y_direction
	return current_y_direction

def set_current_x_direction(direction):
	global current_x_direction
	if direction not in [West, East]:
		print(str(direction) + " is not valid X-axis direction")
		return
	current_x_direction = direction

def set_current_y_direction(direction):
	global current_y_direction
	if direction not in [North, South]:
		print(str(direction) + " is not valid Y-axis direction")
		return
	current_y_direction = direction


def get_next_direction():
	global next_direction
	return next_direction
	
def set_next_direction(direction):
	global next_direction
	if direction not in [North, South, West, East]:
		print(str(direction) + " is not valid direction")
		return
	next_direction = direction

def set_last_step(direction):
	global last_step
	last_step = direction
	
def get_last_step():
	global last_step
	return last_step
		
def get_prio_move():
	global prio_move
	return prio_move		
		
def set_prio_move(direction):
	global prio_move
	prio_move = direction
		
def reset_default_movement():
	global next_direction
	global current_y_direction
	moveTo(0,0)
	current_y_direction = North
	next_direction = North
	
def reset_snake_movement():
	global next_direction
	global current_x_direction
	global current_y_direction
	moveTo(0,0)
	next_direction = North
	current_x_direction = East
	current_y_direction = North
	
def set_furthest_reached_x(x):
	global furthest_reached_x
	furthest_reached_x = x
	
def get_furthest_reached_x():
	global furthest_reached_x
	return furthest_reached_x