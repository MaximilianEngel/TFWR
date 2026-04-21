from __builtins__ import *

my_world_size_tool = get_world_size()

def toggle(options, value):
	x,y = options
	if value == x:
		return y
	elif value == y:
		return x

def toggle_binary(n):
	if n == 0:
		return 1
	elif n == 1:
		return 0
	else:
		print("out of bounds: toggle_binary")

def isEven(n):
	return (n % 2 == 0)
		
def get_coordinates():
	return (get_pos_x(),get_pos_y())

#a -> x-coordinate start_point ; b -> y-coordinate start_point 
def in_square_boundries(a, b, range):
	x, y = get_coordinates()
	return a <= x < a + range and b <= y < b + range

def get_biggest(list):
	biggest = list[0]
	index = 0
	for element in list:
		if element > biggest:
			biggest = element
			index += 1  	
	return {"value": biggest,"index": index}
	
def get_smallest(list):
	smallest = list[0]
	index = 0
	for element in list:
		if element < smallest:
			smallest = element
			index += 1
	return {"value": smallest,"index": index}

def set_my_world_size_tool(ws):
	global my_world_size_tool
	my_world_size_tool = ws

def calc_best_vector(x, y, tx, ty):
	ws = get_my_world_size_tool()
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
	
def get_my_world_size_tool():
	global my_world_size_tool
	return my_world_size_tool 

#returns list: [#possible_fields, remainer]
def calc_possible_fields(field_size, space_between, board_size=get_my_world_size_tool()):
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