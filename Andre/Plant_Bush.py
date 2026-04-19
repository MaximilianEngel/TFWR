from __builtins__ import *

def plant_bush():
	for i in range(get_world_size()):
		if can_harvest():
			harvest()
		if get_pos_y() % 2 == 0:
			plant(Entities.Bush)
		else:
			plant(Entities.Tree)
		move(North)