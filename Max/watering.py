from __builtins__ import *
def watering():
	water = get_water()
	if water < 0.7:
		use_item(Items.Water)