from __builtins__ import *
from movement import *
from mapper import *
from utils import *
from crop_field import *

def plant_pumpkin_field():
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

	move_to_xy(0,0)
	set_x_dir(West)
	set_y_dir(North)

	#Adding waiting for small fields to grow
	harvestable = False
	while not harvestable:
		if can_harvest():
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
	move_to_xy(0,0)
	set_x_dir(West)
	set_y_dir(North)
	print("It's about time!")
	harvest()