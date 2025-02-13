import random

choices = ["rock", "paper", "scissors"]

print("Welcome to Pic Pac Pok!")

# Keep asking until player gives a valid choice
while True:
    player = input("Choose rock, paper, or scissors: ").lower()
    if player in choices:
        break
    print("Invalid choice! Please choose rock, paper, or scissors.")

computer = random.choice(choices)

outcomes = {
    ("rock", "scissors"): "Win",
    ("paper", "rock"): "Win",
    ("scissors", "paper"): "Win",
}

if player == computer:
    result = "Draw"
elif (player, computer) in outcomes:
    result = "Win"
else:
    result = "Lose"

print(f"{result}!, you: {player} - computer: {computer}")
