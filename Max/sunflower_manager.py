from tools import *
from coordinator import *

sunflower_dict = {}

def plant_sunflower():
	global sunflower_dict
	harvest()
	if get_ground_type() != Grounds.Soil:
		till()
	plant(Entities.Sunflower)
	petals = measure()
	sunflower_dict[petals].append(get_coordinates())
	
def plant_sunflower_field():
	field_incomplete = True
	while(field_incomplete):
		plant_sunflower()
		default_movement()
		if get_coordinates() == (0,0):
			field_incomplete = False
		
	
def sunflower_harvest_clean():
	global sunflower_dict 
	for petal_count in range(15, 6, -1):
		for sunflower_coordinates in sunflower_dict[petal_count]:
			tx, ty = sunflower_coordinates
			moveTo(tx, ty)
			wait_for_harvest(can_harvest())
	reset_sunflower_dict()

#Takes too long to compute, but uses least amount of moves
def sunflower_harvest_optimized():
	global sunflower_dict 
	for petal_count in range(15, 6, -1):
		current_list = sunflower_dict[petal_count]
		sunflower_count = len(current_list)
		for _ in range(sunflower_count):
			closest_coordinates = calc_closest_point(current_list) 
			current_list.remove(closest_coordinates)
			tx, ty = closest_coordinates
			moveTo(tx, ty)
			wait_for_harvest(can_harvest())
	reset_sunflower_dict()
	
	
def reset_sunflower_dict():
	global sunflower_dict 
	sunflower_dict = {}
	for petal_count in range(15, 6, -1): 
		sunflower_dict[petal_count] = []