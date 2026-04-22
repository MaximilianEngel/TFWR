from __builtins__ import *
from tools import *
from watering import *
from movement import *
from resource_manager import *
from funFile import dress_properly

gap_filler = "Carrot"
pumpkin_plan = {"pumpkins": {},"last_checked": None}
poly_wish_dict = {}
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

def poly_plant_harvest(entity_pool=[Entities.Carrot, Entities.Bush, Entities.Grass, Entities.Tree]):
	if get_entity_type() != None:
		wait_for_harvest(can_harvest())
	position = get_coordinates()
	wish_dict = get_poly_wish_dict()
	if position in wish_dict:
		poly_entity = wish_dict[position]
		plant_poly_entity(poly_entity)
	else:
		prio_list = get_poly_prio_list()
		bell_distribution = [prio_list[1],prio_list[0],prio_list[2]]
		bell_index = bell_random(len(prio_list))
		if bell_distribution[bell_index] == Items.Wood:
			if isEven(position[1]): # if on even y-coordinates
				plant_poly_entity(Entities.Tree)
			else:
				plant_poly_entity(Entities.Bush)
		
		elif bell_distribution[bell_index] == Items.Hay:
			plant_poly_entity(Entities.Grass)
			
		elif bell_distribution[bell_index] == Items.Carrot:
			plant_poly_entity(Entities.Carrot)
				
		
	
	plant, coor = get_companion()
	add_wish({coor:plant})

def pumpkin_production(current_pumpkin_nr, initial_run): 
	init = initial_run
	position = get_coordinates()
	pumpkin_entry_point = get_entry_point(current_pumpkin_nr)
	harvestable = get_harvestable(current_pumpkin_nr)
	
	if init:
		if get_entity_type() != None:
			dead_pumpkin_below = get_entity_type() == Entities.Dead_Pumpkin
			harvestable = dead_pumpkin_below or can_harvest()
			wait_for_harvest(harvestable)
		soil()
		plant(Entities.Pumpkin)
		return
		
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
		soil()
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
	reset_pumpkin_plan()
	if ps == ws:
		space_between = 0
	field_size = ps + space_between
	
	#possible_pumpkins_per_dimension (pppd)
	pppd, remainer = calc_possible_fields(ps, space_between, ws)
	
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
	
	#remainer pumpkins
	if remainer > 0:
		x_pump, y_pump, re_pumpkin_size, re_remainer = calculate_fields_in_remainer(remainer, space_between, ws)
	
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
	 
def get_poly_wish_dict():
	global poly_wish_dict
	return poly_wish_dict
	
def add_wish(wish):
	global poly_wish_dict
	for key in wish:
		poly_wish_dict[key] = wish[key]
	
def remove_wish(wish):
	global poly_wish_dict
	poly_wish_dict.remove(wish)
	
def reset_wish_dict():
	global poly_wish_dict
	poly_wish_dict = {}

def get_pumpkin_plan():
	global pumpkin_plan
	return pumpkin_plan

def get_pumpkin_nr_below(smart=True):
	pumpkins = get_pumpkin_plan()["pumpkins"]
	key_amount = len(pumpkins)
	key_list = list(range(0, key_amount)) #dumb
	if smart:
		x, y = get_coordinates()
		ws = get_my_world_size()
		if (x > (ws // 2)) and (y > (ws // 2)):
			key_list = list(range(key_amount - 1, -1, -1)) #smart 
	
	for i in key_list:	
		pumpkin = pumpkins[i]
		boundries = pumpkin["boundries"]
		start_coor, end_coor = boundries
		sx, sy = start_coor
		ex, ey = end_coor
		size = ex - sx + 1
		if in_square_boundries(sx, sy, size):
			return i
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

def reset_pumpkin_plan():
	global pumpkin_plan
	pumpkin_plan = {"pumpkins": {},"last_checked": None}

############################## QOL Functions ###############################

def plant_poly_entity(entity):
	if entity == Entities.Carrot:
		soil()
	else:
		unsoil()
		if entity == Entities.Tree:
			#watering()
			pass
	dress_properly(entity)
	plant(entity)

def soil():
	if get_ground_type() != Grounds.Soil:
		till()

def unsoil():
	if get_ground_type() == Grounds.Soil:
		till()

def wait_for_harvest(harvestable):
	if harvestable:
		harvest()
	else:
		print("DAMN WAITING TIME")
		wait_for_harvest(can_harvest())
		
def create_pumpkin_entry(num, pumpkin_size, x, y):
	get_pumpkin_plan()["pumpkins"][num] = {"harvestable": False, "boundries": ((x, y),(x + pumpkin_size - 1, y + pumpkin_size - 1)), "entry_point": None}
	
