from __builtins__ import *

def plant_bush_2():
	for i in range(get_world_size()):
		if can_harvest():
			harvest()
		if get_pos_y() % 2 == 0:
			plant(Entities.Tree)
		else:
			plant(Entities.Bush)
		move(North)