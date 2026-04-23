from __builtins__ import *
from utils import turn_grass
from crop_field import plant_grass
from crop_field import plant_carrot
from crop_field import plant_pumpkin
from crop_field import plant_sunflower

clear()
while True:
	turn_grass()
	if can_harvest():
		while True:
			if num_items(Items.Power) < 50000:
				plant_sunflower()
				clear()
				harvestable = False
				while not harvestable:
					if can_harvest():
						harvestable = True
				continue
			elif get_pos_x() in range(0, 6):
				plant_grass()
			elif get_pos_x() in range(6, 16):
				plant_carrot()
			elif get_pos_x() in range(16, 22):
				plant_pumpkin()
			move(East)