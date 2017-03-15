import random
rolls = input("How many times would you like to roll?\n")
i = 0
total = 0.0

while rolls<1:
	rolls = input("Please enter an actual fucking number you smartass\n")

while (i<rolls):
	dice_roll = random.randint(1,6)
	total += dice_roll
	i+=1

average = total / rolls
print("Average roll: " + str(average))