import random

def get_random(dice, ranges):
	rnd = random.randint(1, dice)
	for minimum, maximum, res in ranges:
		if minimum <= rnd <= maximum:
			return res
	return None


