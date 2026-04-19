from __builtins__ import *
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
		