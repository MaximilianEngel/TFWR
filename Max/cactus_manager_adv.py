from tools import *
from harvestModes import *

blocked_fields = set()
h_prio_fields = set()
l_prio_fields = set()
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
smallest_size = 9

def plant_cactus():
	soil()
	plant(Entities.Cactus)
	size = measure()
	if size > get_biggest_size():
		set_biggest_size(size) 
	add_cactus(size)
	swap_cactus(size)
	
def swap_cactus(size_self):
	swapped_horizontal = swap_cactus_helper(East)
	swapped_vertical = swap_cactus_helper(North)
	
	
	
def swap_cactus_helper(dir):
	
	x,y = get_coordinates()
	bs = get_biggest_size()
	ss = get_smallest_size()
	blocked = get_blocked_fields()
	h_prio_fields = get_h_prio_fields()
	l_prio_fields = get_l_prio_fields()
	cs_ahead = measure(dir)
	cs_behind = measure(toggle_dir(dir))
	cs_self = measure()
	
	#If cactus is in fixed position ignore it
	if dir == East:
		if (x+1,y) in blocked:
			cs_ahead = None
		if (x-1,y) in blocked:
			cs_behind = None

	if dir == North:
		if (x,y+1) in blocked:
			cs_ahead = None
		if (x,y-1) in blocked:
			cs_behind = None 
	
	#Swap cactus logic 
	if cs_behind != None and cs_behind > cs_self:
		swap(toggle_dir(dir))
		temp = cs_self
		cs_self = cs_behind
		cs_behind = temp
		
	if cs_ahead != None and cs_ahead < cs_self:
		swap(dir)
		temp = cs_self
		cs_self = cs_ahead
		cs_ahead = temp
	
	#Dicide if position of cacti can be permanently set
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
	
def get_blocked_fields():
	global blocked_fields
	return blocked_fields
	
def get_h_prio_fields():
	global h_prio_fields
	return h_prio_fields
	
def get_l_prio_fields():
	global l_prio_fields
	return l_prio_fields
	
def field_fixed(coor, size):
	global blocked_fields
	global cactus_amount_per_size
	global prio_fields
	global biggest_size
	global smallest_size 
	
	x, y = coor
	prio_fields.remove(coor)
	blocked_fields.add(coor)
	
	decide_prio_field(x - 1, y)
	decide_prio_field(x, y - 1)
	decide_prio_field(x + 1, y)
	decide_prio_field(x, y + 1)
	
	cactus_amount_per_size[size] -= 1
	if cactus_amount_per_size[size] == 0:
		if size == biggest_size:
			biggest_size -= 1
		elif size == smallest_size:
			smallest_size += 1
		
def decide_prio_field(x,y):
	global h_prio_fields
	global l_prio_fields
	global blocked_fields
	
	h_prio_allowed = False
	l_prio_allowed = False
	
	if x + 1 > get_my_world_size() or y + 1 > get_my_world_size():
		h_prio_allowed = True
		
	elif ((x + 1, y) in blocked_fields) or ((x, y + 1) in blocked_fields):
		h_prio_allowed = True
		
	elif x - 1 < get_my_world_size() or y - 1 < get_my_world_size():
		l_prio_allowed = True
		
	elif ((x - 1, y) in blocked_fields) or ((x, y - 1) in blocked_fields):
		l_prio_allowed = True
	
	if h_prio_allowed:
		h_prio_fields.add((x,y))
		
	elif l_prio_allowed:
		l_prio_fields.add((x,y))

def reset_cactus_field():
	global blocked_fields
	global cactus_amount_per_size
	global biggest_size
	global smallest_size 
	global h_prio_fields
	global l_prio_fields
	blocked_fields = set()
	h_prio_fields = set()
	l_prio_fields = set()
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
	smallest_size = 9