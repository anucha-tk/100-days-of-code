# Exercise 1
# num = input("what number ?")
# numIndexOne = num[0]
# numIndexTwo = num[1]
# print(int(numIndexOne) + int(numIndexTwo))


# Exercise 2 BMI Calculate
# height = float(input("enter your height: "))
# weight = float(input("enter your weight: "))
# print(int(weight / (height**2)))

# Exercise 3 Lift in week
# age = int(input("enter your age: "))
# remaining_year = 90 - age
# day_remaining = remaining_year * 365
# week_remaining = remaining_year * 52
# month_remaining = remaining_year * 12

# print(
#     f"You have {day_remaining} days, {week_remaining} weeks, and {month_remaining} months left."
# )

# project Tip Calculate
print("Welcome to the tip calculate")
bill = float(input("What was the total bill? $"))
tip_percentage = int(
    input("What percentage tip would you like to give 10, 12, or 15? ")
)
people = int(input("How many people to split the bill? "))
bill_each_person = round((((bill * tip_percentage) / 100) + bill) / people, 2)
print(f"Each person should pay: ${bill_each_person}")
