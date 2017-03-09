import random

MIN_SIDES = 1


def roll():
	max_sides = input('Great! How many sides does the dice have?\n')
	if max_sides <= 0:
		max_sides = input("Try again with a number greater than 0:\n")
	else:	
		roll = random.randint(MIN_SIDES,max_sides)
		guess = raw_input('Would you like to guess what you rolled?\n')
		if guess == 'yes':
			num_guess = input("Guess a number between 1 and " + str(max_sides) + ":\n")
			while num_guess != roll:
				if num_guess > roll:
					num_guess = input('Too High! Try again!\n')
					print ""
				elif num_guess < roll:
					num_guess = input("Try a little higher this time! What's your new guess?\n")

			print("Ding ding ding! You rolled a: " + str(roll))
		else:	
			print('You rolled a: ' + str(roll))


play = raw_input("Hello! Would you like to roll a dice?\n").lower()

if play == "yes":
	roll()
	play_again = raw_input('Do you want to play again? yes or no:\n')
else:
	print "Too bad! Maybe next time!"	

if play == "yes":
	if play_again == "yes":
		roll()
		play_again = raw_input('Do you want to play again? yes or no:\n')
	else:	
		print("See ya!")
