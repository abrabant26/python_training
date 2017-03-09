import csv
import random



#reads in csv and picks the random word
"""def pick_word():"""
path = '../../../most-common-english-words-csv.csv'
with open(path, 'rb') as csvfile:
	vocab = list(csv.reader(csvfile, delimiter=',', quotechar='|'))
	random_word = random.choice(vocab)
	random_word = str(random_word)

#define variables
word_length = len(random_word)
letter_list = list(random_word)
letter_list = letter_list[2:word_length-2]
display_word = []
wrong_guesses = []
already_guessed = []		


#replace dash with letter
"""word_substring = current_word
start index = 0
get what index the letter is at in the word and then replace at that index in the -s
"""

def index_word(letter_guess):
	for index,letter in enumerate(random_word):
		if letter_guess == letter:
			display_word[index] = letter_guess,
	print " ".join(display_word)

for letter in letter_list:
	display_word.append("_ ") 

#create dashes
			
def play_hangman():
	guesses = 10
	print "".join(display_word)
	if guesses == 10:
		letter_guess = raw_input("Let's start playing! What's your first guess?\n")
	while guesses > 0:
		if letter_guess not in letter_list:
			guesses -= guesses
			already_guessed.append(letter_guess)
			wrong_guesses.append(letter_guess)
			print "Nice try, but no. Guess a new letter.\n"
			print "You have {} guesses left".format(guesses)
			print index_word(letter_guess)
			play_hangman()
		elif letter_guess in already_guessed:	
			letter_guess = raw_input("You already guessed that letter! Try again:\n")
			print "You have {} guesses left".format(guesses)
			print index_word(letter_list)
			play_hangman()
		else:
			guesses -= guesses
			already_guessed.append(letter_guess)	
			word_guess = raw_input("Good work! You guessed {} correctly. Time to guess another!\n".format(letter_guess))
			print "You have {} guesses left".format(guesses)
			print index_word(letter_guess)
			play_hangman()	

play_hangman()

#makes the word harder if user wants
"""while len(random_word) < 4:
	new_word = raw_input("That's an easy word! Do you want a harder one? ")
	new_word = new_word.lower()
	if new_word == "yes":
		random_word = random.choice(vocab)
	else:
		random_word = random_word
		break"""
