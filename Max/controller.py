from tools import *
from harvestModes import *
from movement import *

harvest_mode = "tree_harvest"
harvest_modes = {
	"tree_harvest": tree_harvest,
	"pumpkin_harvest": pumpkin_harvest
}
current_program = ""

def start_program(str_program):
	global current_program
	if str_program not in programs:
		print("invalid programm")
		return
	current_program = str_program
	programs[str_program]()
	
def default_program():
	create_pumpkin_plan()
	reset_default_movement()
	while(num_items(Items.Power) > 1000):
		#default value for harvest_mode
		set_harvest_mode("tree_harvest")
		 	
		pumpkin = get_pumpkin_nr_below()
		if pumpkin != None:
			set_harvest_mode("pumpkin_harvest")
			set_last_checked_pumpkin(pumpkin)	
		
		execute_harvest()
		default_movement()
	sunflower_rush_program(1)

def pumpkin_program():
	create_pumpkin_plan()
	pp = get_pumpkin_plan()
	reset_default_movement()
	
	while(get_current_program() == "pp"):
		current_pumpkin = get_pumpkin_nr_below()
		last_checked = get_last_checked_pumpkin()
		#if we enter a new pumpkin and there is no entry_point entry make entry for entry_point
		if current_pumpkin != None and current_pumpkin != last_checked:
			entry_point = pp["pumpkins"][current_pumpkin]["entry_point"]
			if entry_point == None:
				set_entry_point(current_pumpkin)
			
		if current_pumpkin != None:
			pumpkin_production(pp, current_pumpkin)
			set_last_checked_pumpkin(current_pumpkin)
			default_movement()
		else:
			default_movement()
			
def sunflower_rush_program():
	while(get_current_program == "sr"):
		reset_sunflower_dict()
		plant_sunflower_field()
		sunflower_harvest_clean()
		n -= 1

def execute_harvest():
	harvest_modes[harvest_mode]()

def set_harvest_mode(hm):
	global harvest_mode
	global harvest_modes
	if hm not in harvest_modes:
		print("invalid harvest_mode")
		return
	harvest_mode = hm
	
def get_harvest_mode():
	global harvest_mode
	return	harvest_mode
	
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
	"default": default_program,
	"sr": sunflower_rush_program,
	"pp": pumpkin_program
}