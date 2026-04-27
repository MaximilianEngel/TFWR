from tools import *
from harvestModes import *
from mapper import *

h_prio_fields = {(get_my_world_size()-1, get_my_world_size()-1)}
l_prio_fields = {(0,0)}
check_list = list(range(get_my_world_size()-1, -1, -1))
cactus_amount_per_size = {
	0: 0,
	1: 0,
	2: 0,
	3: 0,
	4: 0,
	5: 0,
	6: 0,
	7: 0,
	8: 0,
	9: 0
}
biggest_size = 0
smallest_size = 0

def plant_cactus():
	if get_entity_type() == Entities.Cactus:
		return None
	soil()
	plant(Entities.Cactus)
	size = measure()
	return size
	
	
def swap_cactus_adv(size_self, initial):
	swapped_horizontal = swap_cactus_helper(East, initial)
	swapped_vertical = swap_cactus_helper(North, initial)
	return swapped_horizontal or swapped_vertical
	
def swap_cactus_helper(dir, initial):
	x,y = get_coordinates()
	bs = get_biggest_size()
	ss = get_smallest_size()
	blocked = get_blocked_fields()
	h_prio_fields = get_h_prio_fields()
	l_prio_fields = get_l_prio_fields()
	cs_ahead = measure(dir)
	cs_behind = measure(toggle_dir(dir))
	cs_self = measure()
	swapped = False
	#If cactus is in fixed position ignore it
	if dir == East:
		if (x+1,y) in blocked:
			cs_ahead = None
		if (x-1,y) in blocked:
			cs_behind = None

	elif dir == North:
		if (x,y+1) in blocked:
			cs_ahead = None
		if (x,y-1) in blocked:
			cs_behind = None 
	
	#Swap cactus logic 
	if cs_behind != None and cs_behind > cs_self:
		swap(toggle_dir(dir))
		swapped = True
		temp = cs_self
		cs_self = cs_behind
		cs_behind = temp
		
	if cs_ahead != None and cs_ahead < cs_self:
		swap(dir)
		swapped = True
		temp = cs_self
		cs_self = cs_ahead
		cs_ahead = temp
	
	if initial:
		return swapped
	
	#Decide if position of cacti can be permanently set
	if dir == East:
		if cs_ahead == bs and (x+1,y) in h_prio_fields:
			field_fixed((x+1,y), cs_ahead)
		
		if cs_behind == ss and (x-1,y) in l_prio_fields:
			field_fixed((x-1, y), cs_behind)
		
		if cs_self == bs and (x,y) in h_prio_fields:
			field_fixed((x,y), cs_self)
		
		elif cs_self == ss and (x,y) in l_prio_fields:
			field_fixed((x,y), cs_self)
	
	elif dir == North:
		if cs_ahead == bs and (x,y+1) in h_prio_fields:
			field_fixed((x,y+1), cs_ahead)
			
		if cs_behind == ss and (x,y-1) in l_prio_fields:
			field_fixed((x, y-1), cs_behind)
			
		if cs_self == bs and (x,y) in h_prio_fields:
			field_fixed((x,y), cs_self)
			
		elif cs_self == ss and (x,y) in l_prio_fields:
			field_fixed((x,y), cs_self)
			
	return swapped 

def get_biggest_size():
	global biggest_size
	return biggest_size
	
def set_biggest_size(n):
	global biggest_size
	biggest_size = n
	
def get_smallest_size():
	global smallest_size
	return smallest_size
	
def set_smallest_size(n):
	global smallest_size
	smallest_size = n	
	
def add_cactus(size):
	global cactus_amount_per_size
	cactus_amount_per_size[size] += 1
	
def get_h_prio_fields():
	global h_prio_fields
	return h_prio_fields
	
def get_l_prio_fields():
	global l_prio_fields
	return l_prio_fields
	
def field_fixed(coor, size):
	global blocked_fields
	global l_prio_fields
	global h_prio_fields
	global biggest_size
	global smallest_size 
	cps_dict = get_cactus_amount_per_size()
	x, y = coor
	if coor in h_prio_fields:
		h_prio_fields.remove(coor)
	elif coor in l_prio_fields:
		l_prio_fields.remove(coor)
	
	block_field(coor)
	
	decide_prio_field(x - 1, y)
	decide_prio_field(x, y - 1)
	decide_prio_field(x + 1, y)
	decide_prio_field(x, y + 1)

	use_cactus(size)
	if cactus_amount_per_size[size] == 0:
		if size == biggest_size:
			biggest_size -= 1
		elif size == smallest_size:
			smallest_size += 1
		
def decide_prio_field(x,y):
	global h_prio_fields
	global l_prio_fields
	blocked_fields = get_blocked_fields()
	ws = get_my_world_size()
	point_zero = (0,0)
	max_value = ws - 1
	h_prio_allowed = False
	l_prio_allowed = False
	
	#If out of bounds or already blocked, cant be prio field
	if not in_square_boundries((x,y)) or (x, y) in blocked_fields:
		return
	
	#Field diagonal must be unlocked
	if (ws - 2 <= x + y and x + y <= ws):
		return
	
	if x + 1 > max_value or y + 1 > max_value:
		h_prio_allowed = True
		
	elif ((x + 1, y) in blocked_fields) and ((x, y + 1) in blocked_fields):
		h_prio_allowed = True
		
	elif x - 1 < point_zero[0] or y - 1 < point_zero[0]:
		l_prio_allowed = True
		
	elif ((x - 1, y) in blocked_fields) and ((x, y - 1) in blocked_fields):
		l_prio_allowed = True
	
	if h_prio_allowed:
		h_prio_fields.add((x,y))
		
	elif l_prio_allowed:
		l_prio_fields.add((x,y))

def reset_cactus_field():
	global cactus_amount_per_size
	global biggest_size
	global smallest_size 
	global h_prio_fields
	global l_prio_fields
	h_prio_fields = {(get_my_world_size()-1, get_my_world_size()-1)}
	l_prio_fields = {(0,0)}
	check_list = list(range(get_my_world_size()-1, -1, -1))
	cactus_amount_per_size = {
		0: 0,
		1: 0,
		2: 0,
		3: 0,
		4: 0,
		5: 0,
		6: 0,
		7: 0,
		8: 0,
		9: 0
	}
	biggest_size = None
	smallest_size = None
	
def use_cactus(size):
	global cactus_amount_per_size
	cps = cactus_amount_per_size[size]
	cps -= 1
	cactus_amount_per_size[size] = cps
	
def get_cactus_amount_per_size():
	global cactus_amount_per_size
	return cactus_amount_per_size