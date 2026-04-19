	
from __builtins__ import *
from movement import better_movement
from watering import *
from harvestModes import *
from controller import *
from tools import *

next_move = North
y_dir = North

set_pumpkin_plan()

while True:
	set_harvest_mode()
	execute_harvest()
	y_dir, next_move = better_movement(y_dir, next_move)