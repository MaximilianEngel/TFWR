from __builtins__ import *
def watering(n=0):
	water = get_water()
	if n == 0:
		while water < 0.8:
			use_item(Items.Water)
			water = get_water()
		return
	for _ in range(n):
		water = get_water()
		if water < 0.9:
			use_item(Items.Water)