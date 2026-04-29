from __builtins__ import *
from movement import *
from mapper import *
from utils import *
from crop_field import *


set_resized_world_x(40)
set_resized_world_y(40)

desired_sunflowers = 60000
desired_pumpkins = 14982851

clear()
print("Field cleared!")
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
        set_pumpkin_yield()

        #values to remember field size later
        previous_field_size_x = get_resized_world_x()
        previous_field_size_y = get_resized_world_y()

        missing_pumpkins = desired_pumpkins - num_items(Items.Pumpkin)

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