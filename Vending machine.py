from rich.console import Console
from rich.table import Table
from rich.box import DOUBLE
import pyfiglet

#Vending machine menu
vendingmachine_menu = {
    "Snacks": {
        "A1": {"Name": "M&M's", "Price $": 3.75, "Stock": 10},
        "A2": {"Name": "Lays", "Price $": 1.25, "Stock": 14},
        "A3": {"Name": "Doritos", "Price $": 2.50, "Stock": 9},
        "A4": {"Name": "Takis", "Price $": 4.75, "Stock": 5},
        "A5": {"Name": "Gummy bears", "Price $": 2.00, "Stock": 7},
        "A6": {"Name": "Skittles", "Price $": 3.75, "Stock": 10},
    },
    "Drinks": {
        "B1": {"Name": "RedBull", "Price $": 5.75, "Stock": 30},
        "B2": {"Name": "Seven Up", "Price $": 1.75, "Stock": 17},
        "B3": {"Name": "Mountain Dew", "Price $": 2.75, "Stock": 14},
        "B4": {"Name": "Coca Cola Regular", "Price $": 2.50, "Stock": 12},
        "B5": {"Name": "Grape Juice", "Price $": 1.75, "Stock": 10},
        "B6": {"Name": "Bottled Water", "Price $": 0.50, "Stock": 20},
    },
    "Chocolates": {
        "C1": {"Name": "Milk Chocolate Bar", "Price $": 2.75, "Stock": 11},
        "C2": {"Name": "Dark Chocolate Bar", "Price $": 2.25, "Stock": 5},
        "C3": {"Name": "Caramel-Filled Chocolate Bar", "Price $": 2.75, "Stock": 10},
        "C4": {"Name": "Hazelnut Chocolate Bar", "Price $": 2.75, "Stock": 2},
        "C5": {"Name": "Dark Chocolate With Hazelnut", "Price $": 2.00, "Stock": 10},
    },
    "Ice-Creams": {
        "D1": {"Name": "Vanilla Ice Cream Bar", "Price $": 2.75, "Stock": 15},
        "D2": {"Name": "Chocolate Ice Cream Bar", "Price $": 3.75, "Stock": 12},
        "D3": {"Name": "Brownie Ice Cream Sandwich", "Price $": 3.00, "Stock": 7},
        "D4": {"Name": "Blueberry Sorbet Popsicle", "Price $": 2.25, "Stock": 5},
    },
    "Hot Beverages": {
        "E1": {"Name": "Classic Hot Chocolate", "Price $": 3.75, "Stock": 5},
        "E2": {"Name": "Espresso Shot", "Price $": 2.95, "Stock": 4},
        "E3": {"Name": "Cappuccino", "Price $": 3.75, "Stock": 7},
        "E4": {"Name": "Latte Classic", "Price $": 3.25, "Stock": 15},
        "E5": {"Name": "Latte Vanilla", "Price $": 3.05, "Stock": 9},
        "E6": {"Name": "Mocha", "Price $": 2.95, "Stock": 7},
    },
}

console = Console()

# The menu display function
def display_vendingmachine_menu():
    #Then present a styled header.
    header = pyfiglet.figlet_format("Welcome to My Vending Machine", font="slant")
    console.print(f"[bold cyan]{header}[/bold cyan]", justify="center")

    for category, items in vendingmachine_menu.items():
        console.print(f"\n[bold purple]{category}[/bold purple]\n", justify="center")

        table = Table(show_header=True, header_style="bold magenta", box=DOUBLE, title_style="bold green")
        table.add_column("Code", justify="center", style="bright_yellow")
        table.add_column("Item", justify="left", style="cyan")
        table.add_column("Price ($)", justify="right", style="blue")
        table.add_column("Stock", justify="right", style="red")

        for code, item in items.items():
            stock_status = f"{item['Stock']}" if item["Stock"] > 0 else "[bold red]Out of stock[/bold red]"
            table.add_row(code, item["Name"], f"{item['Price $']:.2f}", stock_status)

        console.print(table, justify="center")

#Being able to manage user input and transactions.
def process_purchase():
    while True:
        display_vendingmachine_menu()
        user_choice = console.input("\n[bold cyan]Enter the item's code to make a purchase. (or 'exit' to end): [/bold cyan]").upper()

        if user_choice == "EXIT":
            console.print("\n[bold green]Thank you for using the vending machine, come again soon![/bold purple]")
            break

        #Check the dictionary for the item.
        item_found = None
        for category, items in vendingmachine_menu.items():
            if user_choice in items:
                item_found = items[user_choice]
                break

        if not item_found:
            console.print("\n[bold red]The code is invalid. Please give it another go.[/bold red]")
            continue

        #Verify if the product is available.
        if item_found["Stock"] <= 0:
            console.print(f"\n[bold red]Sorry, {item_found['Name']} is out of stock:( [/bold red]")
            continue

        #Complete the payment process.
        console.print(f"\n[bold cyan]You selected: {item_found['Name']} (${item_found['Price $']:.2f})[/bold cyan]")
        try:
            payment = float(console.input("[bold green]Enter the desired amount of money to be added: $[/bold green]"))
            if payment < item_found["Price $"]:
                console.print(f"\n[bold red]Insufficient funds. You need ${item_found['Price $'] - payment:.2f} more.[/bold red]")
                continue

            #Calculate change after dispensing the item.
            change = payment - item_found["Price $"]
            item_found["Stock"] -= 1
            console.print(f"\n[bold green]Dispensing, please wait {item_found['Name']}...[/bold green]")
            if change > 0:
                console.print(f"[bold yellow]Your change is: ${change:.2f}[/bold yellow]")
            console.print("[bold green]Thank you for your purchase![/bold green]")

            #Find out if the user would want another item.
            another_item = console.input("\n[bold cyan]Are you interested in buying anything else? (yes/no): [/bold cyan]").strip().lower()
            if another_item != "yes":
                console.print("\n[bold green]Thank you for using the vending machine. come again soon![/bold green]")
                break

        except ValueError:
            console.print("\n[bold red]Invalid amount entered. Please try again.[/bold red]")

#Main program
if __name__ == "__main__":
    process_purchase()