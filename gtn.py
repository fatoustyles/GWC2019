from random import * #imports the ability to get a random number
aRandomNumber = randint(1,20) #generates a random integer
tries = 3
while tries > 0:
    guess = input("Guess a number between 1 and 20 (inclusive): ")
    if not guess.isnumeric(): #checks if a string is only digits 0 to 9
        print("That's not a positive whole number, try again!")
    else:
        tries -= 1
        guess = int(guess) #converts a string to an integer
        if tries == 0:
            print("sorry! no more tries left!")
            break
        if(guess == aRandomNumber):
            print("You're right!")
            break
        elif(guess > aRandomNumber):
            print("The number is too high. Try again!")
        else:
            print("The number is too low. Try again!")
