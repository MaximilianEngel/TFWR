from __builtins__ import *

def turn_soil():
	if get_ground_type() != Grounds.Soil:
		till()

def turn_grass():
	if get_ground_type() == Grounds.Soil:
		till()

def location():
	position = get_pos_x(), get_pos_y()
	return position

def move_0():
	for i in range(get_pos_x(), 0, -1):
		move(West)
	for i in range(get_pos_y(), 0, -1):
		move(South)