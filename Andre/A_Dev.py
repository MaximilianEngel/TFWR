from __builtins__ import *

# destruction prevention for harvest
while True:
	if can_harvest():
		harvest()
		till()
		plant(Entities.Carrot)

	if get_pos_y()==2:
		move(East)

	move(North)