from __builtins__ import *

resized_world_x = 0
resized_world_y = 0
resized_world_xy = 0

def set_resized_world_x(n):
    global resized_world_x
    resized_world_x = n

def set_resized_world_y(n):
    global resized_world_y
    resized_world_y = n

def get_resized_world_x():
    global resized_world_x
    return resized_world_x

def get_resized_world_y():
    global resized_world_y
    return resized_world_y

def get_resized_world_xy():
    global resized_world_xy
    return resized_world_x, resized_world_y