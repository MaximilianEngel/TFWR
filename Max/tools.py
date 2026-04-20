from __builtins__ import *
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

def calc_best_vector(x, y, tx, ty, world_size=get_my_world_size()):
	ws = world_size
	vector = [tx - x, ty - y]
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