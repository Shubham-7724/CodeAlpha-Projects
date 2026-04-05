#Hangman Game - A simple game where the user has to guess a word one letter at a time and the number of incorrect guesses would be 6.

import random

Words_list = ["ANCHOR" , "BREEZE" , "SCHOOL" , "CACTUS" , "VELVET"]

print("GAME START! You have to guess a word letter by letter. ")
incorrect_guesses = 6
correct_word = random.choice(Words_list)             #computer's choice
Word_display = ["_"] * len(correct_word)             #to show how many letters you've guessed

while incorrect_guesses > 0:
    print("Word = " , Word_display)
    guess = str(input("Enter the letter : "))        #user's choice

    if guess.upper() in correct_word:                #all the cases possible
        print("Correct guess! \n")    
        for index , letter in enumerate(correct_word):
            if letter == guess.upper():
                Word_display[index] = guess.upper()

        if "_" not in Word_display:
            print(Word_display)
            print("You Win! The word was:", correct_word)    #absence of '_' depicts that the user won
            break   

    elif guess.upper() not in correct_word:
        print("Incorrect guess! \n")
        incorrect_guesses = incorrect_guesses - 1            #reduction in no.of chances when user loses
        print("No. of Chances left = " , incorrect_guesses)
        
        if incorrect_guesses == 0:       #user loses when incorrect_guesses hits ZERO
            print("Game Over!")

    else:
        print("Invalid input! ")





