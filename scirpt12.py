# rock paper scissor game with py

import random

choices = ["rock","paper", "scissor" ]
player_score = 0
computer_score = 0
tie_score = 0

while True:
    player = input("\nChoose your weapon: Rock/Paper/Scissor: (q for quit)").lower()

    if player == "q":
        print("you pussed out, thanks for playing anyways")
        break
    if player not in choices:
        print("invalid choice")
        continue 
    
    # Program starts
    computer = random.choice(choices)
    print(f"Computer choice = {computer}")

    if player == computer:
        print(f"It's a tie {computer} = {player}")
        tie_score += 1 
    elif (player == "rock" and computer == "scissors") or \
         (player == "paper" and computer == "rock") or \
         (player == "scissor" and computer == "paper"):
         print("you won!")
         player_score += 1
    else:
        print("you lost")
        computer_score += 1 
        
    print(f"scores: computer: {computer_score} | player: {player_score} | ties: {tie_score}")