from tools import *
from harvestModes import *
from coordinator import *
from sunflower_manager import *
from pumpkin_manager import *
from cactus_manager import *
from cactus_manager_adv import *
from mapper import *

current_program = ""

def start_program(str_program):
	global current_program
	change_hat(Hats.Wizard_Hat)
	
	if str_program not in programs:
		print("invalid programm")
		return
	current_program = str_program
	programs[str_program]()

def poly_program():
	reset_default_movement()
	while(get_current_program() == "poly"):
		poly_plant_harvest()
		default_movement()

def cactus_program():
	reset_snake_movement()
	ws = get_my_world_size()
	ws_even = isEven(ws)
	cm = create_corner_map(ws)
	was_swapped = False
	
	checkpoints = initialize_checkpoints(get_coordinates(), ws_even)
	
	while(get_current_program() == "cactus"):
		
		if get_entity_type() != Entities.Cactus:
			soil()
			plant(Entities.Cactus)
		
		was_swapped = swap_cactus()
		if was_swapped:
			for coordinate in checkpoints:
				checkpoints[coordinate] = False
	
		snake_movement()
		position = get_coordinates()
		if position in cm:
			was_harvested = verify_checkpoints(position, checkpoints, ws_even)
			if was_harvested:
				break
				
				
def cactus_program_adv():
	reset_snake_movement()
	reset_cactus_field()
	reset_free_spaces()
	reset_blocked_fields()
	
	initial = True
	first_cactus = True
	end_point = None
	checkpoints = {}

	if isEven(get_my_world_size()):
		end_point = axis_mirror(get_coordinates(), "y")
	else:
		end_point = point_reflect(get_coordinates())
	
	while(get_current_program() == "c_adv"):
		if initial:
			if can_harvest():
				harvest()
			size = plant_cactus()
			add_cactus(size)
			if first_cactus:
				set_biggest_size(size)
				set_smallest_size(size)
				first_cactus = False
			elif size > get_biggest_size():
				set_biggest_size(size)
			elif size < get_smallest_size():
				set_smallest_size(size)
			if get_coordinates() == end_point:
				initial = False
				if isEven(get_my_world_size()):
					checkpoints[point_reflect(end_point)] = False
					checkpoints[end_point] = False
				else:
					checkpoints[axis_mirror(end_point, "y")] = False
					checkpoints[axis_mirror(end_point, "x")] = False
		
		swapped = swap_cactus_adv(size, initial)
		if swapped:
			for cp in checkpoints:
				checkpoints[cp] = False
		
		position = get_coordinates()
		if not initial and position in checkpoints:
			checkpoints[position] = True
			
		finished_cp = 0	
		for cp in checkpoints:
			if checkpoints[cp]:
				finished_cp += 1
				 
		
		if finished_cp == 2:
			harvest()
			return	
		
			
		cactus_movement()
		
def weird_substance_program():
	reset_default_movement()
	
	while(get_current_program() == "weird"):
		make_weird_substance(poly_plant_harvest)
		default_movement()
		harvest()	
			
			
def pumpkin_program():
	reset_default_movement()
	initial_run = True
	initial_point = get_coordinates()
	pumpkin_entities = [Entities.Pumpkin, Entities.Dead_Pumpkin]
	
	create_pumpkin_plan()
	pp = get_pumpkin_plan()
	
	while(get_current_program() == "pump"):
		
		#if we established the field we can just check wether pumpkin beneath us or unsoiled
		if not initial_run:
			if (get_entity_type() not in pumpkin_entities) and (get_ground_type() != Grounds.Soil):
				default_movement()
				continue
				
		current_pumpkin = get_pumpkin_nr_below()
		last_checked = get_last_checked_pumpkin()

		#if we enter a new pumpkin and there is no entry_point entry make entry for entry_point
		if current_pumpkin != None and current_pumpkin != last_checked:
			entry_point = get_entry_point(current_pumpkin)
			if entry_point == None:
				set_entry_point(current_pumpkin)
			
		if current_pumpkin != None:
			pumpkin_production(current_pumpkin, initial_run)
			set_last_checked_pumpkin(current_pumpkin)
		elif initial_run and (get_entity_type() != None):
			wait_for_harvest(can_harvest())
		default_movement()
		
		if get_coordinates() == initial_point:
			initial_run = False 
		
		
def sunflower_rush_program():
	while(get_current_program() == "sr"):
		reset_sunflower_dict()
		plant_sunflower_field()
		sunflower_harvest_clean()

def dino_program():
	change_hat(Hats.Dinosaur_Hat)
	snake_movement()
	while(get_current_program() == "dino"):
		snake_movement()
		


def set_current_programm(cp):
	global current_program
	global programs
	if cp not in programs:
		print("invalid program")
		return
	current_program = cp 
	
def get_current_program():
	global current_program
	return current_program
	
############################## PROGRAM LIST ###############################
	
programs = {
	"sr": sunflower_rush_program,
	"pump": pumpkin_program,
	"poly": poly_program,
	"cactus": cactus_program,
	"c_adv": cactus_program_adv,
	"weird": weird_substance_program,
	"dino": dino_program
}