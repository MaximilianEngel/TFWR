from __builtins__ import *
def toggle(options, value):
	x,y = options
	if value == x:
		return y
	elif value == y:
		return x
		
def isEven(n):
	return (n % 2 == 0)
		
def get_coordinates():
	return (get_pos_x(),get_pos_y())

#a -> x-coordinate start_point ; b -> y-coordinate start_point 
def in_square_boundries(a, b, range):
	x, y = get_coordinates()
	return a <= x < a + range and b <= y < b + range
		 