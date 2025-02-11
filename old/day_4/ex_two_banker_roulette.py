import random

names = input("list you friends.(use nick name and write space)")
friend_split = names.split(" ")
random_num = random.randint(0, len(friend_split) - 1)
print(f"{friend_split[random_num]} is going to buy the meal today!")
