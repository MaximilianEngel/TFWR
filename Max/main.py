from __builtins__ import *
from movement import better_movement
from watering import watering
from harvestModes import *
from tools import *
gap_filler = plant_carrot
next_move = North
y_dir = North
while(True):
	watering()
	tree_planted = tree_harvest(gap_filler)
	if tree_planted:
		gap_filler = toggle([plant_carrot, plant_grass], gap_filler)
	y_dir, next_move = better_movement(y_dir, next_move)