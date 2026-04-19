from tools import *
from harvestModes import *
harvest_mode = "tree_harvest"
harvest_modes = {
	"pumpkin_plant_dumb": pumpkin_plant_dumb,
	"tree_harvest": tree_harvest,
	"pumpkin_harvest": pumpkin_harvest
}

def set_harvest_mode():
	global harvest_mode
	global harvest_modes
	
	#default value for harvest_mode
	harvest_mode = "tree_harvest"
	
	pumpkin = get_pumpkin_nr_below()
	if pumpkin != "":
		harvest_mode = "pumpkin_harvest"
		set_last_checked_pumpkin(pumpkin)	

	
def execute_harvest():
	harvest_modes[harvest_mode]()