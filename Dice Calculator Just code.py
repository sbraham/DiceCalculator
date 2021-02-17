import random as r

def d6(type_, adv = False):
	dice = [1, 2, 3, 4, 5, 6]
	if type_ == "int":
		if adv == True:
			roll1 = r.choice(dice)
			roll2 = r.choice(dice)
			if roll1 > roll2:
				return roll1
			else:
				return roll2
		else:
			return r.choice(dice)
	elif type_ == "str":
		if adv == True:
			roll1 = r.choice(dice)
			roll2 = r.choice(dice)
			if roll1 == roll2:
				return "d20: " + str(roll1) + " - (same roll)"
			elif roll1 > roll2:
				return "d20: " + str(roll1) + " - (bigger then "+str(roll2)+")"
			else:
				return "d20: " + str(roll2) + " - (bigger then "+str(roll1)+")"
		else:
			return str(r.choice(dice))

def d8(type_, adv = False):
	dice = [1, 2, 3, 4, 5, 6, 7, 8]
	if type_ == "int":
		if adv == True:
			roll1 = r.choice(dice)
			roll2 = r.choice(dice)
			if roll1 > roll2:
				return roll1
			else:
				return roll2
		else:
			return r.choice(dice)
	elif type_ == "str":
		if adv == True:
			roll1 = r.choice(dice)
			roll2 = r.choice(dice)
			if roll1 == roll2:
				return "d20: " + str(roll1) + " - (same roll)"
			elif roll1 > roll2:
				return "d20: " + str(roll1) + " - (bigger then "+str(roll2)+")"
			else:
				return "d20: " + str(roll2) + " - (bigger then "+str(roll1)+")"
		else:
			return str(r.choice(dice))

def d8(type_, adv = False):
	dice = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	if type_ == "int":
		if adv == True:
			roll1 = r.choice(dice)
			roll2 = r.choice(dice)
			if roll1 > roll2:
				return roll1
			else:
				return roll2
		else:
			return r.choice(dice)
	elif type_ == "str":
		if adv == True:
			roll1 = r.choice(dice)
			roll2 = r.choice(dice)
			if roll1 == roll2:
				return "d20: " + str(roll1) + " - (same roll)"
			elif roll1 > roll2:
				return "d20: " + str(roll1) + " - (bigger then "+str(roll2)+")"
			else:
				return "d20: " + str(roll2) + " - (bigger then "+str(roll1)+")"
		else:
			return str(r.choice(dice))

def d20(type_, adv = False):
	dice = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
	if type_ == "int":
		if adv == True:
			roll1 = r.choice(dice)
			roll2 = r.choice(dice)
			if roll1 > roll2:
				return roll1
			else:
				return roll2
		else:
			return r.choice(dice)
	elif type_ == "str":
		if adv == True:
			roll1 = r.choice(dice)
			roll2 = r.choice(dice)
			if roll1 == roll2:
				return "d20: " + str(roll1) + " - (same roll)"
			elif roll1 > roll2:
				return "d20: " + str(roll1) + " - (bigger then "+str(roll2)+")"
			else:
				return "d20: " + str(roll2) + " - (bigger then "+str(roll1)+")"
		else:
			return str(r.choice(dice))

def Vigilance(hands, adv = False, fiend = False):
	attackMod = 8
	damageMod = 4
	if fiend:
		adv = True
		damageMod += d8("int")

	print("Vigilance: ")
	print("Attack - " + str(d20("int", adv = adv)+attackMod))

	if   hands == 1:
		print("Damage - " + str(d8("int")+damageMod+2))
	elif hands == 2:
		print("Damage - " + str(d10("int")+damageMod)) 

def Net(hands = 1, adv = False):
	attackMod = 4
	
	print("Net: ")
	print("Attack - " + str(d20("int", adv = adv)+attackMod))

	print("Damage - Restrained")

def initiative():
	return (d20("int") + d8("int") + 1 + 4)

if True:
	print("initiative: " + str(initiative()))
	print()

if False:
	Vigilance(hands = 1, adv = False, fiend = False)
	print("")
	Vigilance(hands = 1, adv = False, fiend = False)
	if False:
		print("")
		Vigilance(hands = 1, adv = False, fiend = False)
		print("")
		Vigilance(hands = 1, adv = False, fiend = False)

if False:
	print("")
	Net(hands = 1, adv = False)