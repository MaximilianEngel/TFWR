from __builtins__ import *
from P1_Grass_1 import plant_grass_1
from P1_Grass_2 import plant_grass_2
from P3_Sunflower_1 import plant_sun_1
from P3_Sunflower_2 import plant_sun_2
from P2_Carrot_1 import plant_carrot_1
from P2_Carrot_2 import plant_carrot_2
from P4_Pumpkin import plant_pumpkin_1
from V2_P3_Sunflowerfield import sunflower_field

clear()
while True:
	if num_items(Items.Power) < 60000:
		sunflower_field()

	elif get_pos_x() in [0, 2, 4]:
		plant_grass_1()
	elif get_pos_x() in [1, 3, 5]:
		plant_grass_2()

	elif get_pos_x() in [6, 8, 10, 12, 14]:
		plant_carrot_1()
	elif get_pos_x() in [7, 9, 11, 13, 15]:
		plant_carrot_2()

	elif get_pos_x() in [16, 17, 18, 19, 20, 21]:
		plant_pumpkin_1()
	move(East)