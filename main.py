r = 'rock'
p = 'paper'
s = 'scissors'

import random

choices = [r, p, s]

computer = random.choice(choices)

player = input("Pick an option between: rock, paper or scissors ")


if player == computer:
    print("CPU: ", computer)
    print("player: ", player)
    print("Tie!")
elif player == "rock":
    if  computer == "p":
        print("CPU: ", computer)
        print("player: ",player)
        print("You Lose!")
    if  computer == "s":
        print("CPU: ", computer)
        print("player: ",player)
        print("You Win!")
elif player == "scissors":
    if  computer == "p":
        print("CPU: ", computer)
        print("player: ",player)
        print("You Win!")
    if  computer == "r":
        print("CPU: ", computer)
        print("player: ",player)
        print("You Lose!")
elif player == "paper":
    if  computer == "s":
        print("CPU: ", computer)
        print("player: ",player)
        print("You Lose!")
    if  computer == "r":
        print("CPU: ", computer)
        print("player: ",player)
        print("You Win!")
