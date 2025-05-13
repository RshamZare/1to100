# Number Guessing Game
# The computer picks a random number from 1–20 and the user tries to guess it.

import random

computer_guess = random.randint(1,100)
user_guess = int(input("What's your best guess? between 1 & 100:"))

if computer_guess == user_guess:
    print("Your did it")
    print("You guessed:", user_guess)
    print("Computer guess:", computer_guess)
else:
    print("NOOOO, YOU CUTIE, THE NUMBER WAS", computer_guess, "HAHHAHA")