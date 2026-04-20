from __builtins__ import *

if get_pos_y() == 0 and get_pos_x() == 0:
	clear()
sunflowerDict = {}
for petalamount in range(7, 16): # Dicts for coordinates later
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

for ListNumber in range(15, 6, -1):
	index = 0
	for sunflowerList in sunflowerDict[ListNumber]:
		CordX, CordY = sunflowerList[index]
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
		index += 1
