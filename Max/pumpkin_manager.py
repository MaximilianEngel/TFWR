from coordinator import *
from harvestModes import *

pumpkin_plan = {"pumpkins": {},"last_checked": None}

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

def reset_pumpkin_plan():
	global pumpkin_plan
	pumpkin_plan = {"pumpkins": {},"last_checked": None}
	
def create_pumpkin_entry(num, pumpkin_size, x, y):
	get_pumpkin_plan()["pumpkins"][num] = {"harvestable": False, "boundries": ((x, y),(x + pumpkin_size - 1, y + pumpkin_size - 1)), "entry_point": None}
	