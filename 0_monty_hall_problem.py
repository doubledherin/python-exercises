import random

def monty_hall_problem():

	doors = ["ZONK!", "ZONK!", "ZONK!"]
	r = random.randint(0, 2)
	doors[r] = "BRAND NEW CAR!"
	
	chosen_door = int(raw_input("Pick a door, 1, 2, or 3: ")) - 1  # subtracting 1 to align this value with "doors" indices

	# helper; same set as the possible values of r or chosen_door
	t = [0,1,2]
	zonk = 5		# initializing
	change = ""		# initializing

	# the winning door was chosen (p = 1/3 )
	if r == chosen_door:
		t.pop(r)
		zonk = random.choice(t)
		t.pop(zonk)
		suggested_door = t.pop()
		
		print "Fair enough. But look at what's behind door number %d ... a zonk!" % (zonk + 1)
		print "Do you want to change your choice to door number %d?" % (suggested_door + 1)
		
		while True:

			change = raw_input("Enter 'y' or 'n': ")
			change = change.lower()

			if change in "yn":
				break
			else:
				continue

		if change == 'y':
			if doors[suggested_door] == "BRAND NEW CAR!":
				print "Congratulations! You won a BRAND NEW CAR!"
				return True
			else:
				print "ZONK! Wah-wah. You should have stayed with your first choice."
				return False
		else:
			print "Congratulations! You won a BRAND NEW CAR!"
			return True
	

	# the winning door was not chosen ( p = 2/3 )
	else:
		
		t.pop(chosen_door)
		suggested_door = t.index(r) 	# will always be the car
		zonk = t[0]		

		print "Fair enough. But look at what's behind door number %d ... a zonk!" % (zonk + 1)
		print "Do you want to change your choice to door number %d?" % (suggested_door + 1)

		while True:

			change = raw_input("Enter 'y' or 'n': ")
			change = change.lower()

			if change in "yn":
				break
			else:
				continue

		if change == 'y':
			print "Congratulations! You won a BRAND NEW CAR!"
			return True
		else:
			print "ZONK! Wah-wah. You should have changed doors."
			return False


def simulation(n):
	wins = 0
	losses = 0
	for i in range(n):
		if monty_hall_problem():
			wins += 1
		else:
			losses += 1
	return "When this simulation was run %d times, there were %d wins and %d losses." % (n, wins, losses)

print simulation(10)
