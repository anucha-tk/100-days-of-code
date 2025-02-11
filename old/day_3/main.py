# height = int(input("what your height? "))
# if height > 120:
#     print("your can ride bike")
#     age = int(input("What your age? "))
#     if age > 18:
#         print("pay $10")
#     else:
#         print("pay $8.50")
# else:
#     print("wait you height")

# exercise 1 odd or even
# num = int(input("What number you should check? "))
# result = num % 2
# if result == 0:
#     print("this is an even number")
# else:
#     print("this is an odd number")

# exercise 2 BIM v.2
# height = float(input("enter your height(m): "))
# weight = float(input("enter your weight(kg): "))
# bim = round(weight / (height**2))
# if bim > 35:
#     print("Your are clinically obese")
# elif bim > 30:
#     print("Your are obese")
# elif bim > 25:
#     print("Your are slightly overweight")
# elif bim > 18.5:
#     print("Your are normal weight")
# else:
#     print("Your are underweight")

# exercise 3 leap year
# year = int(input("What year you should check? "))
# is_cal_4 = year % 4 == 0
# is_cal_100 = year % 100 == 0
# is_cal_400 = year % 400 == 0

# if is_cal_4:
#     if is_cal_100:
#         if is_cal_400:
#             print("This year is leap!")
#         else:
#             print("This year is not leap!")
#     else:
#         print("This year is leap!")
# else:
#     print("This year is not leap!")

# exercise 3 pizza order
# print("Welcome to Pizza Delivery")
# get_size = input("What size pizza do you want? (S, M, L): ")
# while get_size.upper() not in ["S", "M", "L"]:
#     print("Invalid size. Please enter S, M, or L.")
#     get_size = input("What size pizza do you want? (S, M, L): ")

# get_pep = input("Do you want pepperoni? Y or N ").upper()
# # your can validate input
# get_extra_cheese = input("Do you want extra cheese? Y or N ").upper()

# if get_size == "S":
#     bill = 15
# elif get_size == "M":
#     bill = 20
# else:
#     bill = 25

# if get_pep == "Y":
#     if get_size == "S":
#         bill += 2
#     else:
#         bill += 3

# if get_extra_cheese == "Y":
#     bill += 1

# print(f"Your final bill is: ${bill}")

# exercise 4 love letter cal

# name_one = [*input("What is your name? ").upper()]
# name_two = [*input("What is their name? ").upper()]
# concat_name = name_one + name_two

# c_true = 0
# for letter in concat_name:
#     if letter in ["T", "R", "U", "E"]:
#         c_true += 1

# c_love = 0
# for letter in concat_name:
#     if letter in ["L", "O", "V", "E"]:
#         c_love += 1
# score = int(str(c_true) + str(c_love))

# if score < 10 or score > 90:
#     print(f"Your score is {score}, you go together like coke and mentos.")
# elif score >= 40 and score <= 50:
#     print(f"Your score is {score}, you are alright together.")
# else:
#     print(f"Your score is {score}.")

# better
# def count_letters(concat_name, letters):
#     return sum(letter in letters for letter in concat_name)


# def get_score(name_one, name_two):
#     concat_name = name_one + name_two
#     c_true = count_letters(concat_name, ["T", "R", "U", "E"])
#     c_love = count_letters(concat_name, ["L", "O", "V", "E"])
#     return int(str(c_true) + str(c_love))


# def print_result(score):
#     if score < 10 or score > 90:
#         print(f"Your score is {score}, you go together like coke and mentos.")
#     elif score >= 40 and score <= 50:
#         print(f"Your score is {score}, you are alright together.")
#     else:
#         print(f"Your score is {score}.")


# name_one = [*input("What is your name? ").upper()]
# name_two = [*input("What is their name? ").upper()]
# score = get_score(name_one, name_two)
# print_result(score)

# final project find treasure island
print(
    r'''*******************************************************************************
              |                   |                  |                     |
     _________|________________.=""_;=.______________|_____________________|_______
    |                   |  ,-"_,=""     `"=.|                  |
    |___________________|__"=._o`"-._        `"=.______________|___________________
              |                `"=._o`"=._      _`"=._                     |
     _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
    |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
    |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
              |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
     _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
    |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
    |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
    ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
    /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
    ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
    /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
    ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
    /______/______/______/______/______/______/______/______/______/______/[TomekK]
    *******************************************************************************'''
)
print("Welcome to Treasure Island.Your mission is to find the treasure.")
# choice one
print(
    r"""
        _.-"/______________________/////  \\\\\_____________________\"-._
        `'-.\~~~~~~~~~~~~~~~~~~~~~~\\\\\  /////~~~~~~~~~~~~~~~~~~~~~/.-'
    """
)
choose_one = input("Left or Right? ").upper()
while choose_one.upper() not in ["LEFT", "RIGHT"]:
    print("Invalid choose. Please enter Left or Right")
    choose_one = input("Left or Right? ").upper()
# choice one result
if choose_one == "RIGHT":
    print("Fall into the hole. Game Over!!!")
    exit()

# choice two
print(
    r"""
                 ___
               /`  _\
               |  / 0|--.
          -   / \_|0`/ /.`'._/)
      - ~ -^_| /-_~ ^- ~_` - -~ _
      -  ~  -| |   - ~ -  ~  -
             \ \, ~   -   ~
              \_| 
        """
)
choose_two = input("Swim or wait? ").upper()
while choose_two.upper() not in ["SWIM", "WAIT"]:
    print("Invalid choose. Please enter swim or wait")
    choose_two = input("Swim or wait? ").upper()
# choice two result
if choose_two == "SWIM":
    print("Attacked by trout. Game Over")
    exit()

# choice three
print(
    r"""
     ______              ______             ______
   ,-' ;  ! `-.       ,-' ;  ! `-.       ,-' ;  ! `-.
  / :  !  :  . \     / :  !  :  . \     / :  !  :  . \
 |_ ;   __:  ;  |   |_ ;   __:  ;  |   |_ ;   __:  ;  |
 )| .  :)(.  !  |   )| .  :)(.  !  |   )| .  :)(.  !  |
 |"    (RED) _  |   |"   (BLUE) _  |   |"  (YELLOW) _ |
 |  :  ;`'  (_) (   |  :  ;`'  (_) (   |  :  ;`'  (_) (
 |  :  :  .     |   |  :  :  .     |   |  :  :  .     |
 )_ !  ,  ;  ;  |   )_ !  ,  ;  ;  |   )_ !  ,  ;  ;  |
 || .  .  :  :  |   | .  .  :  :  |    || .  .  :  :  |
 |" .  |  :  .  |   |" .  |  :  .  |   |" .  |  :  .  |
 |mt-2_;----.___|   |mt-2_;----.___|   |mt-2_;----.___|
        """
)
choose_three = input('Which door? ("Red", "Blue" , "Yellow") ').upper()
# choice three result
if choose_three == "RED":
    print("Burned by fire. Game Over!!")
elif choose_three == "BLUE":
    print("Eaten by beasts. Game Over!!")
elif choose_three == "YELLOW":
    print("You Win!")
else:
    print("Game Over!!")
