from __builtins__ import *

def plant_sun_2():
	for i in range(get_world_size()):
		if can_harvest():
			harvest()
			if get_pos_y() % 2 == 1 and get_ground_type() != Grounds.Soil:
				till()
		if get_pos_y() % 2 == 0:
			plant(Entities.Tree)
		else:
			plant(Entities.Sunflower)
		move(North)