from tools import *
from harvestModes import *
from movement import *
from sunflower_manager import *
from pumpkin_manager import *
from cactus_manager import *

current_program = ""

def start_program(str_program):
	global current_program
	
	if str_program not in programs:
		print("invalid programm")
		return
	current_program = str_program
	programs[str_program]()

def poly_program():
	while(get_current_program() == "poly"):
		reset_default_movement()
		poly_plant_harvest()
		default_movement()

def cactus_program():
	reset_snake_movement()
	while(get_current_program() == "cactus"):
		if get_entity_type() != Entities.Cactus:
			plant_cactus()
		smart_swap()
		b_next_column = snake_movement()
		if b_next_column:
			start_new_column()
			
		
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
	"cactus": cactus_program
}