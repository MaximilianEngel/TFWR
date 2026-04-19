def pumpkin_harvest(pk_finished)
if pk_finished == True and can_harvest:
	harvest()
	pk_finished = False
	
	