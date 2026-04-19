from __builtins__ import *

if get_pos_y() == 0 and get_pos_x() == 0:
	clear()
for _ in range(get_world_size() / 2):
	for StepCount in range(get_world_size(), 0, -1):
		if get_ground_type() != Grounds.Soil:
			till()
		plant(Entities.Sunflower)
		if StepCount != 1:
			move(North)
		else:
			move(East)
	for StepCount in range(get_world_size(), 0, -1):
		if get_ground_type() != Grounds.Soil:
			till()
		plant(Entities.Sunflower)
		if StepCount != 1:
			move(South)
		else:
			move(East)