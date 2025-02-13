import random
import string

letters = list(string.ascii_letters)  # Uses built-in method
numbers = list(string.digits)
symbols = list("!#$%&()*+")


def check(arr: list[str], n: int):
    if n > len(arr):
        raise ValueError(f"number must below {n}")


print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
check(letters, nr_letters)

nr_symbols = int(input("How many symbols would you like?\n"))
check(symbols, nr_symbols)

nr_numbers = int(input("How many numbers would you like?\n"))
check(numbers, nr_numbers)
password = (
    random.choices(letters, k=nr_letters)
    + random.choices(symbols, k=nr_symbols)
    + random.choices(numbers, k=nr_numbers)
)
random.shuffle(password)
password = "".join(password)
print(f"This is password generate by length: {len(password)} is: {password}")
