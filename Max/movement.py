from __builtins__ import *
from tools import *

current_x_direction = None
current_y_direction = None
next_direction = None
my_world_size = get_world_size()

def toggle_dir(direction):
	toggle_map = {
		North: South,
		South: North,
		West: East,
		East: West
	}
	return toggle_map[direction]
		
		
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
	
	move(next_move)
	x,y = get_coordinates()
	ws = get_my_world_size()
	if (y == (ws - 1) and y_dir == North) or (y == 0 and y_dir == South):
		if next_move == West or next_move == East:
			y_dir = toggle_dir(y_dir)
			set_current_y_direction(y_dir)
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
	return next_move in [North, South]
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

############################# Calculations ##############################

#returns list: [#possible_fields, remainer]
def calc_possible_fields(field_size, space_between, board_size=get_my_world_size()):
	field_amount = 0
	if field_size < board_size:
		field_amount += ((board_size - field_size) // (field_size + space_between)) + 1
		remainer = board_size - ((field_amount * field_size) + ((field_amount - 1) * space_between))
		return [field_amount, remainer]
	elif field_size == board_size:
		return [1, 0]
	else: 
		return [0, board_size] 
		
def calculate_fields_in_remainer(remainer, space_between=1, ws=get_my_world_size()):
	pumpkin_size = remainer - space_between
	fields_x, re_remainer = calc_possible_fields(pumpkin_size, space_between, ws) 
	fields_y = fields_x - 1
	return [fields_x, fields_y, pumpkin_size, re_remainer]	

def calc_best_vector(x, y, tx, ty):
	ws = get_my_world_size()
	vector = [tx - x, ty - y]
	
	#if smaller world is simulated, we cant edge jump therefore normal vector needed
	if ws < get_world_size():
		return vector
	
	edge_jump_vector = []
	for distance in vector:
		#distance if utilize jump over edge
		if distance > 0:
			edge_jump_vector.append(distance - ws)
		else:
			edge_jump_vector.append(ws + distance)
	
	best_vector = []
	for i in range(2):
		smaller_distance = get_smallest([abs(vector[i]), abs(edge_jump_vector[i])])
		if smaller_distance["index"] == 0:
			best_vector.append(vector[i])
		else:
			best_vector.append(edge_jump_vector[i])

	return best_vector
	
def calc_closest_point(coordinates_list):
	x, y = get_coordinates()
	least_step_amount = get_my_world_size()
	closest_coordinate = None
	for coordinate in coordinates_list:
		best_vector = calc_best_vector(x,y,coordinate[0], coordinate[1])
		total_steps = abs(best_vector[0]) + abs(best_vector[1])
		if total_steps < least_step_amount:
			least_step_amount = total_steps
			closest_coordinate = coordinate
	return (closest_coordinate[0], closest_coordinate[1])	
	

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
		
def set_my_world_size(n):
	global my_world_size
	if n > get_world_size():
		print("Given world_size is too big")
		return
	my_world_size = n
	
def get_my_world_size():
	global my_world_size
	return my_world_size
		
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


		