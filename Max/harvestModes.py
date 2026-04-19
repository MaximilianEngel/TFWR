from __builtins__ import *
from tools import *
from watering import *

gap_filler = "Carrot"
pumpkins = {}
last_checked_pumpkin = ""

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
	pass
		
def set_pumpkin_plan(ps=6):
	global pumpkins
	pumpkins = {}
	border = get_world_size() - ps
	start_a = (0,0)
	start_b = (0, border)
	start_c = (border, 0)
	start_d = (border, border)
	start_e = (8,0)
	start_f = (0,8)
	start_g = (8,8)
	start_h = (8,16)
	start_i = (16,8)
	
	i = 0
	for start in [start_a, start_b, start_c, start_d, start_e, start_f, start_g, start_h, start_i]:
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