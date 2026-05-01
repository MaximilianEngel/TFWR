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

def plant_pumpkin(mode):
    crop_type = "pumpkin"
    if mode == "infested":
        previous_desired_pumpkins = get_desired_pumpkins()
        set_desired_pumpkins(num_items(Items.Pumpkin) + 2000000)
        quick_print("initiated infested pumpkin mode")
        quick_print("desired pumpkins increased!")
    else:
        quick_print("initiated normal pumpkin mode")

    pumpkin_last_checked_dict = {
        "pumpkin_coord_list":[]
    }
    reset_drone()
    set_pumpkin_yield()

    # values to remember field size later
    previous_field_size_x = get_resized_world_x()
    previous_field_size_y = get_resized_world_y()

    missing_pumpkins = get_desired_pumpkins() - num_items(Items.Pumpkin)

    # to figure out how much we get for a 6*6 Pumpkin including yield upgrades
    pumpkin_6_x_6_yield = 216 * get_pumpkin_yield()

    # yield multi = x * x * max(x, 6)
    # meaning 6 or less is x * x * x
    if missing_pumpkins >= pumpkin_6_x_6_yield:
        float_dimensions = (((missing_pumpkins / 6) / get_pumpkin_yield()) ** 0.5)
    else:
        float_dimensions = (missing_pumpkins / get_pumpkin_yield()) ** (1 / 3)

    # + 1 to cover the loss of rounding down
    dimensions = (float_dimensions + 1) // 1

    set_resized_world_x(dimensions)
    set_resized_world_y(dimensions)
    quick_print("world resized to maximum!")

    for per_tile_on_map in range((get_resized_world_x() * get_resized_world_y())):
        water_crop()
        plant_crop(crop_type)
        if mode == "infested":
            use_item(Items.Fertilizer)
        next_move()

    reset_drone()
    wait_until_harvestable()

    #check every pumpkin
    for per_tile_on_map in range((get_resized_world_x() * get_resized_world_y())):
        if get_entity_type() == Entities.Dead_Pumpkin:
            pumpkin_last_checked_dict["pumpkin_coord_list"].append(location())
            plant_crop(crop_type)
            if mode == "infested":
                use_item(Items.Fertilizer)
        next_move()

    #loop through list until empty
    while len(pumpkin_last_checked_dict["pumpkin_coord_list"]) > 0:
        x_cord, y_cord = pumpkin_last_checked_dict["pumpkin_coord_list"][0]
        move_to_xy(x_cord, y_cord)

        # pop if location not dead on check
        if get_entity_type() == Entities.Pumpkin and can_harvest():
            pumpkin_last_checked_dict["pumpkin_coord_list"].pop(0)

        elif get_entity_type() == Entities.Dead_Pumpkin:
            plant_crop(crop_type)
            if mode == "infested":
                use_item(Items.Fertilizer)

            #pop and add location at end of list to recheck later
            pumpkin_last_checked_dict["pumpkin_coord_list"].pop(0)
            pumpkin_last_checked_dict["pumpkin_coord_list"].append(location())

            #watering to speed up grow speed
            if len(pumpkin_last_checked_dict["pumpkin_coord_list"]) <= 3:
                if len(pumpkin_last_checked_dict["pumpkin_coord_list"]) > 0:
                    water_crop(False)

        else:#in case it's still growing (likely to happen towards the end, 1-3 pumpkins left)
            pumpkin_last_checked_dict["pumpkin_coord_list"].pop(0)
            pumpkin_last_checked_dict["pumpkin_coord_list"].append(location())

    reset_drone()
    print("It's about time!")
    harvest()

    # reset to old field size values
    set_resized_world_x(previous_field_size_x)
    set_resized_world_y(previous_field_size_y)
    quick_print("world resized to previous values!")
    if mode == "infested":
        set_desired_pumpkins(previous_desired_pumpkins)
        quick_print("desired pumpkins reverted to old value!")

def plant_sunflower():
    crop_type = "sunflower"
    reset_drone()
    sunflower_dict = {}
    for petal_amount in range(7, 16):  # Dicts to store coordinates based on petal amount
        sunflower_dict[petal_amount] = []

    for per_tile_on_map in range((get_resized_world_x() * get_resized_world_y())):
        plant_crop(crop_type)
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
            wait_until_harvestable()
            harvest()
            if index >= 0:
                index += 1
            else:
                index -= 1
    reset_drone()

def infest_field():
    reset_drone()
    for per_tile_on_map in range(get_resized_world_x() * get_resized_world_y()):
        use_item(Items.Fertilizer)
        harvest()
        next_move()
    reset_drone()

def companion_field():
    crop_type = "companion"
    reset_drone()
    for per_tile_on_map in range((get_resized_world_x() * get_resized_world_y())):
        plant_crop(crop_type)
        add_to_companion_dict()
        next_move()
    reset_drone()