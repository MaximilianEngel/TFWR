from __builtins__ import *
from P1_Grass_1 import plant_grass_1
from P4_Sunflower_1 import plant_sun_1
from P4_Sunflower_2 import plant_sun_2
from P2_Carrot_1 import plant_carrot_1
from P3_Pumpkin_1 import plant_pumpkin_1

while True:
	move(East)
	if get_pos_x() in [0, 1]:
		plant_grass_1()
	elif get_pos_x() == 2:
		plant_sun_1()
	elif get_pos_x() == 3:
		plant_sun_2()
	elif get_pos_x() in [4, 5]:
		plant_carrot_1()
	elif get_pos_x() in [10, 11, 12, 13, 14, 15]:
		plant_pumpkin_1()