print("Welcome to python Pizza Deliveries!")
size = input("size: ").lower()
if size not in ("s", "m", "l"):
    raise Exception("invalid size")


pepperoni = input("pepperoni: ").lower()
if pepperoni not in ("y", "n"):
    raise Exception("invalid pepperoni")

extra_cheese = input("extra_cheese: ").lower()
if extra_cheese not in ("y", "n"):
    raise Exception("invalid extra_cheese")


price = 0

if size == "s":
    price += 15
    if pepperoni == "y":
        price += 2
elif size == "m":
    price += 20
    if pepperoni == "y":
        price += 3
else:
    price += 25
    if pepperoni == "y":
        price += 3


if extra_cheese == " y":
    price += 1

print(f"total price {price}")
