from __builtins__ import *

def plant_carrot_1():
	for i in range(get_world_size()):
		if can_harvest():
			harvest()
		if get_ground_type() != Grounds.Soil:
				till()
		plant(Entities.Carrot)
		move(North)