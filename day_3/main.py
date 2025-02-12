print("welcome to treasure game")
questionOne = input("left or right? ").lower()
if questionOne == "right" or questionOne != "left":
    raise Exception("game over")

questionTwo = input("swim or wait? ").lower()
if questionTwo == "swim" or questionTwo != "wait":
    raise Exception("game over")

questionThree = input("Which door, blue or yellow? ").lower()
if questionThree in ("blue", "yellow") or questionThree != "":
    raise Exception("game over")

print("you win")
