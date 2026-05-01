from __builtins__ import *
from movement import *
from mapper import *
from utils import *
from crop_field import *


set_resized_world_x(40)
set_resized_world_y(40)

set_desired_sunflowers(86000)
set_desired_pumpkins(27000000)
set_desired_weird_substance(5000000)

clear()
print("Field cleared!")
while True:
    # power farm
    if num_items(Items.Power) < get_desired_sunflowers():
        plant_sunflower()
        continue

    # pumpkin farm
    elif num_items(Items.Pumpkin) < get_desired_pumpkins():
        plant_pumpkin("normal")
        continue

    # weird substance farm
    elif num_items(Items.Weird_Substance) < get_desired_weird_substance():
        plant_pumpkin("infested")
        continue

    else:
        companion_field()
        continue