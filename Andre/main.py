from __builtins__ import *
from movement import *
from mapper import *
from utils import *
from crop_field import *


set_resized_world_x(12)
set_resized_world_y(12)

if can_harvest():
    while True:
        if num_items(Items.Power) < 60000:
            plant_sunflower()
            clear()
            harvestable = False
            while not harvestable:
                if can_harvest():
                    harvestable = True
            continue
        elif get_pos_x() in range(0, get_resized_world_x() // 2):
            plant_carrot()
        elif get_pos_x() in range((get_resized_world_x() // 2), (get_resized_world_x() + 1)):
            plant_pumpkin()
        plant_tree()
        #if get_resized_world_x() % 2 == 1 and location() == ((get_resized_world_x() - 1),(get_resized_world_y() - 1)):
        #    infest_field()
        #elif get_resized_world_x() % 2 == 0 and location() == ((get_resized_world_x() - 1),0):
        #    infest_field()
        next_move()
