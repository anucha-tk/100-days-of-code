from typing import Dict

import questionary
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()


def showTable(bids: Dict[str, int]):
    table = Table(title="🚀 Auction Bids")
    table.add_column("Name", style="cyan", no_wrap=True)
    table.add_column("Bid", style="green")

    for name, bid in bids.items():
        table.add_row(name, str(bid))

    console.print(table)


def run_action():
    bids: Dict[str, int] = {}
    highest_name = ""
    highest_bid = 0

    # console.print(Panel(logo))
    console.print(
        Panel("[bold cyan]🎉 Welcome to the Auction! 🎉[/bold cyan]", expand=False)
    )

    while True:
        name = questionary.text(
            "🔤 What is your name?",
            validate=lambda v: len(v.strip()) >= 1
            or "Name must be at least 1 character",
        ).ask()

        if name in bids:
            console.print("[bold red]⚠️ Name already taken, choose another.[/bold red]")
            continue

        bidding = questionary.password(
            "💰 Your bidding:",
            validate=lambda v: v.isdigit() or "Please enter a number",
        ).ask()
        bidding = int(bidding)

        if bidding > highest_bid:
            highest_name = name
            highest_bid = bidding

        bids[name] = bidding

        more = questionary.confirm("➕ Add another bidder?").ask()
        if not more:
            break

    showTable(bids)
    console.print("\n[bold green]🏁 Bidding is CLOSED![/bold green]\n")
    console.print(
        f"[bold yellow]{highest_name}[/bold yellow] wins with [bold green]${highest_bid}[/bold green] 🎉"
    )


if __name__ == "__main__":
    run_action()
