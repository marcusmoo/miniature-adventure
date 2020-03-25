import random
import time
moves = ("rock", "paper", "scissors")
keep_playing = "true"
while keep_playing == "true":
    cmove = random.choice(moves)
    pmove = input("What is your move? (rock/paper/scissors) ")
    time.sleep(.5)
    print("The computer chose",cmove)
    if cmove == pmove:
     print("Tie")
    elif pmove.lower().strip() == "rock" and cmove == "scissors":
        print("Player wins!")
    elif pmove.lower().strip() == "rock" and cmove == "paper":
        print("Computer wins")
    elif pmove.lower().strip() == "paper" and cmove == "scissors":
        print("Computor wins")
    elif pmove.lower().strip() == "paper" and cmove == "rock":
        print("Player wins!")
    elif pmove.lower().strip() == "scissors" and cmove == "rock":
        print("Computer wins")
    elif pmove.lower().strip() == "scissors" and cmove == "paper":
        print("Player wins!")
    else:
        print("Invalid move")


