def watering():
	water = get_water()
	if water < 0.5:
		use_item(Items.Water)