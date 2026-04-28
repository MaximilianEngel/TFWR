from __builtins__ import *
from mapper import *
from utils import *
from movement import *

def plant_grass():
    if can_harvest():
        harvest()
    if (get_pos_y() + get_pos_x()) % 2 == 0:
        turn_grass()

def plant_tree():
    if can_harvest():
        harvest()
    if (get_pos_y() + get_pos_x()) % 2 == 1:
        plant(Entities.Tree)

def plant_carrot():
    if can_harvest():
        harvest()
    if (get_pos_y() + get_pos_x()) % 2 == 0:
        turn_soil()
        plant(Entities.Carrot)

def plant_pumpkin():
    harvest()
    turn_soil()
    plant(Entities.Pumpkin)

def plant_sunflower():
    clear()
    sunflower_dict = {}
    for petal_amount in range(7, 16):  # Dicts to store coordinates based on petal amount
        sunflower_dict[petal_amount] = []

    for step_count_moving_x in range((get_resized_world_x() * get_resized_world_y())):
        turn_soil()
        plant(Entities.Sunflower)
        petal_count = measure()
        sunflower_dict[petal_count].append([get_pos_x(), get_pos_y()]) #Adds coordinate in list
        next_move()
    for list_number in range(15, 6, -1): #loop for each list in sunflower_dict
        if list_number % 2 == 0: #Swap harvest direction (start to end, end to start, start to end etc.)
            index = -1
        else:
            index = 0
        for sunflower_len_list in sunflower_dict[list_number]:
            cord_x, cord_y = sunflower_dict[list_number][index]
            move_to_xy(cord_x, cord_y)
            harvest()
            if index >= 0:
                index += 1
            else:
                index -= 1

def infest_field():
    move_to_xy(0,0)
    set_x_dir(West)
    set_y_dir(North)
    for steps_for_each_tile in range(get_resized_world_x() * get_resized_world_y()):
        use_item(Items.Fertilizer)
        harvest()
        next_move()
    move_to_xy(0,0)
    set_x_dir(West)
    set_y_dir(North)