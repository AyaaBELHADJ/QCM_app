
import json

class QuestionManager:
    def __init__(self, question_file, language="eng",is_simple_scoring=True):
        """
        Initialize the QuestionManager with the file containing questions.
        Args:
        - question_file (str): Path to the JSON file with the questions.
        - language (str): The language to use for the questions (default is "eng").
        """
        self.language = language
        self.question_file = question_file
        self.questions = []
        self.score = 0 
        self.is_simple_scoring = is_simple_scoring 
        self.load_questions()

    def load_questions(self):
        """
        Load questions from the JSON file into memory.
        """
        with open(self.question_file, 'r', encoding='utf-8') as file:
            data = json.load(file)
            self.questions = data["questions"]

    def get_questions_by_category(self, category=None):
        """
        Get questions for a specific category or all questions.
        Args:
        - category (str): The category of questions to retrieve (optional).
        Returns:
        - list: A list of questions filtered by category.
        """
        if category:
            return [q for q in self.questions if q["category"][self.language] == category]
        return self.questions

    def choose_category(self):
        """
        Display available categories and let the user choose one.
        """
        categories = {q['category'][self.language] for q in self.questions}
        print("Available categories:")
        for idx, category in enumerate(categories, 1):
            print(f"{idx}. {category}")
        
        choice = int(input(f"Enter the number of the category ({', '.join(categories)}): ")) - 1
        return list(categories)[choice]


    def check_answer(self, question, user_answer):
        """
        Check if the user's answer is correct and provide feedback.
        Args:
        - question (dict): The question dictionary.
        - user_answer (str): The user's answer.
        Returns:
        - bool: True if the answer is correct, False otherwise.
        - str : Feedback message
        """
        correct_answer = question['answer'][self.language]
        feedback_messages={
            "eng": {
            "correct": "Correct! Well done.",
            "incorrect": f"Incorrect. The correct answer was: {correct_answer}."
        },
        "fr": {
            "correct": "Correct! Bien joué.",
            "incorrect": f"Incorrect. La bonne réponse était : {correct_answer}."
        }
        }
        messages=feedback_messages.get(self.language, feedback_messages["eng"])
        if user_answer.strip().lower() == correct_answer.strip().lower():
            self.score += 1  # Si la réponse est correcte, augmenter le score
           
            return True, messages["correct"]
        else:
            if not self.is_simple_scoring:
                self.score -= 1  # Subtract 1 for incorrect answers in penalty mode
            return False, messages["incorrect"]
    def get_question_text(self, question):
        """
        Retrieve the question text in the current language.
        Args:
        - question (dict): The question dictionary.
        Returns:
        - str: The question text in the current language.
        """
        return question['question'][self.language]

    def get_options_text(self, question):
        """
        Retrieve the options in the current language.
        Args:
        - question (dict): The question dictionary.
        Returns:
        - list: The list of options in the current language.
        """
        return question['options'][self.language]
    def display_score(self):
    
    # Messages de feedback dans différentes langues
     feedback_messages = {
        "eng": {
            "excellent": "Excellent! You got all the answers right.",
            "good_job": "Good job! You did well.",
            "keep_practicing": "Keep practicing! You'll improve next time."
        },
        "fr": {
            "excellent": "Excellent! Vous avez toutes les réponses correctes.",
            "good_job": "Bon travail! Vous avez bien réussi.",
            "keep_practicing": "Continuez à pratiquer! Vous vous améliorerez la prochaine fois."
        }
    }
    
    # Sélectionner le bon message selon la langue
     messages = feedback_messages.get(self.language, feedback_messages["eng"])
    
    # Affichage du score
     print(f"Your final score is: {self.score}/{len(self.questions)}")
    
    # Affichage du feedback basé sur le score
     if self.score == len(self.questions):
        print(messages["excellent"])
     elif self.score > len(self.questions) / 2:
        print(messages["good_job"])
     else:
           print(messages["keep_practicing"])
