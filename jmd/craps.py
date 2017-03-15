def die_image(roll):
	if roll == 1:
		print '''
		 ___________
		|           |
		|           |
		|     O     |
		|           |
		|___________|
		'''
	elif roll == 2:
		print '''
		 ___________
		|           |
		|   O       |
		|           |
		|       O   |
		|___________|
		''' 
	elif roll == 3:
		print '''
		 ___________
		|           |
		|   O       |
		|     O     |
		|       O   |
		|___________|
		'''
	elif roll == 4:
		print '''
		 ___________
		|           |
		|   O   O   |
		|           |
		|   O   O   |
		|___________|
		''' 
	elif roll == 5:
		print '''
		 ___________
		|           |
		|   O   O   |
		|     O     |
		|   O   O   |
		|___________|
		''' 
	elif roll == 6:
		print '''
		 ___________
		|           |
		|   O   O   |
		|   O   O   |
		|   O   O   |
		|___________|
		''' 

import random
max_num = 6
min_num = 1

print("\nIt's time to play craps!\n")

#initialize varables
die_1_first = 0
die_2_first = 0
first_total = 0
die_1_second = 0
die_2_second = 0
second_total = 0
num_rolls_first = 0
num_rolls_second = 0
still_playing = 1
rolling_first = 1
rolling_second = 0

while still_playing == 1:
	while rolling_first == 1:
		num_rolls_first += 1
		if num_rolls_first == 1:
			raw_input("Press Enter for the come out\n")
		elif num_rolls_first > 1:
			raw_input("Time for another come out roll!\n")

		#roll first dice for come out
		die_1_first = random.randint(min_num,max_num)
		die_2_first = random.randint(min_num,max_num)
		first_total = die_1_first + die_2_first

		if die_1_first <= die_2_first:
			lower_first = die_1_first
			higher_first = die_2_first
		else:
			lower_first = die_2_first
			higher_first = die_1_first

		die_image(lower_first)
		die_image(higher_first)

		if first_total == 2:
			print "Snake Eyes! You've crapped out! Time for a new shooter."
			still_playing = 0
			rolling_first = 0
		elif first_total == 3 or first_total == 12:
			print "You rolled a %i. You've crapped out! Time for a new shooter." % first_total
			still_playing = 0
			rolling_first = 0
		elif first_total == 7 or first_total == 11:
			print "You rolled a %i. Win!\n" % first_total
		else:
			print "You rolled %i" % first_total
			rolling_second = 1
			rolling_first = 0

			#roll dice more for point rolls
			while rolling_second == 1:
				num_rolls_second += 1
				if num_rolls_second == 1:
					print "Keep rolling until you get a %i or roll a 7 (and lose)!\n" % first_total
				elif num_rolls_second > 1:
					print "Time to roll again. Keep trying to get %i.\nRoll #%i.\n" % (first_total, num_rolls_second)
		
				raw_input("Press enter to continue rolling\n")

				die_1_second = random.randint(min_num,max_num)
				die_2_second = random.randint(min_num,max_num)
				second_total = die_1_second + die_2_second	

				if die_1_second <= die_2_second:
					lower_second = die_1_second
					higher_second = die_2_second
				else:
					lower_second = die_2_second
					higher_second = die_1_second

				die_image(lower_second)
				die_image(higher_second)

				if second_total != 7 and second_total != first_total:
					print "You rolled %i\n" % second_total	
				elif second_total == first_total:
					print "You rolled %i! Win