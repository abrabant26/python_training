random_word = list("hangman")
display_word = []
correct = 1
incorrect = 0
max_strikes = 6

for letter in random_word:
	display_word.append("_")

print " ".join(display_word)
guess = raw_input("Guess a letter!\n")

while correct<len(random_word) and incorrect<max_strikes:
	got_one = 0
	for index,letter in enumerate(random_word):
		if guess==letter:
			display_word[index]=guess+" "
			correct+=1
			got_one = 1
	print "".join(display_word)
	incorrect = incorrect + 1 - got_one
	strikes = max_strikes - incorrect
	guess = raw_input("You have %s strikes left. Guess again!\n" % (strikes))

if incorrect == max_strikes:
	print "You lose! The word was \"" + "".join(random_word) + "\""
elif correct == len(random_word):
	print "You win! The word was \"" + "".join(random_word) + "\""