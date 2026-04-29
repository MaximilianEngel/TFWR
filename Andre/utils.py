from __builtins__ import *

pumpkin_yield = 0

def turn_soil():
    if get_ground_type() != Grounds.Soil:
        till()

def turn_grass():
    if get_ground_type() == Grounds.Soil:
        till()

def location():
    position = get_pos_x(), get_pos_y()
    return position

def set_pumpkin_yield():
    global pumpkin_yield
    if get_cost(Unlocks.Pumpkins) == {}:
        pumpkin_yield = 512
    elif get_cost(Unlocks.Pumpkins) == {Items.Carrot:65500000}:
        pumpkin_yield = 256
    elif get_cost(Unlocks.Pumpkins) == {Items.Carrot:16400000}:
        pumpkin_yield = 128
    elif get_cost(Unlocks.Pumpkins) == {Items.Carrot:4100000}:
        pumpkin_yield = 64
    elif get_cost(Unlocks.Pumpkins) == {Items.Carrot:1020000}:
        pumpkin_yield = 32
    elif get_cost(Unlocks.Pumpkins) == {Items.Carrot:256000}:
        pumpkin_yield = 16
    elif get_cost(Unlocks.Pumpkins) == {Items.Carrot:64000}:
        pumpkin_yield = 8
    elif get_cost(Unlocks.Pumpkins) == {Items.Carrot:16000}:
        pumpkin_yield = 4
    elif get_cost(Unlocks.Pumpkins) == {Items.Carrot:4000}:
        pumpkin_yield = 2
    elif get_cost(Unlocks.Pumpkins) == {Items.Carrot:1000}:
        pumpkin_yield = 1

def get_pumpkin_yield():
    global pumpkin_yield
    return pumpkin_yield