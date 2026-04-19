from __builtins__ import *
def toggle(options, value):
	x,y = options
	if value == x:
		return y
	elif value == y:
		return x