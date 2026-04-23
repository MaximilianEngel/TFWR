from tools import *
from movement import *
from harvestModes import *
cactus_column_current = {}
cactus_column_previous = {}


def plant_cactus():
	position = get_coordinates()
	soil()
	plant(Entities.Cactus)
	size = measure()
	add_cactus_to_column(position, size)

def smart_swap():
	x, y = get_coordinates()
	x_dir = get_current_x_direction()
	y_dir = get_current_y_direction()
	swap_coors_general = {
		"y_axis" : {
			North: y-1, 
			South: y+1
		},
		"x_axis" : {
			West: x+1,
			East: x-1
		}
	}
	
	#X-Axis swap coordinate ; Y-Axis swap coordinate
	xsc = swap_coors_general["x_axis"][x_dir]
	ysc = swap_coors_general["y_axis"][y_dir]
	
	c = get_c_row_current()
	p = get_c_row_previous()
	
	c_cac_size = c[(x,y)]
	new_size = swap_helper((xsc, y), p, c_cac_size, y_dir)
	if new_size != c_cac_size:
		c_cac_size = new_size
		swap_helper((x, ysc), c, c_cac_size, x_dir)
		return True
		
	new_size = swap_helper((x, ysc), c, c_cac_size, x_dir)
	if new_size != c_cac_size:
		c_cac_size = new_size
		swap_helper((xsc, y), p, c_cac_size, y_dir)
		return True
		
	return False 

# inputs:
# 	s_c_coor => swap candidate coordinates
# 	s_column => swap column
# 	c_column => current column
# 	c_size => cactus size
# 	dir => direction
# 
# output: cactus size of freshly swapped cactus
def swap_helper(s_c_coor, s_column, c_size, dir):
	if (s_c_coor in s_column) and (s_column[s_c_coor] > c_size):
		swap(toggle_dir(dir))
		temp = s_column[s_c_coor]
		s_column[s_c_coor] = c_size
		c_size = temp	
	return c_size
	
def get_c_row_current():
	global cactus_column_current
	return cactus_column_current
	
def get_c_row_previous():
	global cactus_column_previous
	return cactus_column_previous
	
def add_cactus_to_column(coor, c_size):
	cactus_column_current[coor] = c_size
	
def start_new_column():
	global cactus_column_current
	global cactus_column_previous
	cactus_column_previous = cactus_column_current
	cactus_column_current = {}
	
def reset_c_columns():
	global cactus_column_current
	global cactus_column_previous
	cactus_column_current = {}
	cactus_column_previous = {}