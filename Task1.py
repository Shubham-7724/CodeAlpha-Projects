#Hangman Game - A simple game where the user has to guess a word one letter at a time and the number of incorrect guesses would be 6.

import random

Words_list = ["ANCHOR" , "BREEZE" , "SCHOOL" , "CACTUS" , "VELVET"]

print("GAME START! You have to guess a word letter by letter. ")
incorrect_guesses = 6
correct_word = random.choice(Words_list)
Word_display = ["_"] * len(correct_word)

while incorrect_guesses > 0:
    print("Word = " , Word_display)
    guess = str(input("Enter the letter : "))

    if guess.upper() in correct_word:
        print("Correct guess! \n")    
        for index , letter in enumerate(correct_word):
            if letter == guess:
                Word_display[index] = guess.upper()

        if "_" not in Word_display:
            print("You Win! The word was:", correct_word)
            break

    elif guess.upper() not in correct_word:
        print("Incorrect guess! \n")
        incorrect_guesses = incorrect_guesses - 1
        print("No. of Chances left = " , incorrect_guesses)
        
        if incorrect_guesses == 0:
            print("Game Over!")

    else:
        print("Invalid input! ")





