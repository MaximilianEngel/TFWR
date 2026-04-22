hat_for_occasion_map = {
	Entities.Carrot: Hats.Carrot_Hat,
	Entities.Bush: Hats.Green_Hat,
	Entities.Sunflower: Hats.Sunflower_Hat,
	Entities.Grass: Hats.Straw_Hat,
	Entities.Pumpkin: Hats.Pumpkin_Hat,
	Entities.Cactus: Hats.Purple_Hat,
	Entities.Tree: Hats.Tree_Hat
}
def dress_properly(Entity=None):
	global hat_for_occasion_map
	if Entity == None:
		change_hat(Hats.Wizard_Hat)
	else:
		change_hat(hat_for_occasion_map[Entity])