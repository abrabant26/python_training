import random

random_num = random.randint(1,20)
guess = input("Guess the secret number! (Between 1 and 20)\n")

while guess!=random_num:
	if guess < random_num:
		guess = input("Guess a higher number.\n")
	elif guess > random_num:
		guess = input("Guess a lower number.\n")

print("You win! The secret number was " + str(random_num))