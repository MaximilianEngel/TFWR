from tools import *


def is_power_low():
	b = num_items(Items.Power) < 15000
	return b 

def get_poly_prio_list():
	hay = num_items(Items.Hay)
	wood = num_items(Items.Wood)
	carrots = num_items(Items.Carrot)
	poly_dict = {hay: Items.Hay, wood: Items.Wood, carrots: Items.Carrot}
	sorted_amount = merge_sort([hay, wood, carrots])
	prio_list = []
	for entity_amount in sorted_amount:
		prio_list.append(poly_dict[entity_amount])
	return prio_list