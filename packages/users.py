from typing import Any

usernames = [
    {"name": "anucha", "age": 29},
    {"name": "zom", "age": 32},
    {"name": "da", "age": 56},
    {"name": "thep", "age": 61},
    {"name": "dondanai", "age": 38},
]


def print_name(people: dict[str, Any]):
    print(people["name"])
