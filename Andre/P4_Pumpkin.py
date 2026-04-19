from __builtins__ import *

def plant_pumpkin_1():
	for i in range(get_world_size()):
		if get_entity_type() == Entities.Pumpkin or get_entity_type() == Entities.Dead_Pumpkin:
			harvest()
		if get_ground_type() != Grounds.Soil:
				till()
		plant(Entities.Pumpkin)
		move(North)