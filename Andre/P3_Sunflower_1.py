from __builtins__ import *

def plant_sun_1():
	for i in range(get_world_size()):
		if can_harvest():
			harvest()
			if get_pos_y() % 2 == 0 and get_ground_type() != Grounds.Soil:
				till()
		if get_pos_y() % 2 == 0:
			plant(Entities.Sunflower)
		else:
			plant(Entities.Tree)
		move(North)