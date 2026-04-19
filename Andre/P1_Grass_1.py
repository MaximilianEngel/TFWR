from __builtins__ import *

def plant_grass_1():
	for i in range(get_world_size()):
		if can_harvest():
			harvest()
		if get_pos_y() % 2 == 1:
			plant(Entities.Tree)
		move(North)