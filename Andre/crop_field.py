from __builtins__ import *
from utils import turn_soil
from utils import turn_grass

def plant_grass():
	for i in range(get_world_size()):
		turn_grass()
		if can_harvest():
			harvest()
			if (get_pos_y() + get_pos_x()) % 2 == 1:
				plant(Entities.Tree)
		move(North)

def plant_carrot():
	for i in range(get_world_size()):
		if can_harvest():
			harvest()
			if (get_pos_y() + get_pos_x()) % 2 == 0:
				turn_soil()
		if (get_pos_y() + get_pos_x()) % 2 == 0:
			plant(Entities.Carrot)
		elif (get_pos_y() + get_pos_x()) % 2 == 1:
			plant(Entities.Tree)
		move(North)

def plant_pumpkin():
	for i in range(get_world_size()):
		harvest()
		turn_soil()
		plant(Entities.Pumpkin)
		move(North)

def plant_sunflower():
	clear()
	sunflower_dict = {}
	for petal_amount in range(7, 16):  # Dicts for coordinates later
		sunflower_dict[petal_amount] = []

	for _ in range(get_world_size() / 2):
		for StepCount in range(get_world_size(), 0, -1):
			turn_soil()
			plant(Entities.Sunflower)
			petal_count = measure()
			sunflower_dict[petal_count].append([get_pos_x(), get_pos_y()])
			if StepCount != 1:
				move(North)
			else:
				move(East)
		for StepCount in range(get_world_size(), 0, -1):
			turn_soil()
			plant(Entities.Sunflower)
			petal_count = measure()
			sunflower_dict[petal_count].append([get_pos_x(), get_pos_y()])
			if StepCount != 1:
				move(South)
			else:
				move(East)
	for list_number in range(15, 6, -1):
		if list_number % 2 == 0:
			index = -1
		else:
			index = 0
		for sunflower_len_list in sunflower_dict[list_number]:
			cord_x, cord_y = sunflower_dict[list_number][index]
			move_x = get_pos_x() - cord_x
			if move_x < 0:
				for _ in range(abs(move_x)):
					move(East)
			if move_x > 0:
				for _ in range(abs(move_x)):
					move(West)
			move_y = get_pos_y() - cord_y
			if move_y < 0:
				for _ in range(abs(move_y)):
					move(North)
			if move_y > 0:
				for _ in range(abs(move_y)):
					move(South)
			harvest()
			if index >= 0:
				index += 1
			else:
				index -= 1