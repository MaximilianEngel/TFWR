from __builtins__ import *
from mapper import *

pumpkin_yield = 0
desired_pumpkins = 0
desired_sunflowers = 0
desired_weird_substance = 0

#################### COMPANION DICTIONARY ####################
companion_dict = {}

def add_to_companion_dict():
    global companion_dict
    companion = get_companion()
    if companion != None:
        companion_dict[(get_companion()[1])] = get_companion()[0]

#################### COORDINATE RELATED ####################

def location():
    position = get_pos_x(), get_pos_y()
    return position

#################### PLANTING RELATED ####################
def properly_water():
    amount = (1 - get_water()) // 0.25
    if amount > 0:
        use_item(Items.Water, amount)

def water_crop(condition = True):
    if condition:
        if get_resized_world_x() * get_resized_world_y() <= 64:
            properly_water()
    else:
        properly_water()

def turn_soil():
    if get_ground_type() != Grounds.Soil:
        till()

def turn_grass():
    if get_ground_type() == Grounds.Soil:
        till()

def wait_until_harvestable():
    harvestable = False
    while not harvestable:
        if can_harvest() or get_entity_type() == Entities.Dead_Pumpkin:
            harvestable = True
        else:
            print("Waiting for crop to grow...")


def plant_crop(crop_type):
    if get_entity_type() != None and get_ground_type() != Entities.Dead_Pumpkin:
        wait_until_harvestable()
    harvest()
    if crop_type == "companion":
        def plant_bush():
            turn_grass()
            plant(Entities.Bush)
        def plant_carrot():
            turn_soil()
            plant(Entities.Carrot)
        def plant_tree():
            turn_grass()
            plant(Entities.Tree)

        hay = num_items(Items.Hay)
        wood = num_items(Items.Wood)
        carrots = num_items(Items.Carrot)

        item_storage = []

        if hay <= wood and hay <= carrots:
            append(item_storage, "tree")
            append(item_storage, "grass")
            append(item_storage, "carrot")

        elif wood <= hay and wood <= carrots:
            append(item_storage, "grass")
            append(item_storage, "tree")
            append(item_storage, "carrot")

        else:
            append(item_storage, "tree")
            append(item_storage, "carrot")
            append(item_storage, "grass")

        def plant_most_needed(most_needed_type):
            most_needed = {
                "tree":plant_tree,
                "grass":turn_grass,
                "carrot":plant_carrot
            }
            most_needed[most_needed_type]()

        im_here = location()
        if im_here in companion_dict:
            companion = companion_dict[im_here]
            which_companion = {
                Entities.Tree:plant_tree,
                Entities.Grass:turn_grass,
                Entities.Carrot:plant_carrot,
                Entities.Bush:plant_bush
            }
            which_companion[companion]()
            quick_print("planted companion", companion)
            companion_dict.pop(im_here)

        else:
            dice = [1, 2, 3, 4, 5, 6]
            bell_curve_value = (((random() * len(dice)) + 1) // 1) + (((random() * len(dice)) + 1) // 1)
            if bell_curve_value <= 4:
                plant_most_needed(item_storage[0])
                quick_print("randomized:", item_storage[0])
            elif 5 <= bell_curve_value <= 9:
                plant_most_needed(item_storage[1])
                quick_print("randomized:", "High Prio", item_storage[1])
            else:
                plant_most_needed(item_storage[2])
                quick_print("randomized:", item_storage[2])

    elif crop_type == "pumpkin":
        turn_soil()
        plant(Entities.Pumpkin)
    elif crop_type == "sunflower":
        turn_soil()
        plant(Entities.Sunflower)
    elif crop_type == "cactus":
        turn_soil()
        plant(Entities.Cactus)
    elif crop_type == "maze":
        plant(Entities.Bush)
        use_item(Items.Weird_Substance)
    elif crop_type == "dinosaur":
        pass
    water_crop()


#################### RESOURCE RELATED ####################

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
    quick_print("Pumpkin yield set!")

def get_pumpkin_yield():
    global pumpkin_yield
    return pumpkin_yield

def set_desired_pumpkins(n):
    global desired_pumpkins
    desired_pumpkins = n

def get_desired_pumpkins():
    global desired_pumpkins
    return desired_pumpkins

def set_desired_sunflowers(n):
    global desired_sunflowers
    desired_sunflowers = n

def get_desired_sunflowers():
    global desired_sunflowers
    return desired_sunflowers

def set_desired_weird_substance(n):
    global desired_weird_substance
    desired_weird_substance = n

def get_desired_weird_substance():
    global desired_weird_substance
    return desired_weird_substance