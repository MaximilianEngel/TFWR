from tools import *
from movement import *
from resource_manager import *
from harvestModes import *

harvest()
soil()
plant(Entities.Cactus)
x = measure()
print(x)
