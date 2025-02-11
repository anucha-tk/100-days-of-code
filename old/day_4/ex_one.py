from random import choice

# head or tails
guess = input("What head or tails? (head, tails) ").lower()
choices = ["head", "tails"]
computer_choice = choice(choices)
print(f"result {computer_choice}")
if guess == computer_choice:
    print("You win")
else:
    print("You lose")

# reduce line
# print(
#     f"result {computer_choice} \n{'you win' if guess == computer_choice else 'you lose'}"
# )
