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
from timer import Timer
import threading
from user_managment import UserManager
# Initialize the console
console = Console()

penalty_scoring="Disabled"

import pyfiglet



# Language Selection

choice = questionary.select(
    "Choisissez votre langue / Choose your language : ",
    choices=["fr","eng"]
).ask()

language = choice

# Access a translation

with open(r"C:\Users\HP\OneDrive\Desktop\QCM_app\src\translations.json", "r", encoding="utf-8") as file:

    translations = json.load(file)

def get_translation(key, language="eng"):
    return translations.get(key, {}).get(language, "")

#inisialize question manager and user managment

python_file = "./src/python.json"
user_file="./src/users.json"

question_manager=QuestionManager(python_file,language)

user_manager=UserManager(user_file,question_manager)

#*************  Starting the program  ******************#


console.print(get_translation("welcome",language))

Nom_utilisateur=input(get_translation("enter_username",language))




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

if(user_manager.user_exists(Nom_utilisateur)):
    choices=options_old
else:
    choices=options_new
    

user_data = user_manager.get_or_create_user(Nom_utilisateur)


choice=None
while choice!= get_translation("Exit",language):
    choice = questionary.select(
    get_translation("option_prompt",language),

    choices
    ).ask()


    if choice == get_translation("View_history",language):
        if language== 'eng':
            console.print(f"[green]📜 {Nom_utilisateur}'s History[/green]")
        else:
            console.print(f"[green]📜 Historique de {Nom_utilisateur}[/green]")
        user_manager.display_history(user_data)


    elif choice == get_translation("View_Details",language):
        details = get_translation("quiz_details",language)
        print("Quiz Details:")
        print(f"📚  {details['topics_covered']}")
        print(f"🔢  {details['number_of_questions']}")
        print(f"⏳  {details['time_limit']}")
        print(f"✅  {details['scoring']}")
        print(f"💡  {details['feedback']}")
        print(f"📝  {details['records']}")


    elif choice == get_translation("Edit_Settings",language):
        console.print("[red]You chose to Edit_Settings![/red]")
        penalty_scoring = questionary.select(
            "Do you want to enable penalty scoring?",
            choices=["Enabled", "Disabled"],
        ).ask()

    elif choice == get_translation("Start_QCM",language):
        # Start Quiz Logic
        category = question_manager.choose_category()  # User selects a category
        questions = question_manager.get_questions_by_category(category)
        if penalty_scoring=="Enabled":
            question_manager.is_simple_scoring =False

        #question_manager.score = 0
        #correct_answers = 0

        timer=Timer(10)
        timer_thread = threading.Thread(target=timer.start)
        timer_thread.daemon = True  # Make sure the thread stops when the main program ends
        timer_thread.start()
        for question in questions:
            
            if not timer.time_limit:
                break
            question_text = question_manager.get_question_text(question)
            options = question_manager.get_options_text(question)

            # Display question and options
            answer = questionary.select(
                f"{question_text}",
                choices=options
            ).ask()
            feedback = question_manager.check_answer(question, answer)
            console.print(feedback)

        console.print("Votre score is")
        console.print(question_manager.score)
        console.print("[red]Settings opened!![/red]")

        user_manager.save_result(user_data, question_manager.score, category)


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





message = "Loading your beautiful console..."
for char in message:
    print(char, end='', flush=True)
    time.sleep(0.1)  # Adjust speed
print("\nDone!")

from colorama import Fore, Back, Style, init
init(autoreset=True)

print(Fore.CYAN + "Welcome to your beautiful Python console!")
print(Style.BRIGHT + Back.YELLOW + "This is highlighted text!")

