from tools import *

my_world_size = get_world_size()
free_spaces = None
blocked_fields = set()


def toggle_dir(direction):
	toggle_map = {
		North: South,
		South: North,
		West: East,
		East: West
	}
	return toggle_map[direction]
	
#a -> x-coordinate start_point ; b -> y-coordinate start_point 
def in_square_boundries(position=get_coordinates(), a=0, b=0, range=get_my_world_size()):
	x, y = position
	return a <= x < a + range and b <= y < b + range
	
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

def calc_best_vector(x, y, tx, ty, enable_jump=True):
	ws = get_my_world_size()
	vector = [tx - x, ty - y]
	
	#if smaller world is simulated, we cant edge jump therefore normal vector needed
	if not enable_jump or ws < get_world_size():
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
	

def create_corner_map(n):
	corner_map = {
		(0,0) : (South, West),
		(0,n-1) : (North, West),
		(n-1,0) : (South, East),
		(n-1,n-1): (North, East)
	}
	return corner_map
	
def point_reflect(coor):
	ws = get_my_world_size()
	x_refl = (ws - 1) - coor[0]
	y_refl = (ws - 1) - coor[1]
	return (x_refl,y_refl)
	
def axis_mirror(coor, axis):
	x, y = coor
	ws = get_my_world_size()
	if axis == "x":
		y_mirror = (ws - 1) - y
		return (x, y_mirror)
	
	elif axis == "y":
		x_mirror = (ws - 1) - x
		return (x_mirror, y)
		
	else:
		print("unknown axis: axis_mirror()")
		return None
		
def create_board_map(x_start, y_start, x_size, y_size):
	board_map = {}
	for i in range(x_size):
		for j in range(y_size):
			board_map[i + x_start,j + y_start] = None
	return board_map

def create_space_column_map(x_start, y_start, x_size, y_size):
	column_map = {}
	for i in range(x_size):
		column_map[i+x_start] = set()
		for j in range(y_size):
			column_map[i+x_start].add(j + y_start)
	return column_map
	
def set_my_world_size(n):
	global my_world_size
	if n > get_world_size():
		print("Given world_size is too big")
		return
	my_world_size = n
	
def get_my_world_size():
	global my_world_size
	return my_world_size
	
def get_coordinates():
	return (get_pos_x(),get_pos_y())
	
def reset_free_spaces():
	global free_spaces
	free_spaces = create_space_column_map(0, 0, get_my_world_size(), get_my_world_size())
	
def reset_blocked_fields():
	blocked_fields = set()

def get_free_spaces():
	global free_spaces
	return free_spaces
	
def get_blocked_fields():
	global blocked_fields
	return blocked_fields
	
def block_field(coor):
	global blocked_fields
	blocked_fields.add(coor)
	x,y = coor
	free_spaces[x].remove(y)
	