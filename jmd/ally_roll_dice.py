import random
max = input('How many sides does the dice have? ')
min = 1
roll = random.randint(min,max)
guess = raw_input('Would you like to make a guess? ')
if guess == 'yes':
	num_guess = input("What's your guess? ")
	while num_guess != roll:
		if num_guess > roll:
			num_guess = input('Too High! Try again! ')
		elif num_guess < roll:
			num_guess = input("Try a little higher this time! What's your new guess? ")	
	print("Ding ding ding! You rolled a: " + str(roll))
else:	
	print('You rolled a: ' + str(roll))

play_again = raw_input('Do you want to play again? yes or no: ')

while play_again == "yes":
	roll = random.randint(min,max)
	guess = raw_input('Would you like to make a guess? ')
	if guess == 'yes':
		num_guess = input("What's your guess? ")
		while num_guess != roll:
			if num_guess > roll:
				num_guess = input('Too High! Try again! ')
			elif num_guess < roll:
				num_guess = input("Try a little higher this time! What's your new guess? ")	
		print("Ding ding ding! You rolled a: " + str(roll))
	else:	
		print('You rolled a: ' + str(roll))
	play_again = raw_input('Do you want to play again? yes or no: ')
print("See ya!")
