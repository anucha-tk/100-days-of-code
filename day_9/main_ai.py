import os
from typing import Dict

# Try both import styles to match how you run scripts (same pattern used elsewhere in workspace)
try:
    from art import logo
except Exception:
    from day_9.art import logo


def clear_screen() -> None:
    os.system("cls" if os.name == "nt" else "clear")


def run_auction() -> None:
    bids: Dict[str, int] = {}

    while True:
        print(logo)
        name = input("What is your name? ").strip()
        if not name:
            print("Please enter a name.")
            continue

        bid_str = input("What's your bid? $").strip()
        try:
            bid = int(float(bid_str))
        except ValueError:
            print("Invalid bid. Enter a numeric value.")
            continue

        bids[name] = bid

        more = (
            input("Are there any other bidders? Type 'yes' or 'no': ").strip().lower()
        )
        if more.startswith("y"):
            clear_screen()
            continue

        # determine winner
        if bids:
            winner_name, winner_bid = max(bids.items(), key=lambda kv: kv[1])
            print(f"The winner is {winner_name} with a bid of ${winner_bid}")
        else:
            print("No bids were placed.")
        break


if __name__ == "__main__":
    run_auction()
