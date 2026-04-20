from __builtins__ import *
from tools import *

current_y_direction = ""
next_direction = ""
my_world_size = get_world_size()

def toggle_dir(direction):
	if direction == North:
		return South
	elif direction == South:
		return North		
	elif direction == West:
		return East
	elif direction == East:
		return West 
		
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



############################## GETTER/SETTER ###############################

def get_current_y_direction():
	global current_y_direction
	return current_y_direction

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
	set_my_world_size_tool()
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

############################## QOL Functions ###############################
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
		