from __builtins__ import *
from mapper import *
from utils import *
from movement import *

def plant_grass():
	if can_harvest():
		harvest()
	if (get_pos_y() + get_pos_x()) % 2 == 0:
		turn_grass()

def plant_tree():
	if can_harvest():
		harvest()
	if (get_pos_y() + get_pos_x()) % 2 == 1:
		plant(Entities.Tree)

def plant_carrot():
	if can_harvest():
		harvest()
	if (get_pos_y() + get_pos_x()) % 2 == 0:
		turn_soil()
		plant(Entities.Carrot)

def plant_pumpkin():
	clear()
	pumpkin_last_checked_dict = {
		"pumpkin_coord_list":[]
	}

	for per_tile_on_map in range((get_resized_world_x() * get_resized_world_y())):
		if get_resized_world_x() * get_resized_world_y() <= 36:
			use_item(Items.Water, 4)
		turn_soil()
		plant(Entities.Pumpkin)
		next_move()

	reset_drone()

	#Adding waiting for small fields to grow
	harvestable = False
	while not harvestable:
		if can_harvest() or get_entity_type() == Entities.Dead_Pumpkin:
			harvestable = True

	#check every pumpkin
	for per_tile_on_map in range((get_resized_world_x() * get_resized_world_y())):
		if get_entity_type() == Entities.Dead_Pumpkin:
			pumpkin_last_checked_dict["pumpkin_coord_list"].append(location())
			harvest()
			plant(Entities.Pumpkin)
		next_move()

	#loop through list until empty
	while len(pumpkin_last_checked_dict["pumpkin_coord_list"]) > 0:
		x_cord, y_cord = pumpkin_last_checked_dict["pumpkin_coord_list"][0]
		move_to_xy(x_cord, y_cord)

		# pop if location not dead on check
		if get_entity_type() == Entities.Pumpkin and can_harvest():
			pumpkin_last_checked_dict["pumpkin_coord_list"].pop(0)

		elif get_entity_type() == Entities.Dead_Pumpkin:
			harvest()
			plant(Entities.Pumpkin)

			#pop and add location at end of list to recheck later
			pumpkin_last_checked_dict["pumpkin_coord_list"].pop(0)
			pumpkin_last_checked_dict["pumpkin_coord_list"].append(location())

			#watering to speed up grow speed
			#this should keep it between 0.74 and 0.99 (watering it to 0.99 if value is 0.74)
			#<0.75 to not hit 0 (throws an error)
			if len(pumpkin_last_checked_dict["pumpkin_coord_list"]) <= 3:
				if len(pumpkin_last_checked_dict["pumpkin_coord_list"]) > 0:
					if get_water() < 0.75:
						use_item(Items.Water, ((1 - get_water()) // 0.25))

		else:#in case it's still growing (likely to happen towards the end, 1-3 pumpkins left)
			pumpkin_last_checked_dict["pumpkin_coord_list"].pop(0)
			pumpkin_last_checked_dict["pumpkin_coord_list"].append(location())

	#reset to initialize other programs with correct values
	reset_drone()
	print("It's about time!")
	harvest()

def plant_sunflower():
	clear()
	sunflower_dict = {}
	for petal_amount in range(7, 16):  # Dicts to store coordinates based on petal amount
		sunflower_dict[petal_amount] = []

	for per_tile_on_map in range((get_resized_world_x() * get_resized_world_y())):
		turn_soil()
		plant(Entities.Sunflower)
		petal_count = measure()
		sunflower_dict[petal_count].append([get_pos_x(), get_pos_y()]) #Adds coordinate in list
		next_move()
	for list_number in range(15, 6, -1): #loop for each list in sunflower_dict
		if list_number % 2 == 0: #Swap harvest direction (start to end, end to start, start to end etc.)
			index = -1
		else:
			index = 0
		for sunflower_len_list in sunflower_dict[list_number]:
			cord_x, cord_y = sunflower_dict[list_number][index]
			move_to_xy(cord_x, cord_y)
			harvest()
			if index >= 0:
				index += 1
			else:
				index -= 1

def infest_field():
	reset_drone()
	for per_tile_on_map in range(get_resized_world_x() * get_resized_world_y()):
		use_item(Items.Fertilizer)
		harvest()
		next_move()
	reset_drone()