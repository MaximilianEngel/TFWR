from __builtins__ import *
from tools import *
from watering import *
from movement import *

gap_filler = "Carrot"
pumpkin_plan = {"pumpkins": {},"last_checked": None}
sunflower_dict = {}

def tree_harvest():
	global gap_filler
	if can_harvest():
		harvest()
	pos_y = get_pos_y()
	pos_x = get_pos_x()
	is_tree_field = False
	if (isEven(pos_y)):
		if (isEven(pos_x)):
			is_tree_field = True
	elif (not isEven(pos_y)):
		if (not isEven(pos_x)):
			is_tree_field = True
	if is_tree_field:
		plant(Entities.Tree)
		gap_filler = toggle(["Carrot", "Grass"], gap_filler)
		return True
	else:
		if gap_filler == "Carrot":
			plant_carrot()
		elif gap_filler == "Grass":
			plant_grass()
		return False


def pumpkin_production(pumpkin_plan, current_pumpkin_nr): 
	
	position = get_coordinates()
	pumpkin_entry_point = get_entry_point(current_pumpkin_nr)
	harvestable = get_harvestable(current_pumpkin_nr)
	
	#if we made it to the entry_point of checked pumpkin	
	if position == pumpkin_entry_point:
		
		if harvestable and can_harvest():
			harvest()
			set_harvestable(current_pumpkin_nr, False)
			
		elif not harvestable and can_harvest():
			set_harvestable(current_pumpkin_nr, True)
	
	else:
		set_harvestable(current_pumpkin_nr, harvestable and can_harvest())
	
	if get_entity_type() != Entities.Pumpkin:
		if can_harvest():
			wait_for_harvest(can_harvest)
		if get_ground_type() != Grounds.Soil:
			till()
		plant(Entities.Pumpkin)
	
def plant_carrot():
	if(get_ground_type() != Grounds.Soil):
		till()
	plant(Entities.Carrot)
		
def plant_grass():
	if(get_ground_type() == Grounds.Soil):
		till()

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
	reset_default_movement()
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

############################## GETTER/SETTER ###############################

def create_pumpkin_plan(ps=6, space_between=1, ws=get_my_world_size()):
	
	field_size = ps + space_between
	
	#possible_pumpkins_per_dimension (pppd)
	pppd, remainer = calc_possible_fields(ps, space_between, ws)
	
	#remainer pumpkins
	x_pump, y_pump, re_pumpkin_size, re_remainer = calculate_fields_in_remainer(remainer, space_between, ws)
	
	start_points = list(range(0, pppd * field_size, field_size))
	end_point_of_field = (start_points[-1] + field_size - 1) 
	
	coordinates=[]
	for i in start_points:
		for j in start_points:
			coordinates.append((i,j))
			
	entry_index = 0
	for start_point in coordinates:
		create_pumpkin_entry(entry_index, ps, start_point[0], start_point[1])
		entry_index += 1

	offset = (end_point_of_field + space_between)
	re_field_size = re_pumpkin_size + space_between

	re_start_points_x = list(range(0, x_pump * re_field_size, re_field_size))
	re_start_points_y = list(range(0, y_pump * re_field_size, re_field_size)) 
	
	for start_point in re_start_points_x:
		create_pumpkin_entry(entry_index, re_pumpkin_size, start_point, offset)
		entry_index += 1
		
	for start_point in re_start_points_y:
		create_pumpkin_entry(entry_index, re_pumpkin_size, offset, start_point)
		entry_index += 1
	 
	
def get_pumpkin_plan():
	global pumpkin_plan
	return pumpkin_plan

def get_pumpkin_nr_below():
	pumpkin_plan = get_pumpkin_plan()["pumpkins"]
	for key in pumpkin_plan:
		pumpkin = pumpkin_plan[key]
		boundries = pumpkin["boundries"]
		start_coor, end_coor = boundries
		sx, sy = start_coor
		ex, ey = end_coor
		range = ex - sx + 1
		if in_square_boundries(sx, sy, range):
			return key
	return None

def set_entry_point(pumpkin_nr):
	global pumpkin_plan
	pumpkin_plan["pumpkins"][pumpkin_nr]["entry_point"] = get_coordinates()
	
def get_entry_point(pumpkin_nr):
	global pumpkin_plan
	return pumpkin_plan["pumpkins"][pumpkin_nr]["entry_point"]

def set_harvestable(pumpkin_nr, b):
	global pumpkin_plan
	pumpkin_plan["pumpkins"][pumpkin_nr]["harvestable"] = b
	
def get_harvestable(pumpkin_nr):
	global pumpkin_plan 
	return pumpkin_plan["pumpkins"][pumpkin_nr]["harvestable"]
	
def set_last_checked_pumpkin(n):
	global pumpkin_plan
	pumpkin_plan["last_checked"] = n
	
def get_last_checked_pumpkin():
	pp = get_pumpkin_plan()
	return	pp["last_checked"]

def reset_sunflower_dict():
	global sunflower_dict 
	sunflower_dict = {}
	for petal_count in range(15, 6, -1): 
		sunflower_dict[petal_count] = []

############################## QOL Functions ###############################

def wait_for_harvest(harvestable):
	if harvestable:
		harvest()
	else:
		do_a_flip()
		print("DAMN WAITING TIME")
		wait_for_harvest(can_harvest())
		
def create_pumpkin_entry(num, ps, x, y):
	get_pumpkin_plan()["pumpkins"][num] = {"harvestable": False, "boundries": ((x, y),(x + ps - 1, y + ps - 1)), "entry_point": None}