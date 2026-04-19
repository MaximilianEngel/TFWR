from movement import better_movement
from watering import watering
from harvestModes import *
next_move = North
y_dir = North
while(True):
	watering()
	default()
	y_dir, next_move = better_movement(y_dir, next_move)