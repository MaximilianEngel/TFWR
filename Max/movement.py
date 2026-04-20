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
	world_smaller = get_my_world_size() < get_world_size()
	x,y = get_coordinates()
	if not world_smaller:
		vector = calc_best_vector(x, y, tx, ty, get_my_world_size())
	else:
		vector = (tx - x, ty - y)
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