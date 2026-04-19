from __builtins__ import *
def default():
	if can_harvest():
		harvest()
	if get_pos_y() % 6 == 2:
		if(get_ground_type() != Grounds.Soil):
			till()
		plant(Entities.Carrot)
	elif get_pos_y() % 3 == 1:
		if(get_ground_type() == Grounds.Soil):
			till()
		plant(Entities.Bush)
	else:
		if(get_ground_type() == Grounds.Soil):
			till()
			
def pumpkin_plant_dumb():
	if get_ground_type() != Grounds.Soil:
		till()
	if can_harvest():
		harvest()
	plant(Entities.Pumpkin)

def tree_harvest(gap_fill_plant=plant_grass):
	ws = get_world_size()
	if can_harvest():
		harvest()
	pos_y = get_pos_y()
	pos_x = get_pos_x()
	is_tree_field = False
	for i in range(0, ws, 2):
		if (pos_x % ws == i):
			for j in range(0, ws, 2):
				if (pos_y % ws == j):
					is_tree_field = True
					break
		if (pos_x % ws == i + 1):
			for k in range(0, ws, 2):
				if (pos_y % ws == k + 1):
					is_tree_field = True
					break
	if is_tree_field:
		plant(Entities.Tree)
		return True
	else:
		gap_fill_plant()
		return False

		
def plant_carrot():
	if(get_ground_type() != Grounds.Soil):
		till()
	plant(Entities.Carrot)
		
def plant_grass():
	if(get_ground_type() == Grounds.Soil):
		till()