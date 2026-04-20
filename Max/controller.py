from tools import *
from harvestModes import *
from movement import *

harvest_mode = "tree_harvest"
harvest_modes = {
	"pumpkin_plant_dumb": pumpkin_plant_dumb,
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
	set_pumpkin_plan()
	reset_default_movement()
	while(num_items(Items.Power) > 1000):
		#default value for harvest_mode
		set_harvest_mode("tree_harvest")
		 	
		pumpkin = get_pumpkin_nr_below()
		if pumpkin != "":
			set_harvest_mode("pumpkin_harvest")
			set_last_checked_pumpkin(pumpkin)	
		
		execute_harvest()
		default_movement()
	sunflower_rush_program(1)

def sunflower_rush_program(n = -1):
	while(n != 0):
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

############################## PROGRAM LIST ###############################
	
programs = {
	"default": default_program,
	"sr": sunflower_rush_program,
}