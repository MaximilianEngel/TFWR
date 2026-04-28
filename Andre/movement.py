from __builtins__ import *
from utils import *
from mapper import *

move_dir_dict = {
    "x_dir":West,
    "y_dir":North
}

def move_to_xy(x,y):
    move_x = x - location()[0]
    move_y = y - location()[1]
    for i in range(abs(move_x)):
        if move_x > 0:
            move(East)
        else:
            move(West)
    for i in range(abs(move_y)):
        if move_y > 0:
            move(North)
        else:
            move(South)

def toggle_x_dir():
    if move_dir_dict["x_dir"] == East:
        move_dir_dict["x_dir"] = West
    elif move_dir_dict["x_dir"] == West:
        move_dir_dict["x_dir"] = East

def toggle_y_dir():
    if move_dir_dict["y_dir"] == North:
        move_dir_dict["y_dir"] = South
    elif move_dir_dict["y_dir"] == South:
        move_dir_dict["y_dir"] = North

def next_move():
    ############################ Y Movement ############################
    if move_dir_dict["y_dir"] == North and location()[1] < (get_resized_world_y() -1):
        move(move_dir_dict["y_dir"])
        return
    elif move_dir_dict["y_dir"] == South and location()[1] > 0:
        move(move_dir_dict["y_dir"])
        return
    if location()[1] == (get_resized_world_y() -1) or location()[1] == 0:
        toggle_y_dir()

    ############################ X Movement ############################
    if location() == (0, (get_resized_world_y() - 1)):
        toggle_x_dir()
        move(move_dir_dict["x_dir"])
    elif get_resized_world_x() % 2 == 0 and location() == ((get_resized_world_x() - 1), 0):
        toggle_x_dir()
        move(move_dir_dict["x_dir"])
    elif get_resized_world_x() % 2 == 1 and location() == ((get_resized_world_x() - 1), (get_resized_world_y() - 1)):
        toggle_x_dir()
        move(move_dir_dict["x_dir"])
    elif location()[1] == (get_resized_world_y() -1) or location()[1] == 0:
        move(move_dir_dict["x_dir"])

def set_x_dir(direction):
    move_dir_dict["x_dir"] = direction

def set_y_dir(direction):
    move_dir_dict["y_dir"] = direction

def reset_drone():
    move_to_xy(0,0)
    set_x_dir(West)
    set_y_dir(North)