from __builtins__ import *

def plant_grass():
	for i in range(get_world_size()):
		if can_harvest():
			harvest()
		move(North)