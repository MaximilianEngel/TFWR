from __builtins__ import *
from Plant_Grass import plant_grass
from Plant_Bush import plant_bush
from Plant_Bush_2 import plant_bush_2
from Plant_Carrot import plant_carrot
from Plant_Pumpkin import plant_pumpkin

while True:
	move(East)
	if get_pos_x() in [0, 1]:
		plant_grass()
	elif get_pos_x() == 2:
		plant_bush()
	elif get_pos_x() == 3:
		plant_bush_2()
	elif get_pos_x() in [4, 5]:
		plant_carrot()
	elif get_pos_x() in [10, 11, 12, 13, 14, 15]:
		plant_pumpkin()