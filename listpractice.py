# alist = [0,1,2,3,4]
# for num in alist:
#         print(type(num), num)


# #pseudocode
# total = 0
# ages = [5,12,3,56,24,78,1,15,44]
# #find sum
# #divide from total number of integers
# #print value
# for sum in ages:
#     total += sum
# print(f"total sum:{total}")
# l = len(ages)
# avg  = total/l
# print(avg)


#guess the word
import random

# A list of words that
# potential_words = ["example", "words", "someone", "can", "guess"]
#
# word = random.choice(potential_words)
#
# # Use to test your code:
# # print(word)
#
# # Converts the word to lowercase

# Make it a list of letters for someone to guess
letters = ['b', 'i', 'c', 'y' 'c', 'l','e']
c = [2];[4]
word = "bicycle"
word = word.lower()
wordlist = list(word) #b i c y c l e
# TIP: the number of letters should match the word
print(f"There are {len(letters)} in the word.")
currentword = "_"*len(letters)
currentwordlist = list(currentword)
# Some useful variables
guesses = []
maxfails = 7
fails = 0

while fails < maxfails:
	guess = input("Guess a letter: ")

	# check if the guess is valid: Is it one letter? Have they already guessed it?
    if guess.isalpha():
        print("Invalid input! It's not a letter!")
        continue
    if guess != current_word:
        # maxfails -= 1
        # print(f"That letter is not in the word. You have {maxfails} guesses left.")
        fails = fails+1
    	print("You have " + str(maxfails - fails) + " tries left!")
        guesses.append(input)
        print(guesses)
# check if the guess is correct: Is it in the word? If so, reveal the letters!
    if guess in letters:
        index1 = wordlist.index(guess)
        currentwordlist[index1] = guess
