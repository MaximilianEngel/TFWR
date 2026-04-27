from __builtins__ import *
from watering import *
from mapper import *
from resource_manager import *
from funFile import dress_properly

gap_filler = "Carrot"

poly_wish_dict = {}

def make_weird_substance(plant_func=None):
	use_item(Items.Fertilizer)
	if plant_func:
		plant_func()
	
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

	
def plant_carrot():
	if(get_ground_type() != Grounds.Soil):
		till()
	plant(Entities.Carrot)
		
def plant_grass():
	if(get_ground_type() == Grounds.Soil):
		till()



############################## GETTER/SETTER ###############################

	 
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
		

