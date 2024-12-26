## test 



import ascii_magic
from rich.console import Console
from rich.panel import Panel
from rich.text import Text

import ascii_magic
print(dir(ascii_magic))

# Initialize the console
console = Console()

# Convert an image to ASCII art
ascii_art = ascii_magic.from_image(" data/brand.png")

# Display the ASCII art
console.print(Panel(ascii_art, title="Welcome!", subtitle="ASCII Art", expand=False))

# Add some styled text
console.print(Text("Dynamic Image-Based Console", style="bold green"))
console.print(Panel("This is your custom console interface!", style="cyan"))

# Add some dynamic interactivity (example)
console.print("[bold magenta]Choose an option:[/bold magenta]")
options = [
    "[1] View Details",
    "[2] Edit Settings",
    "[3] Exit"
]
for option in options:
    console.print(option)

# Handle user input
choice = input("\nEnter your choice: ")
if choice == "1":
    console.print("[green]You chose to view details![/green]")
elif choice == "2":
    console.print("[yellow]Settings opened![/yellow]")
elif choice == "3":
    console.print("[red]Goodbye![/red]")
else:
    console.print("[bold red]Invalid option![/bold red]")


from alive_progress import alive_bar
import time

with alive_bar(100) as bar:
    for i in range(100):
        time.sleep(0.03)
        bar()
#



import questionary

choice = questionary.select(
    "Choose an option:",
    choices=["Option 1", "Option 2", "Exit"]
).ask()

print(f"You chose: {choice}")

import time

message = "Loading your beautiful console..."
for char in message:
    print(char, end='', flush=True)
    time.sleep(0.1)  # Adjust speed
print("\nDone!")

from colorama import Fore, Back, Style, init
init(autoreset=True)

print(Fore.CYAN + "Welcome to your beautiful Python console!")
print(Style.BRIGHT + Back.YELLOW + "This is highlighted text!")

import pyfiglet

ascii_art = pyfiglet.figlet_format("Welcome!")
print(ascii_art)


