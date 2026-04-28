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