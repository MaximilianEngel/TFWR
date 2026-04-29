from __builtins__ import *
from movement import *
from mapper import *
from utils import *
from crop_field import *


set_resized_world_x(8)
set_resized_world_y(8)

set_desired_sunflowers(72000)
set_desired_pumpkins(16200000)

clear()
print("Field cleared!")
while True:
    if num_items(Items.Power) < get_desired_sunflowers():
        plant_sunflower()
        continue

    elif num_items(Items.Pumpkin) < get_desired_pumpkins():
        plant_pumpkin()
        continue

    else:
        plant_carrot()
        plant_tree()
    #if get_resized_world_x() % 2 == 1 and location() == ((get_resized_world_x() - 1),(get_resized_world_y() - 1)):
    #    infest_field()
    #elif get_resized_world_x() % 2 == 0 and location() == ((get_resized_world_x() - 1),0):
    #    infest_field()
    next_move()