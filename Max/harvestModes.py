from __builtins__ import *
from tools import *
from watering import *
from movement import *

gap_filler = "Carrot"
pumpkins = {}
last_checked_pumpkin = ""
sunflower_dict = {}

def pumpkin_plant_dumb():
	if get_ground_type() != Grounds.Soil:
		till()
	if can_harvest():
		harvest()
	plant(Entities.Pumpkin)

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

def pumpkin_harvest():
	if get_ground_type() != Grounds.Soil:
		till()
	x,y = get_coordinates()
	pp = get_pumpkin_plan()
	
	
	#if we made it to the start_point of checked pumpkin
	pumpkin = pp[get_last_checked_pumpkin()]
	start_x, start_y = pumpkin["boundries"][0]
	
	if x == start_x and y == start_y:
		
		if pumpkin["harvestable"] and can_harvest():
			harvest()
			pumpkin["harvestable"] = False
			
		elif not pumpkin["harvestable"] and can_harvest():
			pumpkin["harvestable"] = True
	
	else:
		pumpkin["harvestable"] = pumpkin["harvestable"] and can_harvest()
	
	if get_entity_type() != Entities.Pumpkin:
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


############################## GETTER/SETTER ###############################
		
def set_pumpkin_plan(ps=6):
	global pumpkins
	pumpkins = {}
	border = get_my_world_size() - ps
	start_a = (0,0)
	start_b = (0, border)
	start_c = (border, 0)
	start_d = (border, border)

	
	i = 0
	for start in [start_a, start_b, start_c, start_d]:
		pumpkins["pumpkin_" + str(i)] = {"harvestable": False, "boundries": ((start[0], start[1]),(start[0] + ps - 1, start[1] + ps - 1))}
		i = i + 1 

def get_pumpkin_plan():
	global pumpkins
	return pumpkins

def get_pumpkin_nr_below():
	pumpkin_plan = get_pumpkin_plan()
	for key in pumpkin_plan:
		pumpkin = pumpkin_plan[key]
		boundries = pumpkin["boundries"]
		start_coor, end_coor = boundries
		sx, sy = start_coor
		ex, ey = end_coor
		range = ex - sx + 1
		if in_square_boundries(sx, sy, range):
			return key
	return ""
	
def set_last_checked_pumpkin(a):
	global last_checked_pumpkin
	last_checked_pumpkin = a
	
def get_last_checked_pumpkin():
	global last_checked_pumpkin
	return	last_checked_pumpkin

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