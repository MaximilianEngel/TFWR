def default():
	if can_harvest():
		harvest()
	if get_pos_y() % 3 == 0:
		if(get_ground_type() != Grounds.Soil):
			till()
		plant(Entities.Carrot)
	elif get_pos_y() % 3 == 1:
		if(get_ground_type() == Grounds.Soil):
			till()
		plant(Entities.Bush)
	else:
		if(get_ground_type() == Grounds.Soil):
			till()