from __builtins__ import *

def sunflower_field():
	clear()
	sunflowerDict = {}
	for petalamount in range(7, 16):  # Dicts for coordinates later
		sunflowerDict[petalamount] = []

	for _ in range(get_world_size() / 2):
		for StepCount in range(get_world_size(), 0, -1):
			if get_ground_type() != Grounds.Soil:
				till()
			plant(Entities.Sunflower)
			petalcount = measure()
			sunflowerDict[petalcount].append([get_pos_x(), get_pos_y()])
			if StepCount != 1:
				move(North)
			else:
				move(East)
		for StepCount in range(get_world_size(), 0, -1):
			if get_ground_type() != Grounds.Soil:
				till()
			plant(Entities.Sunflower)
			petalcount = measure()
			sunflowerDict[petalcount].append([get_pos_x(), get_pos_y()])
			if StepCount != 1:
				move(South)
			else:
				move(East)
	for list_number in range(15, 6, -1):
		if list_number % 2 == 0:
			index = -1
		else:
			index = 0
		for sunflower_list in sunflowerDict[list_number]:
			CordX, CordY = sunflowerDict[list_number][index]
			MoveX = get_pos_x() - CordX
			if MoveX < 0:
				for _ in range(abs(MoveX)):
					move(East)
			if MoveX > 0:
				for _ in range(abs(MoveX)):
					move(West)
			MoveY = get_pos_y() - CordY
			if MoveY < 0:
				for _ in range(abs(MoveY)):
					move(North)
			if MoveY > 0:
				for _ in range(abs(MoveY)):
					move(South)
			harvest()
			if index >= 0:
				index += 1
			else:
				index -= 1