from src.user_management import UserManager
from src.question_manager import QuestionManager
from src.feedback import Feedback
from src.timer import Timer
from src.export import Export
from colorama import Fore, Style, init
import json

# Initialize colorama
init(autoreset=True)

def main():
    print(Fore.CYAN + Style.BRIGHT + "Bienvenue au QCM Informatique ! / Welcome to the Informatics Quiz!")
    
    # Language Selection
    language = input(Fore.YELLOW + "Choisissez votre langue / Choose your language (fr/en): ").strip().lower()
    if language not in ["fr", "en"]:
        language = "en"

    translations = {
        "welcome": {"fr": "Bienvenue au QCM Informatique !", "en": "Welcome to the Informatics Quiz!"},
        "enter_username": {"fr": "Entrez votre nom d'utilisateur : ", "en": "Enter your username: "},
        "history": {"fr": "Historique de", "en": "History for"},
        "add_test": {"fr": "Voulez-vous ajouter un test ? (o/n) : ", "en": "Do you want to add a test? (y/n): "},
        "category_prompt": {"fr": "Choisissez une catégorie : ", "en": "Choose a category: "},
        "question_prompt": {"fr": "Question", "en": "Question"},
        "your_answer": {"fr": "Votre réponse : ", "en": "Your answer: "},
        "final_score": {"fr": "Votre score final : ", "en": "Your final score: "},
        "export_results": {"fr": "Voulez-vous exporter les résultats ? (o/n) ", "en": "Do you want to export the results? (y/n): "}
    }

    print(Fore.CYAN + Style.BRIGHT + translations["welcome"][language])

    user_manager = UserManager()
    question_manager = QuestionManager()

    # Gestion des utilisateurs
    username = input(Fore.YELLOW + translations["enter_username"][language])
    user = user_manager.get_or_create_user(username)
    
    print(Fore.GREEN + f"\n{translations['history'][language]} {username}:")
    user_manager.display_history(user)

    # Ajouter un test (optionnel)
    add_test = input(Fore.YELLOW + translations["add_test"][language]).strip().lower()
    if add_test in ["o", "y"]:
        question_manager.add_test(language)

    # Choisir une catégorie (optionnel)
    category = question_manager.choose_category(language)

    # Charger les questions
    questions = question_manager.load_questions(category)

    # Démarrer le QCM
    score = 0
    for i, question in enumerate(questions):
        print(Fore.BLUE + f"\n{translations['question_prompt'][language]} {i+1}: {question['question']}")
        for idx, option in enumerate(question['options'], 1):
            print(Fore.MAGENTA + f"{idx}) {option}")
        
        if Timer.enabled():
            Timer.start()
        answer = input(Fore.YELLOW + translations["your_answer"][language])
        if Timer.enabled():
            Timer.stop()

        is_correct = question_manager.check_answer(question, answer)
        Feedback.provide_feedback(is_correct, question, language)
        if is_correct:
            score += 1

    print(Fore.CYAN + f"\n{translations['final_score'][language]} {score}/{len(questions)}")

    # Sauvegarder les résultats
    user_manager.save_result(user, score)

    # Exporter les résultats (optionnel)
    if input(Fore.YELLOW + translations["export_results"][language]).strip().lower() in ["o", "y"]:
        Export.to_csv(user)

if __name__ == "__main__":
    main()
