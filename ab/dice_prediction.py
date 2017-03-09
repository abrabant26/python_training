import random
print "Let's see what a rolled dice is most likely to land on!"
max_sides = input("How many sides does your dice have? ")
if type(max) != int:
	max_sides = input("Try again with a number this time: ")	
min_sides = 1
sample_size = input("How big should our sample size be? ")
if type(sample_size) != int:
	sample_size = input("Nice try. Let's try this again with a number this time: ")

count = 0
total = 0.0
while count < sample_size:
	roll = random.randint(int(min_sides),int(max_sides))
	count += 1
	total += roll
avg = total/sample_size	
print "The average roll of the dice yields a " + str(avg)