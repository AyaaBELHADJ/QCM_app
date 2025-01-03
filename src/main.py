# installations required :
#pip install ascii-magic rich questionary colorama pyfiglet alive-progress

import ascii_magic
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
import questionary
import ascii_magic
import json
from colorama import Fore, Style, init
import question_manager
from question_manager import QuestionManager


# Initialize the console
console = Console()

# Convert an image to ASCII art
#ascii_art = ascii_magic.from_image("/workspaces/QCM_app/trying/p17s2tfgc31jte13d51pea1l2oblr3.png")
# Add some styled text
#console.print(Text("Dynamic Image-Based Console", style="bold green"))
#console.print(Panel("This is your custom console interface!", style="cyan"))



# Language Selection

choice = questionary.select(
    "Choisissez votre langue / Choose your language : ",
    choices=["fr","eng"]
).ask()

language = choice

# Access a translation

with open("/workspaces/QCM_app/src/translations.json", "r", encoding="utf-8") as file:
    translations = json.load(file)

def get_translation(key, language="eng"):
    return translations.get(key, {}).get(language, "")

#inisialize question manager

python_file = "/workspaces/QCM_app/src/python.json"
question_manager=QuestionManager(python_file,language)

#*************  Starting the program  ******************#

console.print(get_translation("welcome",language))

Nom_utilisateur=input(get_translation("enter_username",language))

# here check if new utilisateur or old

options_new = [
    get_translation("View_Details",language),
    get_translation("Edit_Settings",language),
    get_translation("Start_QCM",language),
    get_translation("Exit",language)
]
options_old = [
    get_translation("View_history",language),
    get_translation("View_Details",language),
    get_translation("Edit_Settings",language),
    get_translation("Start_QCM",language),
    get_translation("Exit",language)
]

#if new choices=options_new else choices=options_old
choices=options_new #change it later

choice = questionary.select(
    get_translation("option_prompt",language),
    choices
).ask()


if choice == get_translation("View_history",language):
    console.print(f"[green]📜 {Nom_utilisateur}'s History[/green]")
    #console.print history


elif choice == get_translation("View_Details",language):
    with open('/workspaces/QCM_app/trying/quiz_details.txt', 'r', encoding='utf-8') as file:
        quiz_details = file.read()
    # Print the content
    console.print(quiz_details)


elif choice == get_translation("Edit_Settings",language):
    console.print("[red]You chose to view details![/red]")


elif choice == get_translation("Start_QCM",language):
    # Start Quiz Logic
    category = question_manager.choose_category()  # User selects a category
    questions = question_manager.get_questions_by_category(category)

    correct_answers = 0
    for question in questions:
        question_text = question_manager.get_question_text(question)
        options = question_manager.get_options_text(question)

        # Display question and options
        answer = questionary.select(
            f"{question_text}",
            choices=options
        ).ask()
        check= question_manager.check_answer(question,answer)
        if check == True:
            console.print("right inswer")
        else:console.print("false inswer")

    console.print("[red]Settings opened!![/red]")


elif choice == get_translation("Exit",language):
    console.print("[red]Goodbye![/red]")

else:
    console.print("[bold red]Invalid option![/bold red]")


from alive_progress import alive_bar
import time

with alive_bar(100) as bar:
    for i in range(100):
        time.sleep(0.03)
        bar()



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