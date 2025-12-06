import questionary
from art import logo
from rich.console import Console

console = Console()


def add(n1, n2):
    """Adds two numbers"""
    return n1 + n2


def subtract(n1, n2):
    """Subtracts two numbers"""
    return n1 - n2


def multiply(n1, n2):
    """Multiplies two numbers"""
    return n1 * n2


def divide(n1, n2):
    """Divides two numbers"""
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
    "**": lambda n1, n2: n1**n2,
    "%": lambda n1, n2: n1 % n2,
}


def get_number(prompt):
    return float(
        questionary.text(
            prompt,
            validate=lambda text: text.replace(".", "", 1).isdigit()
            or "Enter a valid number",
        ).ask()
    )


def get_operation():
    return questionary.text("Pick an operation: ").ask()


def perform_calculation(num1, num2, operation_symbol):
    calculation_function = operations[operation_symbol]
    if operation_symbol == "/" and num2 == 0:
        console.print("[bold red]Error: Cannot divide by zero![/bold red]")
        return num1
    else:
        return calculation_function(num1, num2)


def calculator():
    """A simple calculator that can perform continuous calculations."""
    print(logo)

    num1 = get_number("What's the first number?: ")
    for symbol in operations:
        print(symbol)

    while True:
        operation_symbol = get_operation()
        num2 = get_number("What's the next number?: ")
        answer = perform_calculation(num1, num2, operation_symbol)

        console.print(
            f"\n[bold green]{num1} {operation_symbol} {num2} = {answer}[/bold green]\n"
        )

        if (
            questionary.text(
                f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: "
            ).ask()
            == "y"
        ):
            num1 = answer
        else:
            calculator()


if __name__ == "__main__":
    calculator()
