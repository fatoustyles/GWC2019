import random

potential_words = ["stanloona", "hello", "bang", "cnco", "dimelo", "lunay", "hobi", "olivia", "liana","sydney", "streamclimaxxx", "queen"]

word = random.choice(potential_words)

# Converts the word to lowercase
word = word.lower()
#Make it a list of letters for someone to guess
#current_word = ["_", "_"] # TIP: the number of letters should match the word NEW VER BELOW
current_word = list(word)
# print(word)
# # Some useful variables
guesses = [] #holds all previously guessed letters
maxfails = 7
fails = 0

while fails < maxfails:
	guess = input("Guess a letter: ").lower()
	if guess.isalpha() and len(guess) == 1 and guess not in guesses:
		#guess is a single letter and is NEW
		guesses.append(guess)
		if guess in current_word:
			#our guess is right
			print("You guessed a letter correctly!")
		else:
			#our guess is wrong
			fails += 1
			print("You guessed a letter incorrectly!")
	else:
		#not valid input
		print(f"Invalid answer: {guess}")

	print("You have " + str(maxfails - fails) + " tries left!")

	display = ""
	winning = ""
	for i in current_word:
		if i in guesses:
			display += i + " "
			winning += i
			# print(i)
		else:
			display += "_ "
			# print("_ ")
	print(winning)
	if winning == word:
		print("You won!")
		exit(0)
leave = exit(0)
