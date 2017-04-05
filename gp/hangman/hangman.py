import random
#change
"""initiate global variables"""

#open file of 4k words
f = open("4000-most-common-english-words-csv.csv","r")
HANGMAN_DICTIONARY = f.read().splitlines()

for word in HANGMAN_DICTIONARY:
	if len(word)<3:
		HANGMAN_DICTIONARY.remove(word)

#maximum number of wrong guesses allowed
MAX_WRONG = 6


"""initialize all tracking variables including: 
total_guesses, letters_guessed, letters_wrong, letters_right"""
def initialize_game():
	total_guesses = 0 #initialize total_guesses
	letters_wrong = [] # initialize letters_wrong

	#call new_word
	new_word(total_guesses, letters_wrong)


"""Pick a new word"""
def new_word(total_guesses,letters_wrong):

	#pick a random word from the dictionary 
	current_word = random.choice(HANGMAN_DICTIONARY)

	#set letters_right equal to a blank version of current_word
	letters_right = ["_"] * len(current_word)

	#call guess
	guess(total_guesses, letters_wrong, letters_right, current_word)


"""Verify that the user has input a valid letter"""
def verify_input(letter):
	#check for valid input
	if (len(letter) != 1 or not letter.isalpha()):
		print "ATTN: You must enter exactly one letter at a time"
		return False
	else:
		return True



"""Check if the guessed letter has already been entered"""
def already_guessed(letter, letters_right, letters_wrong):
	if(letter in letters_right or letter in letters_wrong):
		print "ATTN: You need to guess a new letter"
		return False
	else:
		return True

"""Check if the letter is part of the current_word
If the letter is part of the word, return True
If the letter is not part of the word, return False"""
def check_letter(letter, current_word):
	if letter in current_word:
		return True
	else:
		return False

def letter_correct(letters_right,current_word,letter):
	word_substring = current_word
	start_index = 0
	while (letter in word_substring):
		substring_index = word_substring.index(letter)
		index = start_index + substring_index
		letters_right[index] = letter
		start_index = index + 1
		word_substring = word_substring[substring_index + 1:]
	return letters_right


def game_won(total_guesses, letters_right, current_word):
	if ("_" not in letters_right):
		print "Congrats! You won! The word is: " + "".join(current_word)
		print "It took you " + str(total_guesses) + " guesses"
		play_again = raw_input("Want to play again? (Y/N): ").lower()
		
		if(play_again == "y"): 
			print"Here we go!"
			initialize_game()
		else: 
			exit()
	else: 
		return False


def game_lost(letters_wrong, current_word):
	if (len(letters_wrong) >= MAX_WRONG):
		print "You lost"
		print "The word was: " + current_word
		play_again = raw_input("Want to play again? (Y/N): ").lower()
		if(play_again == "y"): 
			print"Here we go!"
			initialize_game()
		else: 
			exit()
	
	#the user has not lost, so keep playing
	else:
		return False



"""Preconditions: a word has been chosen and a guess has been made
Check if the letter is part of the chosen word
and return the word with all correct letters and blanks"""
def guess(total_guesses, letters_wrong, letters_right, current_word):

	#variable to track current state: 0 = don't guess again; 1 = guess again
	guess_state = 0 

	print "============== GUESS NUMBER " + str(total_guesses + 1) + " =============="
	
	if (len(letters_wrong) > 0):
		#print the wrong letters
		print "The following letters are not in your word: " + " ".join(letters_wrong)

	#show the word so far
	print "Your word so far is: " + " ".join(letters_right)
	
	#display remaining moves
	print "You have " + str(MAX_WRONG - len(letters_wrong)) + " wrong moves left"

	#prompt the letter input
	letter = raw_input("Guess a letter: ").lower()

	#check that the input is valid
	if not verify_input(letter):
		guess(total_guesses, letters_wrong, letters_right, current_word)

	#check if letter has already been guessed
	elif  not already_guessed(letter, letters_right, letters_wrong):
		guess(total_guesses, letters_wrong, letters_right, current_word)
	
	#check if the letter is in the word
	elif check_letter(letter, current_word):
		letters_right = letter_correct(letters_right, current_word,letter)
		total_guesses += 1
		
		#if the user has not won, guess again
		if  not game_won(total_guesses, letters_right, current_word):
			guess(total_guesses, letters_wrong, letters_right, current_word)
	
	#the letter is incorrect
	else:
		print "The letter '" + letter + "' is not in the word"
		if not game_lost(letters_wrong, current_word):
			letters_wrong.append(letter)
			total_guesses += 1
			guess(total_guesses, letters_wrong, letters_right, current_word)
	

"""initiate game"""
initialize_game()

