from __builtins__ import *
from movement import *
from mapper import *
from utils import *
from crop_field import *


set_resized_world_x(4)
set_resized_world_y(4)

desired_sunflowers = 60000
desired_pumpkins = 10000000

if can_harvest():
    while True:
        if num_items(Items.Power) < desired_sunflowers:
            reset_drone()
            plant_sunflower()
            clear()
            harvestable = False
            while not harvestable:
                if can_harvest():
                    harvestable = True
            continue
        elif num_items(Items.Pumpkin) < desired_pumpkins:
            reset_drone()

            #values to remember field size later
            previous_field_size_x = get_resized_world_x()
            previous_field_size_y = get_resized_world_y()

            #calculate missing pumpkins to upgrade cactus yield
            missing_pumpkins = desired_pumpkins - num_items(Items.Pumpkin)
            if missing_pumpkins >= 6 * 6 * 6:
                #calculate required field size so yield matches missing_pumpkins
                #(n * n * 6) / 6 = n * n
                #n * n ** 0.5 = n
                #n ** 0.5 = field size x and y
                # (x + 1) // 1 to turn into int rounding up (int() doesnt work ingame)
                dimensions = ((((missing_pumpkins / 6) ** 0.5) ** 0.5) + 1) // 1
                set_resized_world_x(dimensions)
                set_resized_world_y(dimensions)

            else: #probably never want a smaller field size than 6 anyway
                set_resized_world_x(6)
                set_resized_world_y(6)

            plant_pumpkin()

            #reset to old field size values
            set_resized_world_x(previous_field_size_x)
            set_resized_world_y(previous_field_size_y)
        else:
            plant_carrot()
            plant_tree()
        #if get_resized_world_x() % 2 == 1 and location() == ((get_resized_world_x() - 1),(get_resized_world_y() - 1)):
        #    infest_field()
        #elif get_resized_world_x() % 2 == 0 and location() == ((get_resized_world_x() - 1),0):
        #    infest_field()
        next_move()